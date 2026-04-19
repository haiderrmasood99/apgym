"""Prepare an APGym-friendly maize APSIM template from APSIM examples."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Iterable


def walk(node: Any) -> Iterable[dict[str, Any]]:
    if not isinstance(node, dict):
        return
    yield node
    children = node.get("Children")
    if isinstance(children, list):
        for child in children:
            yield from walk(child)


def find_first_model(
    payload: dict[str, Any],
    name: str,
    type_contains: str | None = None,
) -> dict[str, Any]:
    for node in walk(payload):
        if str(node.get("Name")) != name:
            continue
        if type_contains and type_contains not in str(node.get("$type", "")):
            continue
        return node
    raise KeyError(f"Could not find model {name!r} ({type_contains or 'any type'})")


def set_manager_param(payload: dict[str, Any], manager_name: str, key: str, value: Any) -> None:
    manager = find_first_model(payload, manager_name, type_contains="Models.Manager")
    params = manager.setdefault("Parameters", [])
    if not isinstance(params, list):
        raise TypeError(f"Manager {manager_name!r} Parameters is not a list")
    for item in params:
        if str(item.get("Key")) == key:
            item["Value"] = str(value)
            return
    params.append({"Key": key, "Value": str(value)})


def ensure_topdress_manager(payload: dict[str, Any]) -> None:
    try:
        manager = find_first_model(payload, "APGym TopDress N", type_contains="Models.Manager")
    except KeyError:
        zone = find_first_model(payload, "Field", type_contains="Models.Core.Zone")
        children = zone.setdefault("Children", [])
        if not isinstance(children, list):
            raise TypeError("Field zone Children is not a list")
        manager = {
            "$type": "Models.Manager, Models",
            "CodeArray": [
                "using Models.Soils;",
                "using System;",
                "using System.Collections.Generic;",
                "using Models.Core;",
                "namespace Models",
                "{",
                "    [Serializable]",
                "    public class Script : Model",
                "    {",
                "        [Link] Clock Clock;",
                "        [Link] Fertiliser Fertiliser;",
                "",
                "        [Description(\"Semicolon list: yyyy-MM-dd:kgNha\")]",
                "        public string ScheduleCsv { get; set; }",
                "",
                "        [Description(\"Fertiliser type\")]",
                "        public Fertiliser.Types FertiliserType { get; set; }",
                "",
                "        private Dictionary<DateTime, double> schedule;",
                "        private HashSet<DateTime> appliedDates = new HashSet<DateTime>();",
                "",
                "        [EventSubscribe(\"Commencing\")]",
                "        private void OnCommencing(object sender, EventArgs e)",
                "        {",
                "            schedule = new Dictionary<DateTime, double>();",
                "            if (string.IsNullOrWhiteSpace(ScheduleCsv))",
                "                return;",
                "",
                "            foreach (string entryRaw in ScheduleCsv.Split(';'))",
                "            {",
                "                string entry = entryRaw.Trim();",
                "                if (entry.Length == 0)",
                "                    continue;",
                "                string[] pieces = entry.Split(':');",
                "                if (pieces.Length != 2)",
                "                    continue;",
                "                if (DateTime.TryParse(pieces[0], out DateTime dt) && double.TryParse(pieces[1], out double amount))",
                "                    schedule[dt.Date] = amount;",
                "            }",
                "        }",
                "",
                "        [EventSubscribe(\"DoManagement\")]",
                "        private void OnDoManagement(object sender, EventArgs e)",
                "        {",
                "            if (schedule == null)",
                "                return;",
                "",
                "            DateTime today = Clock.Today.Date;",
                "            if (schedule.TryGetValue(today, out double amount) && amount > 0 && !appliedDates.Contains(today))",
                "            {",
                "                Fertiliser.Apply(Amount: amount, Type: FertiliserType);",
                "                appliedDates.Add(today);",
                "            }",
                "        }",
                "    }",
                "}",
            ],
            "Parameters": [
                {"Key": "ScheduleCsv", "Value": ""},
                {"Key": "FertiliserType", "Value": "NO3N"},
            ],
            "Name": "APGym TopDress N",
            "ResourceName": None,
            "Children": [],
            "Enabled": True,
            "ReadOnly": False,
        }
        children.append(manager)
    # Always reset to empty schedule during template preparation.
    params = manager.setdefault("Parameters", [])
    if not isinstance(params, list):
        raise TypeError("APGym TopDress N Parameters is not a list")
    keys = {str(p.get("Key")): p for p in params}
    keys.setdefault("ScheduleCsv", {"Key": "ScheduleCsv", "Value": ""})
    keys.setdefault("FertiliserType", {"Key": "FertiliserType", "Value": "NO3N"})
    keys["ScheduleCsv"]["Value"] = ""
    manager["Parameters"] = list(keys.values())


def patch_report(payload: dict[str, Any]) -> None:
    report = find_first_model(payload, "Report", type_contains="Models.Report")
    report["EventNames"] = ["[Clock].DoReport"]
    report["VariableNames"] = [
        "[Clock].Today as Date",
        "[Weather].Rain as Rain",
        "[Maize].Phenology.CurrentStageName as Stage",
        "[Maize].AboveGround.Wt as Biomass",
        "[Maize].Grain.Total.Wt*10 as Yield",
        "[Maize].Grain.Total.Wt as GrainWt",
        "[Maize].Total.Wt as TotalWt",
    ]


def patch_clock(payload: dict[str, Any], start: str, end: str) -> None:
    clock = find_first_model(payload, "Clock", type_contains="Models.Clock")
    clock["Start"] = f"{start}T00:00:00"
    clock["End"] = f"{end}T00:00:00"


def prepare_template(source: Path, target: Path, start: str, end: str) -> None:
    with source.open("r", encoding="utf-8") as handle:
        payload = json.load(handle)
    patch_report(payload)
    set_manager_param(payload, manager_name="Fertilise at sowing", key="Amount", value=0.0)
    ensure_topdress_manager(payload)
    patch_clock(payload, start=start, end=end)
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2)
        handle.write("\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True, help="Source APSIM maize template")
    parser.add_argument("--target", required=True, help="Output APGym template")
    parser.add_argument("--start", default="1990-01-01")
    parser.add_argument("--end", default="1990-12-31")
    args = parser.parse_args()
    prepare_template(
        source=Path(args.source).expanduser().resolve(),
        target=Path(args.target).expanduser().resolve(),
        start=args.start,
        end=args.end,
    )


if __name__ == "__main__":
    main()
