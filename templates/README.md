# APGym APSIM Templates

`maize_n_base.apsimx` in this folder is a placeholder JSON scaffold for dry-run development only.

Before real APSIM execution, replace it with a validated APSIM Next Gen simulation file and keep (or update) the patch path used by `MaizeNConfig.nitrogen_schedule_patch_path`.

Suggested process:

1. Build and validate a real maize + nitrogen `.apsimx` manually in APSIM UI.
2. Add report tables for daily state and seasonal summary.
3. Confirm CLI run works with `Models.exe`.
4. Point `MaizeNConfig.template_path` at that file.
