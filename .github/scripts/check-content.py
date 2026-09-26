"""Check local Markdown targets and JSON without fetching remote websites."""
from pathlib import Path
import json
import re
import subprocess
from urllib.parse import unquote, urlsplit

root = Path.cwd().resolve()
files = [Path(p) for p in subprocess.check_output(["git", "ls-files", "-z"]).decode().split("\0") if p]
errors = []
for file in files:
    if file.suffix == ".json":
        try:
            json.loads(file.read_text())
        except (ValueError, UnicodeError) as error:
            errors.append(f"{file}: invalid JSON: {error}")
    if file.suffix.lower() != ".md":
        continue
    text = re.sub(r"(?ms)^(```|~~~).*?^\1[^\n]*$", "", file.read_text())
    targets = re.findall(r"!?\[[^\]\n]*\]\((<[^>]+>|[^\s)]+)(?:\s+[^)]*)?\)", text)
    targets += re.findall(r'<(?:img|a)\b[^>]*(?:src|href)=["\']([^"\']+)["\']', text)
    for target in targets:
        target = target.strip("<>")
        parsed = urlsplit(target)
        if parsed.scheme or parsed.netloc or not parsed.path:
            continue
        path = unquote(parsed.path)
        candidate = (root / path.lstrip("/")) if path.startswith("/") else file.parent / path
        if not candidate.exists():
            errors.append(f"{file}: missing local link target {path}")
if errors:
    raise SystemExit("\n".join(errors))
print("Local Markdown targets and JSON are valid.")
