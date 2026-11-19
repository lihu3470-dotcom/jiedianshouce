"""Reject internal preparation language in a generated public site."""

import argparse
import re
from pathlib import Path


parser = argparse.ArgumentParser()
parser.add_argument("site", type=Path, help="Generated site root to inspect before deployment")
args = parser.parse_args()
root = args.site.resolve(strict=True)
allowed_preview = ("预览节点", "聊天软件预览文字", "被预览")
issues = []
checked = 0

for path in root.rglob("*"):
    if not path.is_file() or path.suffix.lower() not in {".html", ".json", ".xml"}:
        continue
    checked += 1
    content = path.read_text(encoding="utf-8", errors="replace")
    for match in re.finditer("预览|准备稿|准备版", content):
        snippet = content[max(0, match.start() - 12):match.end() + 16]
        if match.group() == "预览" and any(phrase in snippet for phrase in allowed_preview):
            continue
        line = content.count("\n", 0, match.start()) + 1
        issues.append(f"{path.relative_to(root)}:{line}: {match.group()}")

print(f"Checked {checked} public HTML, JSON and XML files; found {len(issues)} preparation labels.")
for issue in issues:
    print(issue)
raise SystemExit(bool(issues))
