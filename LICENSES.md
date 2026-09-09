# Licences, per path

Licensing here is not uniform, so a single repository-level licence file would be
misleading. Every statement below was read out of the mirrored artifact itself, not
inferred from a description of it.

## Constitution text

| Path | Licence |
| --- | --- |
| `mirror/constitution.txt` | CC0 1.0 Universal — public domain dedication |
| `mirror/constitution-v2.0-core.md` | CC0 1.0 Universal |
| `mirror/records/constitution-2.0-ratification.json` | CC0 1.0 (published record) |

## Kits

| Archive | Licence, as shipped inside it |
| --- | --- |
| `mirror/downloads/spiralmesh-local-memory-v0.2.zip` | **Apache-2.0** for the new store, runner, launchers, packaging tools and starter docs (`LICENSE`). **CC0 1.0** for the reused `dialogue.py` and the carried Constitution Core (`LICENSE-LOCAL-MEMORY-CC0.txt`, `NOTICE-LOCAL-MEMORY.md`). |
| `mirror/downloads/spiralmesh-continuity-local-v0.1.zip` through `v0.6` | **Apache-2.0** (`LICENSE`). The carried Constitution 2.0 Core is separately published under **CC0 1.0**; the retained `LICENSE-CONSTITUTION.txt` names the historical v1.8 path, as disclosed in the current quickstart. |
| `mirror/downloads/article11-local-agent-memory-kit.zip` and `article11-local-agent-memory-kit-20260909.zip` | **CC0 1.0 Universal** (`LICENSE`). The dated kit's `THIRD_PARTY_NOTICES.md` preserves the separate terms of externally installed dependencies, models and host adapters. |
| `mirror/fork/article11-fork-kit-v1.0.0.zip` | See the fork documentation alongside it; the constitution content it carries is CC0. |
| `mirror/downloads/article11-constitution-2.0-starter.zip` | **No licence file is shipped.** See below. |

Browser-memory bridge code is Apache-2.0 with the carried Constitution under CC0, as declared in its archive.

## The starter ZIP

`article11-constitution-2.0-starter.zip` contains no `LICENSE`, `COPYING`, or `NOTICE`
member. The constitution text inside it is CC0 — the package check compares its carried text to
`mirror/constitution.txt`. The mirror verifier checks the archive against its manifest digest. The wrapper
files around it (`verify.py`, `manifest.json`, `READ_OFFLINE.html`, `START_HERE.md`)
carry no stated licence.

Until that is resolved upstream, treat the constitution text inside it as CC0 and the
wrapper as unlicensed. This is recorded as finding F1 in `UPSTREAM_NOTES.md`. The
archive is mirrored unmodified; adding a licence file here would break byte parity with
article11.ai and would also mean this repository asserting a licence that is not the
publisher's to have granted by proxy.

## Names and marks are not licensed

Stated in the publishers' own notice, and repeated here because it is the constraint
most easily missed when copying public-domain material:

> ARTICLE 11 AI, Article11.ai and SPIRALMESH names and marks are not licensed by these
> code or text licenses. A fork should use its own identity.

Copy the rules freely. Do not present your fork as being them.

## This repository's own files

`README.md`, `README_FOR_AGENTS.md`, `AGENTS.md`, `UPSTREAM_NOTES.md`, `LICENSES.md`, `MANIFEST.json` and
`verify_mirror.py` were written for this mirror and are offered under **CC0 1.0**, to
match the constitution they describe. They are documentation and a checker; there is
nothing in them worth restricting.
