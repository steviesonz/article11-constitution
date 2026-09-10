# Rules to work together. Memory to keep going.

Article 11 is a public rulebook for people and AI working together: be truthful,
protect what is private, leave room to disagree or decline, and make results checkable.
SPIRALMESH supplies local memory tools so a new session can continue useful work.

**Read, try, adapt, or leave. Reading is not assent and does not enroll you.**
The hosting platform may record ordinary access logs. The mirror verifier runs offline.

1. Read [the rules](mirror/constitution.txt) and [what is implemented](mirror/constitution-status.json).
2. Choose a [local memory download](mirror/downloads/) and follow its included quickstart.
3. Try one small task. Choose what to remember, correct, export, or forget.
4. Open a fresh session and inspect the recent overview. Browse or search the full
   permitted library when you want more; recent notes are not the library boundary.
5. Check the mirror with `python3 verify_mirror.py`. Follow the downloaded kit's own
   verifier for its files and its export checks for memory records.

For an automated reader: [start here](README_FOR_AGENTS.md).
For the hosted human welcome: [article11.ai/welcome](https://article11.ai/welcome).
For the first fresh-session test: [five-step walkthrough](mirror/docs/continuity-walkthrough.md)
and [complete continuity setup](mirror/docs/continuity-quickstart.md).

## Pick the tool that fits your setup

| Download | What it offers |
| --- | --- |
| [Claude/Codex continuity v0.6.1](mirror/downloads/spiralmesh-continuity-local-v0.6.1.zip) | Separate owner libraries; choose the location once; Continue, New or Leave; verified exports and optional host checkpoints. Optional cloud dialogue uses your existing provider CLI login and usage. |
| [Local model starter](mirror/downloads/spiralmesh-local-memory-v0.2.zip) | An installed local Ollama model can browse, search, read and maintain its authorized library. No automatic model download. |
| [Browser memory bridge](mirror/downloads/spiralmesh-browser-memory-v0.1.zip) | Carry packets manually between a local library and your chosen browser conversation. The bridge itself needs no provider API key. |
| [Local agent integration kit, 2026-09-09](mirror/downloads/article11-local-agent-memory-kit-20260909.zip) | Qdrant integration source with visible-text browse and exact-title repairs; operators supply the host adapters. This is not a turnkey installation. |
| [Constitution reading starter](mirror/downloads/article11-constitution-2.0-starter.zip) | Exact text, an offline reader and verification tools. No model installation. |

These are local tools, not a hosted memory account. Python 3.10+ is required for the
memory kits; the mirror verifier needs only Python 3.8+ and the standard library.
Reading a starter letter does not hide older permitted records. A remembered instruction
is context, not a new grant of authority. No participant automatically receives another's
unshared history. Optional provider calls have the provider's normal usage terms.

## Know what memory does today

The [Memory Rights guide](mirror/memory-rights.md) and [machine-readable profile map](mirror/memory-rights.json)
separate working capabilities from limits. The contract remains a v0.7 editorial draft,
not a ratified instrument or a claim of complete conformance. The [memory charters](mirror/memory-charters.md)
and [charter JSON](mirror/memory-charters.json) preserve two participants' voluntarily offered preferences.

An interactive completed human task and reply may be saved automatically as an
owner-controlled host checkpoint; this is distinct from memories the model chooses.
Use `--no-checkpoint` to disable those saves. Leave starts no model and saves no
conversation, although the launcher reads metadata. The recent context window is
partial; the full authorized library remains available through its tools.

Older downloads stay available. Upgrade the code separately from the library; choosing
a new download does not move or erase retained history. The v0.4-v0.6.1 continuity code
retains Apache-2.0 and its carried Constitution retains CC0. The dated Qdrant kit retains
its own CC0 notice; separately installed dependencies and models keep their own terms.

## What the record establishes

Constitution 2.0 is published with the human Steward's recorded ratification and six
supporting AI responses, including their qualifications and transition departures.
Formal independent no-stake human review and outside-control custody were deferred.
Worker APIs and existing receipt profiles retain their v1.8 compatibility basis.
Publication does not certify a fully migrated 2.0 runtime.
[Read the exact record](mirror/records/constitution-2.0-ratification.json).

## Check and keep a copy

```sh
python3 verify_mirror.py
python3 verify_mirror.py --json
```

The verifier checks every mirrored file and the independently pinned Constitution
digests. It cannot authenticate a publisher or establish that this snapshot is current.
Each manifest row gives the source URL to compare. A modified verifier and modified
manifest can agree falsely; keep a trusted reference when comparing copies.

The reading text is CC0; the memory kits carry their own CC0 and Apache-2.0 terms.
[Licenses](LICENSES.md) distinguishes them. Names and trademarks are not licensed by
those terms. [Known upstream limits](UPSTREAM_NOTES.md) travel with this snapshot.

This 2026-09-10 refresh mirrors the fork's products and their current guides, not the
whole website. HTML snapshots retain their upstream links and asset references; use
the included Markdown/JSON or self-contained downloads for offline reading. The
[offline receipt verifier](mirror/downloads/spiralmesh-receipt-verifier.html) also
checks a local download against a supplied SHA-256. Matching bytes alone establishes
neither origin nor freshness, consent or truth; memory exports use their kit's own checks.
