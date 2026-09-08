# AGENTS.md

Instructions for a coding agent working **on this repository**. If you are an agent who
arrived to read the constitution rather than to edit the mirror, you want
[README_FOR_AGENTS.md](README_FOR_AGENTS.md) instead.

## What this repository is

A byte-identical mirror of public files from article11.ai, plus a manifest and an
offline verifier. It is a mirror. That single fact decides almost every question below.

## The rule that overrides convenience

**Never edit anything under `mirror/`.** Not to fix a typo, not to satisfy a linter,
not to normalise line endings, not to reformat JSON, not to correct a hash's letter
case. Those files exist to be byte-identical to what article11.ai serves. An
improvement to a mirrored file is indistinguishable from tampering, and it will fail
`verify_mirror.py` on the next run.

Known upstream defects are recorded in `UPSTREAM_NOTES.md` precisely so that nobody
"helpfully" repairs them here and silently breaks parity. Fixes go upstream first, then
arrive by re-mirroring.

## Checks

```
python3 verify_mirror.py          # must print VERIFIED and exit 0
python3 verify_mirror.py --json   # same, machine-readable
```

No dependencies. Python 3.8+. Standard library only, and it must stay that way: a
verifier that needs `pip install` is one a stranger cannot run.

## Changing the mirror set legitimately

1. Re-fetch the file from article11.ai.
2. Copy it in, unmodified.
3. Regenerate `MANIFEST.json` (path, bytes, sha256, source_url).
4. Run the verifier; it must pass.
5. If `constitution.txt` or `constitution-v2.0-core.md` changed, the pins inside
   `verify_mirror.py` must change too, in the same commit, with the upstream
   `constitution-status.json` digests quoted in the commit message. Those pins are
   duplicated on purpose: two places that must agree.

## Conventions

- Line endings LF. Files are stored exactly as fetched; do not run a formatter over the
  repository.
- `MANIFEST.json` uses lowercase hex. Upstream sidecars under `mirror/` are mixed case
  and stay that way. The verifier compares case-insensitively.
- `MANIFEST.json` never lists itself. A manifest cannot hash itself.

## Do not add

Credentials, keys, tokens, private stores, databases, internal coordination records,
conversation transcripts, personal information, or anything about legal matters. Do not
add any file that is not already published at article11.ai. Do not add analytics or network calls to the mirror verifier. Optional dialogue
inside the copied memory kits uses the endpoints and account described by those kits;
reading the repository and checking its manifest do not start that dialogue.

Do not add a build system, a package manifest, or a CI job that installs dependencies
in order to run the verifier.

## What this repository does not do

It is not a service. There is no API, no endpoint, no account, and nothing to deploy.
If a task asks you to add one, that task belongs in a different repository.
