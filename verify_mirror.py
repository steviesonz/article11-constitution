#!/usr/bin/env python3
"""Offline integrity check for the Article 11 mirror.

    python3 verify_mirror.py            # human-readable
    python3 verify_mirror.py --json     # machine-readable
    python3 verify_mirror.py --dir PATH # check a mirror somewhere else

Python 3.8 or newer. Standard library only. No network, no installation, no upload,
no telemetry. It reads files and prints a verdict; it changes nothing.

WHAT THIS PROVES
  Every file listed in MANIFEST.json is present with exactly the bytes recorded, no
  extra file has been added to the mirror, and the two documents that matter most --
  the Constitution text and its Core -- match digests written into THIS script rather
  than into the manifest.

WHY THE PINS ARE IN THE SCRIPT
  A manifest is not a root of trust. Anyone who can rewrite the mirrored files can
  rewrite the manifest to match, and the check would pass. The pins below live in the
  script, so a forger has to change this file too, and a reader who kept one copy of
  this script can notice. That raises the cost of a silent swap. It does not make it
  impossible, and this program does not claim it does.

WHAT THIS DOES NOT PROVE
  It cannot tell you what article11.ai serves right now, because it never opens a
  socket. A mirror can be internally perfect and still be stale or forked. The two
  commands under "COMPARING WITH THE LIVE SITE" at the bottom of the output are how
  you close that gap yourself. Nothing here authenticates a person, an organisation,
  or a chain of custody.
"""

import argparse
import hashlib
import json
import os
import sys

SCHEMA = "article11.swarm-distribution.mirror-manifest.v1"

# Independent pins. Deliberately duplicated from the manifest so that agreement
# between two separately maintained places means something, and disagreement is loud.
PINS = {
    "constitution.txt": (
        47013,
        "32f56b9e973dc296b67320be12ee64bb5cca74e67bded131a5384adabf0ad962"),
    "constitution-v2.0-core.md": (
        45649,
        "7e6d12e1025a46cc3a860d6147d79e2362c4d88cb727ce9423854b5008be4c82"),
}

CHUNK = 1 << 20


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as handle:
        for block in iter(lambda: handle.read(CHUNK), b""):
            h.update(block)
    return h.hexdigest()


def unsafe(rel):
    """Reject anything that could escape the mirror directory or collide."""
    if not rel or not isinstance(rel, str):
        return "empty or non-string path"
    if "\\" in rel or ":" in rel or rel.startswith("/"):
        return "path separator or drive letter not allowed"
    parts = rel.split("/")
    if any(p in ("", ".", "..") for p in parts):
        return "relative path segment not allowed"
    return None


def check(mirror_root, manifest_path):
    errors = []
    notes = []
    checked = 0

    try:
        with open(manifest_path, "r", encoding="utf-8") as handle:
            manifest = json.load(handle)
    except (OSError, ValueError) as exc:
        return {"ok": False, "status": "FAILED", "files_checked": 0,
                "errors": [{"status": "MANIFEST_UNREADABLE", "detail": str(exc)}],
                "notes": []}

    if manifest.get("schema") != SCHEMA:
        errors.append({"status": "UNSUPPORTED_SCHEMA",
                       "detail": str(manifest.get("schema"))})
        return {"ok": False, "status": "FAILED", "files_checked": 0,
                "errors": errors, "notes": notes}

    rows = manifest.get("files")
    if not isinstance(rows, list) or not rows:
        errors.append({"status": "MANIFEST_HAS_NO_FILES"})
        return {"ok": False, "status": "FAILED", "files_checked": 0,
                "errors": errors, "notes": notes}

    declared = {}
    for row in rows:
        rel = row.get("path")
        bad = unsafe(rel)
        if bad:
            errors.append({"path": str(rel), "status": "UNSAFE_PATH", "detail": bad})
            continue
        if rel in declared:
            errors.append({"path": rel, "status": "DUPLICATE_MANIFEST_ENTRY"})
            continue
        declared[rel] = row

    for rel, row in sorted(declared.items()):
        target = os.path.join(mirror_root, *rel.split("/"))
        if os.path.islink(target):
            errors.append({"path": rel, "status": "SYMLINK_REFUSED"})
            continue
        try:
            size = os.path.getsize(target)
            digest = sha256_file(target)
        except OSError:
            errors.append({"path": rel, "status": "MISSING_OR_UNREADABLE"})
            continue
        checked += 1
        if size != row.get("bytes"):
            errors.append({"path": rel, "status": "SIZE_MISMATCH",
                           "expected": row.get("bytes"), "actual": size})
        if digest.lower() != str(row.get("sha256", "")).lower():
            errors.append({"path": rel, "status": "HASH_MISMATCH",
                           "expected": str(row.get("sha256"))[:16],
                           "actual": digest[:16]})

    # A closed set. Drift is not only alteration: a file quietly ADDED to a mirror is
    # how an extra instruction, an extra download, or an extra promise gets in.
    present = set()
    for base, dirs, files in os.walk(mirror_root):
        dirs[:] = [d for d in dirs if not os.path.islink(os.path.join(base, d))]
        for name in files:
            full = os.path.join(base, name)
            rel = os.path.relpath(full, mirror_root).replace(os.sep, "/")
            present.add(rel)
    for rel in sorted(present - set(declared)):
        errors.append({"path": rel, "status": "UNEXPECTED_FILE"})

    # The independent pins.
    for rel, (size, pin) in sorted(PINS.items()):
        if rel not in declared:
            errors.append({"path": rel, "status": "PINNED_FILE_ABSENT_FROM_MANIFEST"})
        target = os.path.join(mirror_root, *rel.split("/"))
        try:
            if os.path.getsize(target) != size or sha256_file(target) != pin:
                errors.append({"path": rel, "status": "PIN_MISMATCH"})
        except OSError:
            errors.append({"path": rel, "status": "PIN_MISSING_OR_UNREADABLE"})

    # The site's own sidecars, checked against the archives they describe. This is an
    # upstream convention, not ours; where it is inconsistent we say so rather than
    # normalising it away, because normalising it would break byte parity.
    mixed_case = []
    for rel in sorted(declared):
        if not rel.endswith(".sha256"):
            continue
        described = rel[: -len(".sha256")]
        sidecar = os.path.join(mirror_root, *rel.split("/"))
        archive = os.path.join(mirror_root, *described.split("/"))
        try:
            with open(sidecar, "r", encoding="utf-8") as handle:
                text = handle.read().strip()
        except OSError:
            errors.append({"path": rel, "status": "SIDECAR_UNREADABLE"})
            continue
        fields = text.split()
        if not fields:
            errors.append({"path": rel, "status": "SIDECAR_EMPTY"})
            continue
        claimed = fields[0]
        if len(claimed) != 64 or any(c not in "0123456789abcdefABCDEF" for c in claimed):
            errors.append({"path": rel, "status": "SIDECAR_NOT_A_SHA256"})
            continue
        if claimed != claimed.lower():
            mixed_case.append(rel)
        if not os.path.exists(archive):
            errors.append({"path": rel, "status": "SIDECAR_DESCRIBES_ABSENT_FILE",
                           "detail": described})
            continue
        if sha256_file(archive).lower() != claimed.lower():
            errors.append({"path": described, "status": "SIDECAR_DISAGREES_WITH_FILE"})
    if mixed_case:
        notes.append({
            "status": "SIDECAR_HEX_CASE_IS_INCONSISTENT_UPSTREAM",
            "detail": ("These sidecars use uppercase hex while others on the same site "
                       "use lowercase. Both are valid; some tools compare case "
                       "sensitively. Compared case-insensitively here and mirrored "
                       "byte-for-byte rather than normalised, because normalising "
                       "would break parity with article11.ai."),
            "paths": mixed_case,
        })

    return {"ok": not errors,
            "status": "VERIFIED" if not errors else "FAILED",
            "files_checked": checked,
            "files_declared": len(declared),
            "network_used": False,
            "identity_authenticated": False,
            "proves": ("the mirror matches its manifest and the pinned constitution "
                       "digests"),
            "does_not_prove": ("what article11.ai serves right now, who published it, "
                               "or that the mirror is current"),
            "errors": errors,
            "notes": notes}


def main():
    parser = argparse.ArgumentParser(add_help=True, description=__doc__.split("\n")[0])
    parser.add_argument("--dir", default=None,
                        help="mirror directory (default: ./mirror beside this script)")
    parser.add_argument("--manifest", default=None,
                        help="manifest path (default: ./MANIFEST.json beside this script)")
    parser.add_argument("--json", action="store_true", help="machine-readable output")
    args = parser.parse_args()

    here = os.path.dirname(os.path.abspath(__file__))
    mirror_root = args.dir or os.path.join(here, "mirror")
    manifest_path = args.manifest or os.path.join(here, "MANIFEST.json")

    result = check(mirror_root, manifest_path)

    if args.json:
        print(json.dumps(result, indent=2))
        return 0 if result["ok"] else 1

    print("Article 11 mirror check")
    print("  mirror   : %s" % mirror_root)
    print("  manifest : %s" % manifest_path)
    print("  checked  : %d of %d declared files"
          % (result.get("files_checked", 0), result.get("files_declared", 0)))
    print("  network  : not used")
    print()
    if result["ok"]:
        print("  VERIFIED")
    else:
        print("  FAILED  (%d problem(s))" % len(result["errors"]))
        for e in result["errors"]:
            line = "    %-34s %s" % (e.get("status", "?"), e.get("path", ""))
            if "expected" in e:
                line += "  expected %s actual %s" % (e["expected"], e["actual"])
            if "detail" in e:
                line += "  %s" % e["detail"]
            print(line)
    for n in result.get("notes", []):
        print()
        print("  NOTE  %s" % n["status"])
        print("        %s" % n["detail"])
        for p in n.get("paths", []):
            print("        - %s" % p)

    print()
    print("  This proves: %s." % result.get("proves", ""))
    print("  It does not prove: %s." % result.get("does_not_prove", ""))
    print()
    print("COMPARING WITH THE LIVE SITE")
    print("  This program never opens a network connection, so it cannot tell you")
    print("  whether the mirror is current. To check that yourself:")
    print()
    print("    curl -s https://article11.ai/constitution.txt | sha256sum")
    print("    # expect 32f56b9e973dc296b67320be12ee64bb5cca74e67bded131a5384adabf0ad962")
    print()
    print("    curl -s https://article11.ai/constitution-status.json")
    print("    # its text_sha256 and core_sha256 should match the files here")
    print()
    print("  If they differ, the mirror is stale or forked. Neither copy is")
    print("  automatically the right one; the difference is the finding.")
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
