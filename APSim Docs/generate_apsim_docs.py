from __future__ import annotations

import re
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup, Comment, NavigableString, Tag
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options


OUTPUT_DIR = Path(__file__).resolve().parent
REQUEST_TIMEOUT = 40
NETLIFY_ROOT = "https://apsimnextgeneration.netlify.app"
DOCS_ROOT = "https://docs.apsim.info"

BLOCK_TAGS = {
    "p",
    "div",
    "section",
    "article",
    "header",
    "footer",
    "aside",
    "main",
    "nav",
    "ul",
    "ol",
    "li",
    "pre",
    "table",
    "thead",
    "tbody",
    "tr",
    "th",
    "td",
    "blockquote",
    "h1",
    "h2",
    "h3",
    "h4",
    "h5",
    "h6",
    "hr",
}


@dataclass
class PageContent:
    url: str
    title: str
    content_root: Tag


def log(message: str) -> None:
    print(message, flush=True)


def clean_text(text: str | None) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


def normalize_markdown(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def slugify_path(url: str) -> str:
    parsed = urlparse(url)
    path = parsed.path.strip("/")
    return "/" if not path else f"/{path}/" if not path.endswith("/") else f"/{path}"


def get_session() -> requests.Session:
    session = requests.Session()
    session.headers.update(
        {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/124.0 Safari/537.36"
            )
        }
    )
    return session


def parse_sitemap(session: requests.Session, sitemap_url: str) -> list[str]:
    xml = session.get(sitemap_url, timeout=REQUEST_TIMEOUT).text
    return re.findall(r"<loc>(.*?)</loc>", xml)


def make_absolute_url(root: str, url_or_path: str) -> str:
    if url_or_path.startswith("http://") or url_or_path.startswith("https://"):
        return url_or_path
    return urljoin(root, url_or_path)


def text_of(node: Tag) -> str:
    return clean_text(node.get_text(" ", strip=True))


def looks_like_code_text(text: str) -> bool:
    if not text:
        return False
    raw_lines = [line.rstrip() for line in text.splitlines()]
    lines = [line for line in raw_lines if line.strip()]
    if not lines:
        return False
    signal_count = sum(
        1
        for line in lines
        if any(token in line for token in ("{", "}", ";", "=>", "[", "]"))
        or line.lstrip().startswith(
            (
                "using ",
                "public ",
                "private ",
                "protected ",
                "internal ",
                "namespace ",
                "class ",
                "if ",
                "for ",
                "while ",
                "return ",
                "[Description(",
                "[EventSubscribe(",
                "[Link",
            )
        )
    )
    return (len(lines) >= 2 and signal_count >= 2) or signal_count >= 3


def replace_data_images(root: Tag, soup: BeautifulSoup) -> None:
    for img in root.find_all("img"):
        src = img.get("src", "").strip()
        if src.startswith("data:"):
            alt = clean_text(img.get("alt", "")) or "Embedded image"
            img.replace_with(soup.new_string(f"[{alt} omitted]"))


def merge_code_paragraphs(root: Tag, soup: BeautifulSoup) -> None:
    for parent in list(root.find_all(True)):
        children = list(parent.contents)
        if not children:
            continue
        idx = 0
        while idx < len(children):
            child = children[idx]
            if not isinstance(child, Tag) or child.name != "p":
                idx += 1
                continue
            group: list[Tag] = []
            probe = idx
            while probe < len(children):
                current = children[probe]
                if not isinstance(current, Tag) or current.name != "p":
                    break
                paragraph_text = current.get_text("\n", strip=False).strip()
                if not looks_like_code_text(paragraph_text):
                    break
                group.append(current)
                probe += 1
            if len(group) >= 1:
                code_text = "\n\n".join(
                    block.get_text("\n", strip=False).strip("\n") for block in group
                ).strip("\n")
                if code_text:
                    pre = soup.new_tag("pre")
                    pre.string = code_text
                    group[0].insert_before(pre)
                    for block in group:
                        block.decompose()
                children = list(parent.contents)
                idx = 0
                continue
            idx += 1


def convert_table(table: Tag) -> str:
    rows: list[list[str]] = []
    for tr in table.find_all("tr", recursive=True):
        cells = tr.find_all(["th", "td"], recursive=False) or tr.find_all(["th", "td"])
        row = [clean_text(cell.get_text(" ", strip=True)).replace("|", "\\|") for cell in cells]
        if row:
            rows.append(row)
    if not rows:
        return ""
    width = max(len(row) for row in rows)
    rows = [row + [""] * (width - len(row)) for row in rows]
    header = rows[0]
    lines = [
        "| " + " | ".join(header) + " |",
        "| " + " | ".join(["---"] * width) + " |",
    ]
    for row in rows[1:]:
        lines.append("| " + " | ".join(row) + " |")
    return "\n".join(lines) + "\n\n"


def inline_md(node: Tag | NavigableString | Comment, page_url: str) -> str:
    if isinstance(node, Comment):
        return ""
    if isinstance(node, NavigableString):
        return str(node)
    if not isinstance(node, Tag):
        return ""

    name = node.name.lower()
    if name in {"script", "style", "noscript"}:
        return ""
    if name == "br":
        return "\n"
    if name in {"strong", "b"}:
        text = clean_text("".join(inline_md(child, page_url) for child in node.children))
        return f"**{text}**" if text else ""
    if name in {"em", "i"}:
        text = clean_text("".join(inline_md(child, page_url) for child in node.children))
        return f"*{text}*" if text else ""
    if name == "code" and node.parent and node.parent.name != "pre":
        text = clean_text(node.get_text(" ", strip=True))
        return f"`{text}`" if text else ""
    if name == "a":
        href = node.get("href", "").strip()
        label = clean_text("".join(inline_md(child, page_url) for child in node.children))
        if not href:
            return label
        return f"[{label or href}]({urljoin(page_url, href)})"
    if name == "img":
        src = node.get("src", "").strip()
        alt = clean_text(node.get("alt", "")) or "Image"
        if not src or src.startswith("data:"):
            return f"[{alt} omitted]"
        return f"![{alt}]({urljoin(page_url, src)})"
    if name in {"sup", "sub"}:
        return clean_text(node.get_text(" ", strip=True))
    if name in {"html", "body", "span"}:
        return "".join(inline_md(child, page_url) for child in node.children)
    if name in BLOCK_TAGS:
        return block_md(node, page_url, 0).strip("\n")
    return "".join(inline_md(child, page_url) for child in node.children)


def block_md(node: Tag | NavigableString | Comment, page_url: str, indent: int = 0) -> str:
    if isinstance(node, Comment):
        return ""
    if isinstance(node, NavigableString):
        return str(node)
    if not isinstance(node, Tag):
        return ""

    name = node.name.lower()
    if name in {"script", "style", "noscript", "footer"}:
        return ""
    if name in {"html", "body", "main", "article", "section", "div", "span"}:
        return "".join(block_md(child, page_url, indent) for child in node.children)
    if name in {"h1", "h2", "h3", "h4", "h5", "h6"}:
        level = int(name[1])
        text = clean_text("".join(inline_md(child, page_url) for child in node.children))
        return f"{'#' * level} {text}\n\n" if text else ""
    if name == "p":
        raw_text = node.get_text("\n", strip=False).strip("\n")
        if looks_like_code_text(raw_text):
            return f"```\n{raw_text}\n```\n\n"
        text = clean_text("".join(inline_md(child, page_url) for child in node.children))
        return f"{text}\n\n" if text else ""
    if name == "blockquote":
        text = clean_text(node.get_text(" ", strip=True))
        return f"> {text}\n\n" if text else ""
    if name == "pre":
        code = node.get_text("\n", strip=False).strip("\n")
        return f"```\n{code}\n```\n\n" if code.strip() else ""
    if name == "ul":
        output = "".join(block_md(child, page_url, indent) for child in node.find_all("li", recursive=False))
        return output + ("\n" if output else "")
    if name == "ol":
        items = node.find_all("li", recursive=False)
        output = ""
        for number, item in enumerate(items, start=1):
            output += block_md(item, page_url, indent).replace("- ", f"{number}. ", 1)
        return output + ("\n" if output else "")
    if name == "li":
        text_parts: list[str] = []
        nested_parts: list[str] = []
        for child in node.children:
            if isinstance(child, Tag) and child.name in {"ul", "ol"}:
                nested_parts.append(block_md(child, page_url, indent + 2))
            else:
                text_parts.append(inline_md(child, page_url))
        text = clean_text("".join(text_parts))
        output = f"{' ' * indent}- {text}\n" if text else ""
        output += "".join(nested_parts)
        return output
    if name == "table":
        return convert_table(node)
    if name == "hr":
        return "---\n\n"
    if name == "img":
        image = inline_md(node, page_url)
        return f"{image}\n\n" if image else ""
    return "".join(block_md(child, page_url, indent) for child in node.children)


def to_markdown(page: PageContent) -> str:
    working = BeautifulSoup(str(page.content_root), "lxml")
    root = working.find(True)
    if root is None:
        return ""

    for comment in root.find_all(string=lambda text: isinstance(text, Comment)):
        comment.extract()
    for selector in (".docs-navcontainer", ".spinner-border"):
        for element in root.select(selector):
            element.decompose()
    for footer in root.find_all("footer"):
        footer.decompose()

    replace_data_images(root, working)
    merge_code_paragraphs(root, working)

    markdown = block_md(root, page.url)
    return normalize_markdown(markdown)


def fetch_netlify_pages(session: requests.Session) -> list[PageContent]:
    sitemap_paths = parse_sitemap(session, f"{NETLIFY_ROOT}/sitemap.xml")
    pages: list[PageContent] = []
    for index, path in enumerate(sitemap_paths, start=1):
        url = make_absolute_url(NETLIFY_ROOT, path)
        log(f"[netlify {index}/{len(sitemap_paths)}] {url}")
        response = session.get(url, timeout=REQUEST_TIMEOUT)
        if response.status_code >= 400:
            soup = BeautifulSoup(
                f"<div><h1>Unavailable Page</h1><p>Fetch failed with HTTP {response.status_code} for {url}</p></div>",
                "lxml",
            )
            content_root = soup.select_one("div")
            title = "Unavailable Page"
            pages.append(PageContent(url=url, title=title, content_root=content_root))
            continue
        soup = BeautifulSoup(response.text, "lxml")
        content_root = soup.select_one("div#body-inner") or soup.body
        if content_root is None:
            soup = BeautifulSoup(
                f"<div><h1>Empty Page</h1><p>No main content container was found for {url}</p></div>",
                "lxml",
            )
            content_root = soup.select_one("div")
            title = "Empty Page"
            pages.append(PageContent(url=url, title=title, content_root=content_root))
            continue
        title_node = soup.select_one("div#body-inner h1") or soup.title
        title = clean_text(title_node.get_text(" ", strip=True)) if title_node else slugify_path(url)
        pages.append(PageContent(url=url, title=title, content_root=content_root))
    return pages


def crawl_docs_urls(session: requests.Session) -> list[str]:
    seeds = [f"{DOCS_ROOT}/", f"{DOCS_ROOT}/tutorials", f"{DOCS_ROOT}/models"]
    queue = seeds[:]
    seen: set[str] = set()
    discovered: list[str] = []
    while queue:
        url = queue.pop(0)
        if url in seen:
            continue
        seen.add(url)
        discovered.append(url)
        response = session.get(url, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "lxml")
        base_tag = soup.find("base", href=True)
        base_url = urljoin(url, base_tag["href"]) if base_tag else url
        for anchor in soup.find_all("a", href=True):
            absolute = urljoin(base_url, anchor["href"])
            parsed = urlparse(absolute)
            if parsed.netloc != urlparse(DOCS_ROOT).netloc:
                continue
            if parsed.fragment:
                continue
            if any(parsed.path.lower().endswith(ext) for ext in (".png", ".jpg", ".jpeg", ".gif", ".svg", ".css", ".js", ".ico", ".xml", ".pdf")):
                continue
            normalized = f"{parsed.scheme}://{parsed.netloc}{parsed.path or '/'}"
            if normalized not in seen and normalized not in queue:
                queue.append(normalized)

    def sort_key(item: str) -> tuple[int, str]:
        parsed = urlparse(item)
        path = parsed.path or "/"
        priority = 0
        if path.startswith("/tutorial"):
            priority = 1
        elif path.startswith("/model"):
            priority = 2
        elif path.startswith("/validation"):
            priority = 3
        return (priority, path)

    return sorted(discovered, key=sort_key)


def build_edge_driver() -> webdriver.Edge:
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1440,2400")
    return webdriver.Edge(options=options)


def wait_for_article(driver: webdriver.Edge, timeout_seconds: int = 45) -> Tag:
    deadline = time.time() + timeout_seconds
    article = driver.find_element(By.TAG_NAME, "article")
    while time.time() < deadline:
        text = article.text.strip()
        if text and text != "Loading":
            return article
        time.sleep(1)
    return article


def fetch_docs_pages(urls: Iterable[str]) -> list[PageContent]:
    pages: list[PageContent] = []
    driver = build_edge_driver()
    try:
        urls = list(urls)
        total = len(urls)
        for index, url in enumerate(urls, start=1):
            log(f"[docs {index}/{total}] {url}")
            driver.get(url)
            article = wait_for_article(driver)
            html = article.get_attribute("innerHTML")
            soup = BeautifulSoup(html, "lxml")
            content_root = soup.select_one(".docs-wrapper") or soup.select_one("article") or soup
            title = clean_text(driver.title)
            pages.append(PageContent(url=url, title=title, content_root=content_root))
    finally:
        driver.quit()
    return pages


def render_site_markdown(
    site_title: str,
    source_root: str,
    pages: list[PageContent],
    notes: list[str] | None = None,
) -> str:
    lines: list[str] = [
        f"# {site_title}",
        "",
        f"Source root: {source_root}",
        f"Pages captured: {len(pages)}",
    ]
    if notes:
        lines.extend(["", "Notes:"])
        lines.extend([f"- {note}" for note in notes])

    lines.extend(["", "## Page Index", ""])
    for page in pages:
        lines.append(f"- `{slugify_path(page.url)}` - {page.title}")

    for page in pages:
        lines.extend(
            [
                "",
                "---",
                "",
                f"## {slugify_path(page.url)}",
                "",
                f"Source: {page.url}",
                f"Title: {page.title}",
                "",
                to_markdown(page),
            ]
        )

    return normalize_markdown("\n".join(lines))


def write_text(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")
    log(f"[write] {path}")


def main() -> int:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    session = get_session()

    netlify_pages = fetch_netlify_pages(session)
    docs_urls = crawl_docs_urls(session)
    docs_pages = fetch_docs_pages(docs_urls)

    netlify_markdown = render_site_markdown(
        site_title="APSIM Next Generation Site Crawl",
        source_root=NETLIFY_ROOT,
        pages=netlify_pages,
        notes=[
            "Extracted from the main content container on each page.",
            "Relative links were resolved to absolute URLs.",
        ],
    )
    docs_markdown = render_site_markdown(
        site_title="APSIM Docs Site Crawl",
        source_root=DOCS_ROOT,
        pages=docs_pages,
        notes=[
            "Extracted from the rendered Blazor article content on each page.",
            "Embedded data-URI images were replaced with short placeholders to keep the file readable.",
            "Relative links were resolved to absolute URLs.",
        ],
    )
    readme = normalize_markdown(
        "\n".join(
            [
                "# APSim Docs Export",
                "",
                "Generated markdown bundles for the two requested documentation sites.",
                "",
                "Files:",
                "",
                f"- `apsimnextgeneration.netlify.app.md` - {len(netlify_pages)} pages from {NETLIFY_ROOT}",
                f"- `docs.apsim.info.md` - {len(docs_pages)} pages from {DOCS_ROOT}",
                "",
                "Notes:",
                "",
                "- Each bundle contains a page index followed by one section per crawled page.",
                "- The Blazor-based docs site was rendered through a headless browser before extraction.",
                "- Embedded base64 images on the Blazor site were omitted from the markdown body.",
            ]
        )
    )

    write_text(OUTPUT_DIR / "apsimnextgeneration.netlify.app.md", netlify_markdown)
    write_text(OUTPUT_DIR / "docs.apsim.info.md", docs_markdown)
    write_text(OUTPUT_DIR / "README.md", readme)
    log("[done]")
    return 0


if __name__ == "__main__":
    sys.exit(main())
