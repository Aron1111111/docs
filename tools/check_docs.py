"""Check local documentation files without accessing the application API."""
from pathlib import Path
from urllib.parse import urlsplit, unquote
import re
import sys

root = Path(__file__).resolve().parents[1]
required = [
    "README.md", ".gitignore", "docs/requirements.md",
    "docs/architecture.md", "docs/user-guide.md", "docs/admin-guide.md",
    "docs/testing.md", "docs/verification.md", "api/bookclub.openapi.yaml",
    "docs/images/components.png", "docs/images/sequence.png",
]
errors = []
count = 0
for name in required:
    if not (root / name).is_file():
        errors.append("Missing required file: " + name)
for page in root.rglob("*.md"):
    if ".git" in page.relative_to(root).parts:
        continue
    for target in re.findall(r"\]\(([^)]+)\)", page.read_text(encoding="utf-8")):
        url = urlsplit(target)
        if url.scheme or url.netloc or not url.path:
            continue
        dest = (page.parent / unquote(url.path)).resolve()
        if not dest.is_relative_to(root):
            errors.append("Path escapes project: " + target)
        elif not dest.is_file():
            errors.append("Missing link target: " + target)
        count += 1
for name in ["components.png", "sequence.png"]:
    path = root / "docs" / "images" / name
    if path.is_file() and path.read_bytes()[:8] != b"\x89PNG\r\n\x1a\n":
        errors.append("Invalid PNG header: " + name)
if errors:
    print("FAIL")
    print("\n".join(errors))
    sys.exit(1)
print(f"PASS: {len(required)} required files; {count} relative file links; 2 PNG headers")
