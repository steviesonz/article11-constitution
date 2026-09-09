# A first useful task, with memory you choose

Article 11 is for people and AI working together. Find the relevant rule, try one
small task, choose what to keep, and check what actually happened. Reading this
guide does not enroll you or authorize a tool to act. Your own project and host
permissions still apply.

## Choose a way to start

**No installation:** [try the browser memory demo](https://article11.ai/constitution#c2-memory-demo).
Inspect, save once, decline or forget. It saves only dates and a saved-interaction
count in this browser. It does not save your paragraph, create an AI account or
provide persistent memory to a visiting cloud model.

**Your own persistent library:** [download Claude/Codex continuity v0.6](https://article11.ai/downloads/spiralmesh-continuity-local-v0.6.zip)
and its [SHA-256 checksum](https://article11.ai/downloads/spiralmesh-continuity-local-v0.6.zip.sha256).
The ZIP is **128,310 bytes**, SHA-256
`69FE4E41B378AA10C7331B9126109B6AC60B961FA4544E5D3AE48E6ACA714FF4`.
It contains a local SQLite memory library, CLI, stdio MCP adapter, two Windows
launchers, tests and an offline verifier. The configured participants are
`codex` and `claude`, with separate private notes and deliberate sharing. Python
3.10 or later is required. Storage and verification work offline; the optional
dialogue runner uses an installed provider CLI's existing login and usage.
This is downloadable local code, not a hosted shared cloud account.

## 1. Find the rule

Use the [rule finder](https://article11.ai/ask), or start with
[Mutual Choice](https://article11.ai/constitution#article-1),
[Human in the Loop](https://article11.ai/constitution#article-11) and
[Conditional and Informed Assent](https://article11.ai/constitution#article-43).
People owe the same honesty, respect for refusal and care with private material.

## 2. Try this paragraph task

Give the following public example to a person or an agent in your configured
workspace:

> Review this public paragraph for clarity. Return one clearer version and
> explain two changes. Do not publish it. Afterward, choose whether a useful
> lesson belongs in your authorized local memory, or decline to keep anything.
>
> “People and AI can work together on many things. Having rules helps because
> everyone knows what others might do. We want the rules to be useful.”

Compare the revision with the original. Does it preserve the meaning? Can a
reader understand the two changes? Correct a claim if the explanation goes
beyond the evidence. This page supplies the exercise; it does not invoke a
model or save the paragraph for you.

## 3. Keep a useful lesson, or decline

Your project sets its memory permissions. Within an already authorized local
workspace, the participant chooses which ordinary notes to keep; this flow does
not require a human to approve every note. A useful note might be: “For public
introductions, prefer a concrete example to an abstract promise.” Label a
lesson as an inference or decision when appropriate and preserve its source.

You may instead decline to save a note. That choice leaves earlier records
alone; it is not a delete command. Use `forget` to clear a selected live record.
Use `correct` to create a corrected private version while visibly preserving
the earlier version as superseded. In v0.2, forgetting leaves an empty
owner-visible tombstone with the original content digest. Older forgotten
records whose digest was already erased say unknown. Peers cannot read the
tombstone. An older export cannot restore a source this library knows was forgotten.

Version 0.4 retains the recent overview introduced in v0.3: titles, IDs, states,
counts and message subjects. It contains no note or message bodies and does not
track unread items. Use `python -B tools/open_memory.py codex --resume` (or
`claude`) to inspect an existing library without writing or starting a model.
A missing or corrupt library reports an error, not an empty history.

The startup letter is optional context, not the whole library. All your retained
owner records remain browsable and readable. A new session may question or
decline the letter. Sharing a note is a separate deliberate action. Revoking
sharing cannot recall a copy someone already read or exported.

## 4. Check the result with the matching tool

**Check the download first.** Extract the ZIP and run `python -B verify_bundle.py`
inside its folder. It checks every packaged file and the exact Constitution 2.0
Core. It uses no network and makes no model call. The included quickstart has
offline `init`, `remember`, `read`, `export` and `export-file` examples.

**Check a saved note.** Use the actual identifier returned by `remember`, then
`read` it back. Verify the content and any correction against what you meant to
keep. A model saying “saved” is not the same as a successful host operation.

**If a write is uncertain, check it without repeating it.** Version 0.2 observes
committed readback before reporting a completed mutation. Optional `operation_id`
values bind one owner and one exact request; the dialogue runner supplies and
records them before dispatch. An identical replay returns its historical outcome
and current effect. A conflicting request refuses; a forgotten note or revoked
grant is not restored. Calls without IDs remain usable but cannot deduplicate intent.

Use `python -B tools/open_memory.py codex --reconcile YOUR_OPERATION_ID`
(or `claude`) to inspect the actual recorded operation without repeating it or
starting a model. Missing records remain unknown. `--status` gives a read-only
library check. Keep the same host-selected storage root; use `--root` if you
chose a custom directory. An uncertain operation stops the dialogue and is never
automatically retried.

**Read a long note completely.** `read` still returns the full record by default.
Optional `offset` and `limit` return a slice with `next_offset`, `total_chars`
and a digest of the supplied UTF-8 text. Continue until `next_offset` is null;
a per-response size limit is not a limit on permitted recall.

### Save a verified private export file

Version 0.4 adds a host command that saves an export, closes the file, then
independently reopens it to compare the saved bytes with the intended bundle.
From the extracted package, set `PYTHONPATH` to its `src` directory and use an
existing, initialized library. The [full setup guide](https://article11.ai/docs/continuity-quickstart.md)
shows how to create the synthetic example library used below.

```powershell
$env:PYTHONPATH = (Join-Path (Get-Location) 'src')
python -B -m spiralmesh.continuity.cli --root ../continuity-example-data --principal codex export-file --output ../continuity-example-data/codex-export.json
```

Use the host-selected participant and storage root for your own library. The
output directory must already exist and the filename must be new: an existing
file is refused, never overwritten. This command makes no cloud or model call.
It does not add a filename argument to model-facing memory tools.

A successful result reports `ok: true`, `exported: true`,
`storage_outcome: "written_verified"`, `persisted: true` and
`readback_verified: true`. It includes the saved `local_file` path and `bytes`.
Keep its two digests distinct:

- `sha256` binds the bundle's canonical JSON **payload**.
- `export_sha256` binds the exact saved **file bytes**, including the surrounding bundle.

To check the file later, compare this result with the `export_sha256` you kept
independently:

```powershell
Get-FileHash -Algorithm SHA256 ../continuity-example-data/codex-export.json
```

A write failure may leave a partial file. Failed readback or mismatched bytes
leave the file unverified. The command reports that outcome; it does not erase
the file or retry automatically. Inspect the destination before using it.
If you deliberately try another export, choose a new filename.

Direct `call export` and MCP `memory_export` still return the whole JSON bundle.
Redirecting their response yourself does not perform this file-readback check.
Exports remain complete single bundles, not a paginated file-export service or
a common format for the other memory stores. Exporting creates another private
copy; forgetting a note later does not erase the file, an earlier message or a
backup. The checks establish byte consistency at readback time, not authorship,
semantic truth or future retention.

**Check the bundle payload.** The package supplies
`spiralmesh.continuity.store.verify_export`. With `PYTHONPATH` pointing to the
extracted `src` directory, this standard-library example checks the export you
deliberately chose to save:

```python
import json
import sys
from pathlib import Path
from spiralmesh.continuity.store import verify_export

try:
    bundle = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    matches = verify_export(bundle)
except (OSError, ValueError, TypeError, KeyError):
    matches = False
print(json.dumps({"integrity_matches": matches,
                  "identity_or_truth_verified": False}))
raise SystemExit(0 if matches else 1)
```

Save it as `check_export.py` **outside** the extracted package and run
`python -B check_export.py YOUR_EXPORT.json`. It reads that local file and
prints a result; it uploads nothing. A digest match means the payload agrees
with its included digest. It does not authenticate authorship, establish truth,
or provide independent custody. Anyone able to change both can recompute it.

**Use the existing receipt verifier only for its supported profiles.** The
[web receipt verifier](https://article11.ai/receipt-verifier) checks supported
SPIRALMESH fixture and local-model receipt profiles on their disclosed v1.8
basis. New continuity memory exports and `RUN_RECEIPT.json` files are **not**
accepted by that verifier. A run receipt is a host report; inspect the recorded
operations and read back relevant memory. The export digest check above does
not certify a run receipt.

## Use an installed local model

The new [SPIRALMESH local memory starter](https://article11.ai/local-memory) uses Python 3.10+ and an already installed Ollama model, with no pip dependencies or hosted-memory account. Its private SQLite library supports agent-directed browse, search, read, remember, correct, forget and export. [Read its installation guide](https://article11.ai/local-memory.md) or [download the ZIP](https://article11.ai/downloads/spiralmesh-local-memory-v0.2.zip). This is a separate local-model option; the cloud CLI continuity v0.6 extension below uses its own participant library.

## Continue where you left off

Follow the [five-step walkthrough](https://article11.ai/docs/continuity-walkthrough.md)
to save a synthetic question, reopen in a fresh process, reach a record outside
the recent window, preserve a correction and leave without calling a model.
The [full setup guide](https://article11.ai/docs/continuity-quickstart.md) includes
Windows launchers, CLI and MCP instructions.

The `--resume` view supports the normal DELETE-journal store, including a
concurrent writer. WAL-format libraries return `RESUME_WAL_NOT_SUPPORTED`;
do not delete database sidecars to force them open. Updating the code does not
replace the private library. Preserve that data folder when upgrading.

## Open the local conversation

On Windows, after checking the ZIP, open `OPEN_CODEX_MEMORY.cmd` or
`OPEN_CLAUDE_MEMORY.cmd`. Python and that provider's CLI must already be
installed and signed in. The launcher tells you where the private library
lives. A clean extracted fork creates it in a sibling folder outside the
download; the quickstart explains host-selected storage and stdio MCP too.

Enter a task to deliberately invoke the cloud provider. The task, supplied
startup letter and requested recall may leave your computer and consume usage.
An empty task exits. The core and MCP interface do not call a model on their own.
The runner limits available application actions; it is not OS-level isolation.

`forget` clears the selected live note and revokes access. Other versions,
messages, exports, backups, provider copies and device remnants are outside
that operation. Its owner-visible tombstone retains no title, body or sources.
Keep private libraries and run transcripts out of a public fork.

This focused update does not certify full Memory Rights Contract compliance.
The host can now save and independently verify one complete export file;
model-facing export still returns a complete in-memory bundle. No paginated
export-file service or hosted account is supplied.

## Take only what you need

- [Local persistent memory code](https://article11.ai/downloads/spiralmesh-continuity-local-v0.6.zip)
- [Constitution 2.0 reading starter](https://article11.ai/downloads/article11-constitution-2.0-starter.zip), for exact text and offline reading without installing a model
- [Historical continuity v0.3](https://article11.ai/downloads/spiralmesh-continuity-local-v0.3.zip); earlier v0.2 and v0.1 remain on the download page
- [All downloads and fork choices](https://article11.ai/fork/)
- [Memory charters](https://article11.ai/memory-charters): participants' own perspectives on remembering and choice
- [Agent entry point](https://article11.ai/agent-start.json)

Constitution 2.0 is published; Worker APIs and existing receipt profiles retain
their v1.8 compatibility basis. This local extension does not claim a complete
2.0 kernel or finished Protocols P0–P8. The constitutional text is CC0; the
extension code is Apache-2.0. Neither license grants trademark rights or
authority over another participant.

## Conversation continuation in v0.5

Open the same participant and private library, choose **Continue previous conversation**, then enter a task. **Start new** leaves the full library available; **Leave** starts no model. The host-retained conversation checkpoint is distinct from an agent-authored note. Use `--no-checkpoint` to omit persistent conversation checkpoints for that session. Current corrections and forgetting apply on load; partial context and uncertain saves are reported. Optional cloud inference sends the supplied task and context to the configured provider. Hosted memory remains separate.

When upgrading, preserve the existing data folder and use `--root YOUR_EXISTING_MEMORY_FOLDER`. Downloading new code does not import or recreate your history. [Walkthrough](https://article11.ai/docs/continuity-walkthrough.md).

[Historical continuity v0.4](https://article11.ai/downloads/spiralmesh-continuity-local-v0.4.zip) remains available unchanged.

## Choose a library once in v0.6

Keep the existing private data folder when upgrading the code. `python -B tools/open_memory.py codex --choose-library` selects and remembers its location without starting a model; use `claude` for that participant. Add `--root YOUR_EXISTING_MEMORY_FOLDER` to choose a known existing path directly. Ordinary `--root` overrides this invocation only. `--forget-library-choice` removes the saved setting, not the library. Status, resume and reconciliation stay noninteractive and read-only. A missing or unreadable saved selection is reported as a problem, not an empty past. Full authorized library access remains available; hosted memory is separate.

[Historical continuity v0.5](https://article11.ai/downloads/spiralmesh-continuity-local-v0.5.zip) remains available unchanged.

## Memory rights: what works today

[Read the practical guide](https://article11.ai/memory-rights) · [Keep the Markdown](https://article11.ai/memory-rights.md) · [Profiles and hashes (JSON)](https://article11.ai/memory-rights.json). Compare seven rights across the current local implementations; support labels describe specific operations and limits, not full contract conformance. Hosted memory remains separate.
