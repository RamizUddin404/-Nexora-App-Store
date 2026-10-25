#!/usr/bin/env python3
"""Small dependency-free checks for the NEXORA static website."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse
import sys

ROOT = Path(__file__).resolve().parents[1]
HTML_FILE = ROOT / "index.html"

class SiteChecker(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = set()
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
            if not value or value.startswith(("#", "data:", "mailto:", "tel:")):
                continue
            parsed = urlparse(value)
            if parsed.scheme or parsed.netloc:
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
    if checker.errors:
        print("NEXORA static site checks failed:")
        for error in checker.errors:
            print(f" - {error}")
        return 1
    print(f"PASS: static HTML checks completed ({len(checker.ids)} unique IDs checked).")
    return 0

if __name__ == "__main__":
    sys.exit(main())
