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
| `mirror/downloads/spiralmesh-continuity-local-v0.1.zip` through `v0.6.1` | **Apache-2.0** (`LICENSE`). The carried Constitution 2.0 Core is separately published under **CC0 1.0**; the retained `LICENSE-CONSTITUTION.txt` names the historical v1.8 path, as disclosed in the current quickstart. |
| `mirror/downloads/article11-local-agent-memory-kit.zip` and `article11-local-agent-memory-kit-20260909.zip` | **CC0 1.0 Universal** (`LICENSE`). The dated kit's `THIRD_PARTY_NOTICES.md` preserves the separate terms of externally installed dependencies, models and host adapters. |
| `mirror/fork/article11-fork-kit-v1.0.0.zip` | See the fork documentation alongside it; the constitution content it carries is CC0. |
| `mirror/downloads/article11-constitution-2.0-starter.zip` | **CC0 1.0 Universal** for every included file (`LICENSE`, `NOTICE.md`); names and marks excluded. |

Browser-memory bridge code is Apache-2.0 with the carried Constitution under CC0, as declared in its archive.

## The starter ZIP

The current `article11-constitution-2.0-starter.zip` ships `LICENSE` and `NOTICE.md`.
The publisher dedicates every included file to CC0 1.0: the carried texts and
records, reading aid, start notes, verifier, manifest and carried receipt verifier.
The names and marks remain excluded. The Constitution and Core retain their exact
published bytes, and the mirror verifier checks the complete archive digest.

The earlier starter lacked an explicit wrapper-file licence. The 95,673-byte
upstream re-release closes that gap; earlier snapshots remain in repository
history. This mirror copies the upstream archive unchanged rather than adding
licence terms inside it.

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
