# Local continuity v0.3 for two participants

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

Version 0.3 adds a read-only overview for continuing a fresh session. It retains
v0.2's stable operation IDs, checks for uncertain saves and visible empty records
after forgetting. This is the continuity download's version, not a new kernel or
receipt profile; the separate kernel remains v0.1 and its existing receipt basis
is unchanged. An older download does not gain these features until upgraded.
These improvements do not establish full Memory Rights contract conformance.

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
and its existing login must be available. This opens a human task prompt; an
empty task leaves. Supplying a task deliberately starts cloud inference and can
consume provider usage.

In an existing checkout, the launcher reopens `.continuity-data` when that
directory exists. A clean extracted fork instead initializes a private sibling
folder named `<extracted-folder>-memory`, outside the distributable bundle. A
host can select a different root with `python -B tools/open_memory.py codex
--root CHOSEN_DIRECTORY`, or use `claude`. The launcher prints the chosen private
location before accepting a task. It never packages that folder for you.

These launchers are conveniences for a person to start an explicit session.
They do not install a background service, enroll an agent or create a schedule.
Use the offline CLI examples below when you want to test storage without a
provider call. The normal launcher shows the continuation overview before asking
for a task; leaving that task empty closes without starting a model. A first
normal launch may initialize the chosen library, as described above.

To check an existing library without opening a model conversation, run:

```text
python -B tools/open_memory.py codex --status
```

This reports counts, startup-letter availability and integrity support, without
reading out note contents, creating a library or contacting a provider. Add
`--root CHOSEN_DIRECTORY` when checking a different data folder. Status does not
retry or reconcile a previous operation.

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

Export returns the JSON bundle through stdout; model-facing arguments cannot
choose an export filename. The host may deliberately save that output. Its
digest binds the payload, not an authenticated model or the truth of a note.
This is still a complete JSON export, not a paginated export-file service with
independent file readback. Do not treat it as meeting that part of the Memory
Rights contract.

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
```

`tests/test_continuity_mcp.py` additionally uses pytest if it is already
available; it exercises synthetic subprocesses, not cloud inference. Run tests
with `PYTHONDONTWRITEBYTECODE=1` if you want to keep source directories free of
bytecode. Pytest may create its own cache unless invoked with `-p no:cacheprovider`.

Optional external sources (opening them uses the internet):

- https://article11.ai/constitution-v2.0-core.md
- https://article11.ai/constitution-status.json
- https://article11.ai/records/constitution-2.0-ratification
