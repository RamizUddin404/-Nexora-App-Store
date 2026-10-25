#!/usr/bin/env python3
"""Dependency-free static checks for the NEXORA website."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse
import re
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
HTML_FILE = ROOT / "index.html"

class SiteChecker(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = set()
        self.anchors = []
        self.errors = []
        self.title_seen = False
        self.in_title = False
        self.title_text = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        element_id = attrs.get("id")
        if element_id:
            if element_id in self.ids:
                self.errors.append(f"Duplicate static id: {element_id}")
            self.ids.add(element_id)
        if tag == "title":
            self.in_title = True
        for attr in ("href", "src"):
            value = attrs.get(attr)
            if not value:
                continue
            if attr == "href" and value.startswith("#"):
                self.anchors.append(value[1:])
                continue
            if value.startswith(("data:", "mailto:", "tel:", "javascript:")):
                if value.startswith("javascript:"):
                    self.errors.append("javascript: URL is not allowed in markup")
                continue
            parsed = urlparse(value)
            if parsed.scheme or parsed.netloc:
                if parsed.scheme and parsed.scheme not in ("https", "http"):
                    self.errors.append(f"Unexpected URL scheme in {attr}: {value}")
                continue
            target = (ROOT / parsed.path).resolve()
            if not str(target).startswith(str(ROOT.resolve())):
                self.errors.append(f"Unsafe local path: {value}")
            elif parsed.path and not target.exists():
                self.errors.append(f"Missing local asset: {value}")

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False
            self.title_seen = True

    def handle_data(self, data):
        if self.in_title:
            self.title_text.append(data)

def main():
    if not HTML_FILE.exists():
        print("FAIL: index.html is missing")
        return 1
    source = HTML_FILE.read_text(encoding="utf-8")
    checker = SiteChecker()
    checker.feed(source)
    checker.close()
    if '<html lang="en">' not in source and "<html lang='en'>" not in source:
        checker.errors.append("HTML language attribute is missing or not set to en")
    if 'name="viewport"' not in source:
        checker.errors.append("Responsive viewport meta tag is missing")
    if "<main" not in source.lower():
        checker.errors.append("Main landmark is missing")
    if not checker.title_seen or not "".join(checker.title_text).strip():
        checker.errors.append("A non-empty document title is required")
    for anchor in checker.anchors:
        if anchor and anchor not in checker.ids:
            checker.errors.append(f"Broken in-page anchor: #{anchor}")

    scripts = re.findall(r"<script\\b[^>]*>([\\s\\S]*?)</script>", source, re.IGNORECASE)
    if not scripts:
        checker.errors.append("No inline JavaScript block found")
    elif shutil.which("node"):
        for index, script in enumerate(scripts, start=1):
            result = subprocess.run(
                ["node", "--check"],
                input=script,
                text=True,
                capture_output=True,
                cwd=ROOT,
                check=False,
            )
            if result.returncode:
                checker.errors.append(
                    f"JavaScript syntax check failed for script {index}: "
                    f"{(result.stderr or result.stdout).strip()}"
                )
    else:
        print("NOTE: Node.js not installed; JavaScript syntax check skipped.")

    if checker.errors:
        print("NEXORA static site checks failed:")
        for error in checker.errors:
            print(f" - {error}")
        return 1
    print(f"PASS: static HTML checks completed ({len(checker.ids)} unique IDs, {len(checker.anchors)} in-page links checked).")
    return 0

if __name__ == "__main__":
    sys.exit(main())
