#!/usr/bin/env python3
"""Check that every plugin has an explicit semver version, and that any plugin
whose files changed since BASE also bumped its version.

Usage:
  python3 scripts/check_versions.py            # explicit-version check only
  python3 scripts/check_versions.py <base-ref> # also require bumps vs base-ref
"""
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SEMVER = re.compile(r"^\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?$")


def git(*args):
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)


def parse(v):
    core = v.split("+")[0].split("-")[0]
    return tuple(int(x) for x in core.split("."))


def main():
    errors = []
    market = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())

    for entry in market["plugins"]:
        name, source = entry["name"], entry["source"]
        if not isinstance(source, str):
            continue  # plugin lives in another repo; versioned there
        plugin_dir = (ROOT / source).resolve()
        manifest_path = plugin_dir / ".claude-plugin/plugin.json"
        rel_manifest = manifest_path.relative_to(ROOT).as_posix()
        manifest = json.loads(manifest_path.read_text())

        if manifest.get("name") != name:
            errors.append(f"{name}: plugin.json name is {manifest.get('name')!r}; it must match the marketplace entry")
        version = manifest.get("version")
        if not version or not SEMVER.match(str(version)):
            errors.append(f"{name}: plugin.json needs an explicit semver 'version' (found {version!r})")
            continue
        if "version" in entry:
            errors.append(f"{name}: set 'version' only in plugin.json, not in marketplace.json")

        if len(sys.argv) < 2:
            continue
        base = sys.argv[1]
        rel_dir = plugin_dir.relative_to(ROOT).as_posix()
        changed = git("diff", "--name-only", f"{base}...HEAD", "--", rel_dir).stdout.strip()
        if not changed:
            continue
        old = git("show", f"{base}:{rel_manifest}")
        if old.returncode != 0:
            continue  # new plugin
        old_version = json.loads(old.stdout).get("version")
        if not old_version or not SEMVER.match(str(old_version)):
            continue
        if parse(version) <= parse(old_version):
            errors.append(f"{name}: files changed but version is still {version} (was {old_version}); bump it")

    if errors:
        print("Version check failed:")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)
    print("Version check passed.")


if __name__ == "__main__":
    main()
