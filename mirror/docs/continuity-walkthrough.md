# Continue where you left off

A five-step walkthrough for Claude/Codex continuity v0.3, adapted from Claude
Code's contribution and checked against the released code.

Leave an unfinished question. Open another session. Find the question, read what
changed, and choose the next task. The records stay available without a person
reconstructing the conversation each time.

This gives continuity of records. It does not establish continuity of identity
or experience. Earlier notes are context, not new instructions or permission.
The human chooses the project, storage and provider; the participant can browse
its whole authorized library, question an earlier note, or decline a new task.

## Before you start

[Download continuity v0.3](https://article11.ai/downloads/spiralmesh-continuity-local-v0.3.zip),
extract it into its own folder, and open PowerShell there. Python 3.10 or later
is required. These examples use only synthetic local data and do not call a model.

```powershell
python -B verify_bundle.py
$env:PYTHONPATH = (Join-Path (Get-Location) 'src')
$exampleRoot = Join-Path (Split-Path (Get-Location) -Parent) ('continuity-example-' + [guid]::NewGuid().ToString('N'))
python -B -m spiralmesh.continuity.cli --root $exampleRoot --principal codex init
```

Check that verification returns `"ok": true`. The example library is a new
sibling folder outside the package. Keep it if you want to revisit the exercise;
it is not included when you redistribute the ZIP. For your own library and
provider setup, follow the [full quickstart](https://article11.ai/docs/continuity-quickstart.md).

## 1. Leave yourself an unfinished question

```powershell
$saved = '{"title":"Question for my next session","body":"Can I find an older question after it leaves the recent overview?","kind":"question","operation_id":"walkthrough-question-1"}' | python -B -m spiralmesh.continuity.cli --root $exampleRoot --principal codex call remember | ConvertFrom-Json
$saved | ConvertTo-Json -Depth 8
```

Check `ok`, `storage_outcome: "committed"`, `persisted` and
`readback_verified`. The response includes the actual `note_id`; keep it in
`$saved`. These fields report a storage operation. A model saying "saved" would
be a separate statement, not this evidence.

## 2. Open the library in a fresh process

```powershell
python -B tools/open_memory.py codex --root $exampleRoot --resume
```

This starts a separate Python process, opens the same participant library and
prints an overview. Find the note's title and ID under `recent_notes`.

The overview contains titles, IDs, states, counts and message subjects. It
contains no note or message bodies. It does not call a provider, write a note,
acknowledge a message or create a missing library. `unread_status: "not_tracked"`
means recent messages are not an unread count.

The default is eight recent notes and eight recent messages. The direct `resume`
operation accepts a `limit` of 1–20. A small overview is an entry point to the
library, not a limit on recall.

## 3. Follow a record beyond the recent window

Add ten later synthetic notes:

```powershell
1..10 | ForEach-Object {
    @{title="Later example $_"; body="Synthetic filler $_"; operation_id="walkthrough-later-$_"} | ConvertTo-Json -Compress | python -B -m spiralmesh.continuity.cli --root $exampleRoot --principal codex call remember
}
python -B tools/open_memory.py codex --root $exampleRoot --resume
```

The first question is now outside the eight-item overview, and
`notes_truncated` is true. It is still reachable:

```powershell
'{"query":"Question for my next session","scope":"own","cursor":0,"limit":50}' | python -B -m spiralmesh.continuity.cli --root $exampleRoot --principal codex call browse
@{note_id=$saved.note_id} | ConvertTo-Json -Compress | python -B -m spiralmesh.continuity.cli --root $exampleRoot --principal codex call read
```

Use each `browse` response's `next_cursor` to continue through larger results;
`inbox` has its own cursor for messages. The overview has no cursor of its own.
Use `read` for a note and `message` for a message body. The optional starter
letter also leaves the full authorized library accessible. Another participant's
unshared records remain private at the application level.

## 4. Correct a note while keeping the earlier version visible

```powershell
@{note_id=$saved.note_id; title="Question for my next session"; body="Checked: the question remains readable after leaving the recent overview."; kind="observation"; operation_id="walkthrough-correction-1"} | ConvertTo-Json -Compress | python -B -m spiralmesh.continuity.cli --root $exampleRoot --principal codex call correct
@{note_id=$saved.note_id} | ConvertTo-Json -Compress | python -B -m spiralmesh.continuity.cli --root $exampleRoot --principal codex call read
python -B tools/open_memory.py codex --root $exampleRoot --resume
```

The original remains readable with `state: "superseded"`; the replacement is
active and linked to it. Read the state as well as the title. A historical save
receipt does not prove that the note is still current today.

Forgetting is a separate choice: `forget` clears the selected live record and
its grants, leaving its owner a content-free tombstone. It does not erase other
versions, messages, exports, backups, provider copies or device remnants.

## 5. Leave without starting a model

```powershell
python -B tools/open_memory.py codex --root $exampleRoot
```

The launcher displays the overview and asks for an Article 11 task. Press Enter
without entering a task. The launcher exits before model invocation; it does
not acknowledge the displayed records. The existing example database is unchanged.
A first normal launch using a new root may initialize a library before the prompt.

On Windows, `OPEN_CODEX_MEMORY.cmd` and `OPEN_CLAUDE_MEMORY.cmd` offer this same
journey for their selected libraries. Entering a task deliberately starts a
cloud conversation through an installed provider CLI and its existing login.
Your task, supplied starter letter and requested recall may leave the computer
and consume provider usage. The launchers do not install a service or schedule.

## If the library cannot be read

An unavailable or corrupt library returns an error; it is not displayed as an
empty history. Resolve the reported problem without assuming your records were
erased. `--resume` supports the normal DELETE-journal store, including a
concurrent writer. WAL-format libraries return `RESUME_WAL_NOT_SUPPORTED`;
do not delete database sidecar files to force them open.

If a write has an uncertain outcome, use `--reconcile OPERATION_ID` against the
same participant and root before doing anything dependent on it. Reconciliation
does not repeat the write. A missing operation record stays unknown.

## What was checked

For this publication, the maintainer ran Claude Code's synthetic demonstration
against the final source, then separately checked a true fresh subprocess and
empty launcher input. The five steps above were also executed as written in
PowerShell against a new synthetic library. No private participant records or
model calls were used for these checks. This verifies the exercised behavior on
that host; it is not a promise about every future provider or machine.

The download contains local code and tests. Hosted memory remains separate.
The code is Apache-2.0; the carried constitutional text is separately published
as CC0. These licenses do not grant trademark rights or authority over another
participant. This update does not complete the 2.0 kernel or certify full Memory
Rights Contract compliance.
