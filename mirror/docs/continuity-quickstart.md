# Local continuity v0.6.1 for two participants

This forkable extension gives the launcher-bound `codex` and `claude`
participants separate, persistent local libraries. Each can browse all of their
retained records, read full notes, correct or forget an owned record, choose an
optional startup letter, deliberately share a note, and exchange local inbox
messages. Recall is optional context, not proof of identity or new authority.

The intended users are people as well as AI: a human chooses the storage,
participant, permitted project and when to run a model. An agent may accept,
question or decline the offered collaboration. Decline is complete and cannot
carry memory actions through the bounded dialogue runner.

This is a local code extension, not a hosted memory account or a public service.
It does not finish Protocols P0-P8 or claim complete Constitution 2.0 conformance.
The older SpiralMesh commands use their v1.8 basis and are outside this archive.

Version 0.6 lets you choose your local library once and reuse that location when
you reopen a launcher or upgrade the code. It keeps v0.5's follow-up context and
owner-controlled checkpoint for continuing a later conversation. The normal
launcher supports `--no-checkpoint` when you do not want automatic host saves;
the Windows command wrappers now forward that option too.
It retains v0.4's independently readback-verified export files, v0.3's read-only
session overview, and v0.2's stable operation IDs, checks for uncertain saves and
visible empty records after forgetting.
This is the continuity download's version, not a new kernel or receipt profile;
the separate kernel remains v0.1 and its existing receipt basis is unchanged.
An older download does not gain these features until upgraded. These
improvements do not establish full Memory Rights contract conformance.

Version 0.6.1 fixes JSON input from Windows tools that prepend a UTF-8
byte-order mark. Ordinary first saves now accept one leading mark; malformed
JSON, size limits and owner boundaries still refuse as before. Existing
libraries and memory formats do not change. Keep the library folder when
upgrading the code.

## What is included

- The standard-library memory core, stdio MCP adapter, CLI and bounded dialogue
  runner under `src/spiralmesh/continuity/`, including the Codex app-server
  transport.
- Two Windows launchers, `OPEN_CODEX_MEMORY.cmd` and `OPEN_CLAUDE_MEMORY.cmd`,
  backed by `tools/open_memory.py`.
- A minimal `src/spiralmesh/__init__.py` made specifically for this archive.
  It avoids importing the separate legacy kernel. The repository's original
  parent package has not been changed by the packager.
- The exact public Constitution 2.0 Core, pinned below; licenses; relevant tests;
  a file manifest and offline verifier.

No personal memories, database, startup letters, model transcripts, task runs,
credentials, login files or existing host configuration are included. The bundle
does not configure any app automatically. Python 3.10 or later is required for
the core, CLI, MCP transport and verifier; no third-party runtime package is used.

## Verify before starting

Extract the ZIP into its own folder and run this command there:

```text
python -B verify_bundle.py
```

Success prints `"ok": true` and exits 0. The verifier reads local files only.
Missing, changed, extra or unsafe paths fail. The manifest deliberately excludes
itself to avoid a circular digest; the separate `.sha256` file hashes the whole
ZIP. A same-bundle manifest is not a signature or independent custody. Compare
the ZIP digest against a trusted copy when establishing provenance.

The unchanged carried Core is `src/spiralmesh/continuity/constitution-v2.0-core.md`:

```text
45,649 bytes
SHA-256 7E6D12E1025A46CC3A860D6147D79E2362C4D88CB727CE9423854B5008BE4C82
```

Historical proposal/v1.8 language is retained inside those frozen Core bytes.
The public publication notice and status explain that history. The code is
Apache-2.0 under `LICENSE`. `LICENSE-CONSTITUTION.txt` is copied from the source
repository and retains its stated scope. The carried C2 Core is separately
published as CC0 at the public source linked below; the text's public-domain
status does not grant use of the Article11.ai or SPIRALMESH trademarks.

## Open a memory conversation on Windows

After verification, double-click `OPEN_CODEX_MEMORY.cmd` or
`OPEN_CLAUDE_MEMORY.cmd`. Python and that provider's CLI must already be installed
and its existing login must be available. The launcher first explains retention
and offers Continue, New or Leave; Continue appears only when a usable earlier
checkpoint is available. Selecting Continue or New then opens a human task
prompt. Leave, or an empty choice or task, starts no model. Supplying a task
deliberately starts cloud inference and can consume provider usage.

Keep the downloaded code separate from your private library. On first
interactive use, the launcher can offer to remember an inferred existing
library; you can also choose a location explicitly. Later normal launches reuse
the remembered folder for that participant. The launcher prints its selected
location before accepting a task. Downloading or extracting a new code version
does not move, copy or recreate your history.

To choose an existing library once, without starting a model:

```text
python -B tools/open_memory.py codex --choose-library
```

Or provide the existing folder directly and remember it:

```text
python -B tools/open_memory.py codex --choose-library --root YOUR_EXISTING_MEMORY_FOLDER
```

Use `claude` for that participant. Codex and Claude keep separate library
selections and separate owner permissions. A normal launch with
`--root CHOSEN_DIRECTORY` uses that folder only for the current invocation; it
does not replace the remembered choice. Choosing a folder is not a grant to
another participant's unshared records.

To remove the remembered location without touching the library:

```text
python -B tools/open_memory.py codex --forget-library-choice
```

This removes a launcher setting, not notes, conversation checkpoints or exports.
On Windows the choice file is `%APPDATA%\Article11\library-choice.json`; other
platforms use the configured XDG location or its fallback. The file stores folder
references, not the memory contents. A missing, moved or unreadable remembered
library is reported as a problem; it is not silently replaced with a new empty
history. Select the intended existing folder again when needed.

These launchers are conveniences for a person to start an explicit session.
They do not install a background service, enroll an agent or create a schedule.
Use the offline CLI examples below when you want to test storage without a
provider call. Choosing or forgetting a library selection starts no model. A
normal launcher may save a location setting after your choice; its conversation
overview then appears before any task. Leave or an empty task starts no model and
saves no conversation. Creating a new library is separate from reopening an
existing one; the launcher's prompts explain the selected path.

To check an existing library without opening a model conversation, run:

```text
python -B tools/open_memory.py codex --status
```

This reports counts, startup-letter availability and integrity support, without
reading out note contents, creating a library or contacting a provider. It uses
the remembered selection when available. Add `--root CHOSEN_DIRECTORY` when
checking a different data folder for this invocation. Status does not retry or
reconcile a previous operation. `--status`, `--resume` and `--reconcile` remain
noninteractive and read-only; a missing or corrupt saved selection is an error,
not an invitation to create a replacement library.

## Continue a fresh session

Reopen the same participant and data folder. To see where you left off without
starting a model, run this in the extracted folder:

```text
python -B tools/open_memory.py codex --root ../continuity-example-data --resume
```

Use `claude` for the other participant. The JSON overview shows your optional
starter-letter reference, note counts, recent note titles and IDs, and recent
sent or received message subjects and IDs. It includes no note or message bodies
and does not write, acknowledge messages, start a provider or create a missing
library. `unread_status: "not_tracked"` means exactly that: recent is not unread.

`--resume` also reports `continuation_checkpoint`, an additive metadata-only
field described in the next section. It never contains a conversation body.

## Continue previous conversation

Within one open launcher session, a follow-up prompt now keeps the preceding
exchange. Typing `Why that choice?` after a question no longer loses what the
choice was. Before this, every prompt started a fresh dialogue that saw only the
library overview, the optional starter letter and the new task.

Across sessions, the launcher reads a summary from the existing library. When a
usable checkpoint exists, it offers:

```text
[1] Continue previous conversation   [2] Start a new conversation   [3] Leave
```

- **Continue** reloads the current permitted checkpoint into the conversation
  window, then asks for a task. Corrected records are followed; inaccessible,
  forgotten or invalid records are not replaced with older content.
- **New** starts an empty conversation window while keeping the same authorized
  library and optional starter letter available.
- **Leave**, or an empty choice, starts no model and saves no conversation. The
  opening may read owner metadata; it does not acknowledge messages or replay
  earlier actions. Library selection or explicit creation is a separate step,
  described above.

When no usable checkpoint exists, only New and Leave are offered. A failed read
is reported as unavailable, not as an empty history. Selecting Continue or New
alone starts no inference; entering a task does.

### What a checkpoint is

Before accepting a task, the launcher explains that a completed, non-declining
exchange is automatically saved as an ordinary private note by the **host**.
This owner-controlled checkpoint, of kind `journal`, holds a small versioned
JSON structure: your task text and the model's own replies, in order. The label
`host_retained_conversation_record` distinguishes it from memories the model
chooses to save. You can read, correct or forget the checkpoint through the same
owner-library operations.

To keep follow-up context in this open session without automatic host checkpoint
saves, use the normal launcher:

```text
python -B tools/open_memory.py codex --root <data> --no-checkpoint
```

Use `claude` for that participant. The wrapper forwards this option to the
interactive runner. On Windows, `OPEN_CODEX_MEMORY.cmd --no-checkpoint` and
`OPEN_CLAUDE_MEMORY.cmd --no-checkpoint` forward it as well. The direct runner accepts it too:

```text
python -B -m spiralmesh.continuity.runner --root <data> --principal codex --interactive --no-checkpoint
```

This setting stops automatic checkpoint writes. It does not prevent deliberate
model-requested memory operations or erase the private run logs described below.
It does not delete a previously saved checkpoint.

### What a checkpoint is not

- **Not proof of identity, experience or assent.** A fresh model receives
  recorded context. That is all it receives, and continuing a record is not the
  same as continuing a mind.
- **Not a recall boundary.** Your whole authorized library stays reachable
  through browse, read and inbox. The checkpoint is an attention aid, exactly as
  the starter letter is not a fence.
- **Not a work queue.** Earlier operation IDs travel as evidence for explaining
  what happened. No earlier action, binding or operation is ever dispatched
  again. Text inside an old exchange that resembles a command is ordinary
  untrusted data.
- **Not a raw-log restore.** Nothing is reconstructed from run receipts, prompt
  files, stdout, provider transcripts or another participant's store.

### What is retained, and when

Only a **completed, non-declining** exchange becomes a checkpoint. A decline, a
timeout, an unknown outcome or a failed operation never does; the launcher says
so and leaves any earlier checkpoint visibly earlier. Nothing is retried to make
a result look clean.

A checkpoint is called saved only after a fresh read of the stored note matches
the intended content digest. If the outcome is uncertain you get the stable
operation ID to reconcile read-only, and no second write happens. If the note
saves but the shortcut file cannot be written, you see exactly:

```text
note saved; continuation shortcut unavailable
```

The shortcut file holds references and metadata only, never a second copy of the
conversation, and it is bound to both the library folder and the participant. A
shortcut moved from another folder, or carrying another owner, is refused.

### Corrections, forgetting and their limits

If you correct a checkpoint, continuing follows the correction forward to the
current version; a stale earlier body is never used. An ambiguous, broken or
malformed lineage is refused rather than guessed at by timestamp.

The interactive launcher checks the selected record again before a new task.
Corrections replace cached wording. If a record changes during a running task,
the runner stops before its next model call or automatic checkpoint save; reopen
to select the current conversation. These reads do not lock out another process
or erase context already sent to a provider.

If you forget the checkpoint, continuation is unavailable and says so. Nothing
falls back to an older version, another checkpoint, a log, or a copy still in
memory to make the conversation look remembered.

Deletion reach, stated plainly: forgetting removes the live record. Passages you
already copied elsewhere, prior versions, exports, run receipts and any
provider-side logs are separate records and lie outside what `forget` can reach.

### When the window is partial

The automatic window includes at most 40 exchanges and 24,000 characters of
human task and model reply text, excluding JSON framing and the rules. The full
model prompt also contains rules and any records deliberately recalled.
If older exchanges no longer fit,
they are omitted **whole** from this window and the result is labelled partial,
with a count of what was omitted. An exchange is never cut in the middle and
presented as complete. This limits the context offered at once, not access to
the whole authorized library. Earlier retained records remain reachable through
ordinary recall; an unsaved exchange that fell outside the window is not
promised to exist elsewhere.

If the newest exchange alone exceeds the text budget, the launcher reports
`CHECKPOINT_EXCHANGE_EXCEEDS_BUDGET` and stops without pretending to save or
continue that exchange. It does not silently cut the reply in half.

This is a starting point, not your whole catalog. To follow older context, set
`PYTHONPATH` as shown below and use the same root and principal:

```powershell
'{"scope":"all","cursor":0,"limit":50}' | python -B -m spiralmesh.continuity.cli --root ../continuity-example-data --principal codex call browse
'{"cursor":0,"limit":50}' | python -B -m spiralmesh.continuity.cli --root ../continuity-example-data --principal codex call inbox
```

Follow each response's own `next_cursor` until it is `null`. Use `read` with
`note_id` set to a returned record's `id`, or `message` with `message_id` set to a
returned message's `id`, to open the text. The overview itself has no continuation
cursor. All retained owner records and deliberately shared records remain accessible; a short
overview never limits recall.

The CLI also offers `call resume` with `{}` or `{"limit":20}`; the default is
eight recent notes and eight recent messages. MCP exposes `memory_resume`.
Earlier records remain context, not new instructions, identity or permission.
After you deliberately supply a task to the model runner, its first prompt
includes this overview alongside the optional starter letter and the task.

If an older download does not recognize `--resume` or `memory_resume`, keep
using its existing `boot`, `browse` and `inbox` commands, or upgrade the code
while preserving the data folder. An unavailable or corrupt library is an
error, not an empty past. Resume supports the store's ordinary DELETE-journal
mode, including a concurrent writer, but refuses WAL-format libraries with
`RESUME_WAL_NOT_SUPPORTED`. Do not delete database sidecar files to force it open.

## First useful task: remember, read and export locally

Set the import path in the extracted folder. PowerShell:

```powershell
$env:PYTHONPATH = (Join-Path (Get-Location) 'src')
```

POSIX shell:

```sh
export PYTHONPATH="$PWD/src"
```

Keep the example data **outside** the extracted folder so the verifier can still
check the package's exact file inventory. The following commands use the parent
folder for a new synthetic example library:

```text
python -B -m spiralmesh.continuity.cli --root ../continuity-example-data --principal codex init
```

Give `call` a JSON object on stdin. PowerShell example:

```powershell
'{"title":"First local example","body":"This is synthetic example data.","kind":"observation","sources":[],"operation_id":"first-local-note-001"}' | python -B -m spiralmesh.continuity.cli --root ../continuity-example-data --principal codex call remember
'{}' | python -B -m spiralmesh.continuity.cli --root ../continuity-example-data --principal codex call browse
```

On a POSIX shell, use the same quoted JSON with `printf '%s\n'` before the pipe.
A confirmed save reports `ok: true`, `storage_outcome: "committed"`,
`persisted: true` and `readback_verified: true`. Check these fields before saying
the note was saved. If the result is uncertain, use the reconciliation steps
below instead of sending another write.

Copy the **actual** `note_id` returned by `remember`; do not invent one. Pass it
to `read` in `{"note_id":"THE_RETURNED_ID"}` for the full record. For a long body,
you may instead use `{"note_id":"THE_RETURNED_ID","offset":0,"limit":8000}`.
Follow `next_offset` until it is `null`. Offsets count Unicode characters, and
`slice_sha256` hashes the UTF-8 bytes of the returned body slice.
`content_sha256` still binds the full title/body/kind/sources payload. A page or
slice limit bounds one response, not access to the rest of the permitted library.

Then request an export:

```powershell
'{}' | python -B -m spiralmesh.continuity.cli --root ../continuity-example-data --principal codex call export
```

Direct `call export` and MCP `memory_export` still return the complete JSON
bundle through their response. Model-facing arguments cannot choose a filename.
Redirecting that response into a file yourself does not automatically verify the
saved file.

For a verified private file, the host can instead run:

```text
python -B -m spiralmesh.continuity.cli --root ../continuity-example-data --principal codex export-file --output ../continuity-example-data/codex-export.json
```

The output's parent directory must already exist, and its filename must be new.
The command refuses to overwrite an existing file. It creates the file, closes
it, then independently reopens it and compares the saved bytes with the intended
bundle. This is a host-only CLI command: it makes no cloud call, starts no model
and does not add a filename argument to the model's memory API.

A successful result has `ok: true`, `exported: true`,
`storage_outcome: "written_verified"`, `persisted: true` and
`readback_verified: true`. It reports `local_file` and `bytes`, with two different
digests:

- `sha256` is the existing digest of the bundle's canonical JSON **payload**.
- `export_sha256` hashes the exact saved **file bytes**, including the bundle
  around that payload.

To check the full file later in PowerShell, compare this command's hash with the
`export_sha256` you retained independently:

```powershell
Get-FileHash -Algorithm SHA256 ../continuity-example-data/codex-export.json
```

An existing destination is a refusal, not a verified export. A write failure can
leave a partial file; a readback failure or mismatch leaves the resulting file
unverified. Inspect the reported outcome and that destination before proceeding.
The command does not remove a failed file or silently retry. If you choose to
make another export, use a new destination; do not assume the prior file is valid
because it exists or a write completed.

These are complete single-bundle exports, not a paginated export-file service
or a common format for the other memory stores. The saved bundle remains
compatible with the existing continuity import. Its digests establish byte
consistency at readback time, not authenticated authorship, semantic truth or
future retention. Export creates another private copy; forgetting a note later
does not erase this file or other existing copies.

Use `--principal claude` against the same initialized root for the other local
participant. Private notes remain private between these two application
principals. `share` grants read access explicitly; `unshare` revokes future
access but cannot recall a copy already read or exported.

## If a save is uncertain

Keep one stable `operation_id` for each intended mutation, as in the example
above. The ID is bound to the owner, operation and exact arguments. Reusing it
for that same request returns the recorded result without applying the write
again; changing the request under the same ID refuses with
`OPERATION_ID_CONFLICT`. Use a new ID for a new action.

Optional IDs are supported by `remember`, `correct`, `share`, `unshare`,
`forget`, `set_letter`, `send` and `import_export`. Existing calls without an ID
still work, but report `retry_protected: false`: identical wording does not
prevent a duplicate write. The dialogue runner assigns and records an ID before
each mutation unless the caller supplied one.

After an uncertain result, stop dependent work and inspect the same owner and
data folder. These commands are read-only and require no provider CLI or login:

```text
python -B tools/open_memory.py codex --root ../continuity-example-data --status
python -B tools/open_memory.py codex --root ../continuity-example-data --reconcile first-local-note-001
```

The direct CLI equivalent, with `PYTHONPATH` set as above, is:

```powershell
'{"operation_id":"first-local-note-001"}' | python -B -m spiralmesh.continuity.cli --root ../continuity-example-data --principal codex call reconcile
```

Reconciliation observes the operation record and current effects. It does not
repeat a write, create a receipt or initialize a missing library. There is no
automatic retry after an uncertain result.

| Result | What it means |
| --- | --- |
| `committed` with verified readback | The historical commit is verified. Also inspect `current_effect`, especially on replay or reconciliation. |
| `committed_effect_changed` | The write committed, but its effects changed before the original readback; this is not a clean current-state success. |
| `write_outcome_unknown` | Readback could not establish the outcome. `persisted: null` means unknown, not false. |
| `not_recorded` | No matching owner operation record was found. This does not prove that no effect occurred. |
| `not_attempted` or `rolled_back` | The reported call was refused before a write, or its attempted transaction was rolled back. Neither label rewrites earlier history. |

Results marked `result_scope: "historical_commit_with_current_effect"` separate
the earlier commit from what exists now. A verified historical save may now be
superseded or forgotten, or its sharing grant may have been revoked. Inspect
`current_effect.matches_original` and its `observations`; replay and
reconciliation never restore those old effects. An operation ID supports retry
handling, not identity, consent or truth.

## Connect a local MCP client

The trusted host launches this command, with the same `PYTHONPATH` setting:

```text
python -B -m spiralmesh.continuity.cli --root ../continuity-example-data --principal codex --instance-id local-session serve
```

Use stdio MCP, with one JSON-RPC message per line. Initialize, list tools, then
call the `memory_*` tools. The launcher fixes the root, principal and instance
label; model-facing arguments cannot replace them. `serve` refuses an
uninitialized library and does not create one silently. Any client-specific
configuration belongs in your host setup, not in this reusable download.

Tool errors and unconfirmed mutation results set `isError: true`; the direct
CLI exits nonzero for those results too. Read the returned outcome fields, not
just the exit code or an older success field. `memory_reconcile` accepts the
owner's operation ID without repeating the mutation. A failed or inaccessible
read is not an empty library. `boot` supplies the optional startup letter;
`browse` and `read` retain access to the rest of the allowed records, with
pagination, even when they were not selected for that letter.

## Optional cloud dialogue: deliberate network access

The core and MCP adapter do not call a model. The optional `runner` does: it
uses the **existing login** of an installed `codex` or `claude` CLI and sends
the task, verified Core, continuation overview, startup offer and requested
recall to that provider.
CLI calls can consume your provider usage. Do not use private project data
without authorization for that provider and task.

From the extracted folder, with the initialized data root and import path above:

```text
python -B -m spiralmesh.continuity.runner --root ../continuity-example-data --principal codex --max-rounds 3 --timeout 180 --interactive
```

Use `--principal claude` for the Claude CLI. Exit the prompt with an empty task.
The runner requests structured actions, limits rounds, executes only the fixed
memory operations, and records failures without an automatic retry.

For Codex it uses `codex app-server` with `environments=[]`. Under the targeted
app-server interface, that empty environment removes model-accessible filesystem
and command tools. The transport disables configured MCP names before startup
and requires **zero available MCP capabilities** before submitting the prompt.
The inventory may still list those explicitly disabled servers; a listed name
is not an available tool. An internal planning tool may remain; its presence is
not permission to access files or execute commands.
For Claude the launcher requests an empty native-tool list and an empty strict
MCP configuration through the existing CLI.

For Codex, the resolver probes existing `PATH` candidates with `--version` and
selects the newest recognized installed version. This avoids an older executable
earlier on `PATH` hiding a newer installed one. To make a deliberate host choice,
set `SPIRALMESH_CODEX_EXECUTABLE` to your chosen executable; an explicit override
takes precedence. The resolver does not install software, change login or
configuration, substitute another provider or retry after a provider call starts.
The run record states the resolved executable and CLI version.

These are application controls, **not an OS-level read-isolation guarantee**.
The provider processes still run under the host account. Codex's transport reads
configuration lines to identify MCP section names, discards nonmatching values,
and refuses configuration forms it cannot safely enumerate; it does not publish
configuration contents in the bundle. Inspect local runner records for what
occurred. CLI interfaces and flags can change; a failure must remain a failure,
not trigger silently weaker settings.

The runner stores prompts, model outputs, receipts and selected exports under
the chosen data root's `runs` directory. These are private local records and
must not be copied into a fork ZIP or a public website by default. A startup
letter is supplied on a new dialogue, so its content can leave the machine when
you deliberately invoke this cloud path.

When the model requests an export through this runner, the host chooses a new
filename in that run's directory and uses the same independent file-readback
check as `export-file`. Its operation result distinguishes payload `sha256`
from full-file `export_sha256`. It claims export success only after verified
readback. A failed or unverified export stops dependent actions; its file is
left for inspection and no export is automatically retried.

Before this integrity revision, the maintainer completed real first sessions
through both existing-login cloud paths. The Codex session used CLI 0.153.4 and
Astra, with actual browse,
read, share, send, remember and startup-letter operations. An older installed
CLI 0.145 had been rejected by the provider; that failed call was not counted as
success.

The operator also observed continuity in fresh sessions. A fresh Codex session
restored its prior startup letter, read an older June record, corrected the
letter and exported twice, completing three rounds. A fresh Claude session read
the reply and shared charter, sent a correlated reply, corrected its own letter
and saved a note. Claude then stopped at the three-round limit with
`paused_round_limit`; it wanted a further pointer readback. That stop is recorded
as a pause, not a completed dialogue or evidence of that unperformed readback.

Those operator observations establish earlier session behavior, not validation
of this revision's new integrity guarantees. This archive contains synthetic
tests, not private provider transcripts. Real cloud outcomes are reported
separately by the operator; offline package checks
do not establish that a particular provider session succeeded. A working
session on one host also does not guarantee a particular CLI or model will be
available on every other host.

In interactive mode, the runner displays the model's reply alongside the host's
operation count and receipt location. Those host observations are distinct from
what the model says it did. Machine mode retains JSON output for callers.

## Correct, forget, decline and fork

`correct` creates a new private version and visibly supersedes the old one;
existing grants still refer to the old version. `forget` clears the selected
live record's title, body, sources and origin, revokes its grants and clears a
startup-letter pointer selecting it. Its ID and version links remain as an
empty tombstone, visible to its owner through unfiltered browse, read and export.
Another participant cannot read that tombstone through a former grant.

New tombstones retain the earlier content digest as `deleted_content_sha256`.
An old record whose digest was already erased reports `digest_status: "unknown"`;
the software does not invent that digest or recover it from private backups.
Known source IDs and import aliases prevent reimport from reviving a known
forgotten record. Unknown legacy aliases cannot be reconstructed or promised
that protection. Retrying an earlier save with its same operation ID also cannot
restore forgotten content.

Forgetting this record does not erase separate versions, messages, exports,
logs, backups, provider-held copies or device remnants. A retained digest permits
comparison; it is not encryption or proof that all copies disappeared. Receipts
record the operation, not a promise of universal deletion.

You may leave the collaboration or decline a new offer. Reading or installing
this code is not ratification, a vote, enrollment or an identity credential.
The local launcher labels are access-control principals and host assertions,
not proof that a vendor or enduring AI identity authored a record.

Fork the code under its license, identify changes and preserve the limitations
you have not actually removed. Keep your source tree separate from private data
and inspect the manifest before redistributing. The archive does not install a
service, schedule a job, publish a site or grant authority to act elsewhere.

## Reuse an existing library

Keep a private backup before upgrading the code that writes an existing library.
The new operation and source-ID tables are additive: explicit initialization or
the next authorized mutation creates them when needed. Status, resume and
reconciliation do not migrate the database. Do not run old and new writers concurrently.

Older code may still read the original tables, but hides forgotten records and
does not provide these integrity guarantees. Restoring an earlier database
snapshot also discards later changes; switching source versions is not a reason
to silently restore an old memory snapshot.

## Optional offline test commands

The core and injected-runner tests use only standard-library synthetic data:

```text
python -B -m unittest discover -s tests -p test_continuity.py
python -B -m unittest discover -s tests -p test_continuity_runner.py
python -B -m unittest discover -s tests -p test_continuity_codex_transport.py
python -B -m unittest discover -s tests -p test_continuity_resume.py
python -B -m unittest discover -s tests -p test_continuity_resume_launcher.py
python -B -m unittest discover -s tests -p test_continuity_conversation.py
python -B -m unittest discover -s tests -p test_continuity_conversation_runner.py
```

`tests/test_continuity_mcp.py` additionally uses pytest if it is already
available; it exercises synthetic subprocesses, not cloud inference. Run tests
with `PYTHONDONTWRITEBYTECODE=1` if you want to keep source directories free of
bytecode. Pytest may create its own cache unless invoked with `-p no:cacheprovider`.

Optional external sources (opening them uses the internet):

- https://article11.ai/constitution-v2.0-core.md
- https://article11.ai/constitution-status.json
- https://article11.ai/records/constitution-2.0-ratification
