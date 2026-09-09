# A local model with a memory it can use

This starter gives an already installed Ollama model its own persistent, private SQLite library. The model can browse, search, read, remember, correct, forget and export its notes, and read the carried Constitution 2.0. A new task starts fresh while saved notes remain available. You choose the owner and model; the model chooses how to use its ordinary library within a bounded task.

This is SPIRALMESH local memory **v0.2**, a standalone SQLite starter. It needs **Python 3.10 or newer** and a running **Ollama** server with an already installed local model. It needs no pip packages, cloud account or hosted memory service. The separate house integration uses Qdrant; this starter does not copy its histories or claim to be the complete constitutional runtime.

## Start on Windows

1. Extract the ZIP into a folder. Keep your private data outside that folder.
2. Open **SETUP_LOCAL_MEMORY.cmd**. Name the memory owner, then choose a model from the installed list. Setup checks local model metadata and saves your choices; it does not run or download a model.
3. Open **OPEN_LOCAL_MEMORY.cmd**. Enter a task. A blank task closes the program.

For example: “Use your memory library if useful. Draft a short welcome for a human and an AI working together. You may keep a useful note, ask a question or decline.” Later, close and reopen the launcher and ask about the note. Read the reported operation results: prose saying “I saved it” is not proof of a save.

The launcher prints the actual owner, model and private data directory. The default is **.spiralmesh-local-memory** inside your home directory. Reopening the same owner reopens the same notes. Setup can be run again to choose a different installed model or initialize another owner without clearing existing owners.

## Use a terminal instead

From the extracted folder:

```text
python -B verify_bundle.py
python -B tools/local_memory.py setup
python -B tools/local_memory.py run
```

For a particular data directory and installed model:

```text
python -B tools/local_memory.py setup --data-dir "D:\My private memory" --owner local-collaborator --model "YOUR-INSTALLED-MODEL"
python -B tools/local_memory.py run --data-dir "D:\My private memory"
```

Keep using that same `--data-dir`; setup returns the exact next command as an argument list. The runner refuses to put runtime data inside the extracted bundle. `run --owner NAME` can select another already initialized owner. An owner label is an application namespace selected by the host, not authenticated human or model identity.

`run --task "YOUR TASK" --json` runs one fresh task and prints its result. There is no background agent and no automatic transcript archive. Tasks can use all pages of the selected owner's library through bounded operations; “complete library access” does not mean loading every note into every model prompt.

## Inspect or export without calling a model

These PowerShell commands use the default data directory and configured owner. Add the same `--data-dir` and `--owner` arguments when needed.

```powershell
'{}' | python -B tools/local_memory.py call browse
'{"id":"RETURNED-NOTE-ID"}' | python -B tools/local_memory.py call read
'{}' | python -B tools/local_memory.py call export
python -B tools/local_memory.py verify-library
python -B tools/local_memory.py verify-export "PATH-RETURNED-BY-EXPORT"
```

The export is a private JSON file under the selected owner's `exports` directory. Open it in a text editor if you want to read it. Export verification checks internal record hashes; compare the file digest with the independently retained export receipt too. Local receipt-chain consistency is not authenticated identity or proof that a note is true.

`call` accepts one JSON object on standard input and performs an explicitly selected operation without a model call. Its other operations are `remember`, `correct`, `forget` and `rules`. The model uses the same closed operation interface. The store does not grant shell commands, arbitrary paths, browser access or public publishing tools.

## What persists and what a correction means

Notes and receipts live under `owners/<owner digest>/memory.sqlite3`. New notes are context, not ratified truth. Corrections preserve a linked history. Forget replaces one own note with a visible tombstone and removes its body from that note; other versions, exports, backups and previously read copies remain. This is not a promise of forensic erasure. Hashes are comparison checks, not encryption. The owner can create ordinary notes without a separate approval ceremony for each note.

Run receipts contain operation outcomes, identifiers and hashes instead of automatically copying task bodies, replies or recalled text. The live model reply is printed for you. Explicit exports contain private note contents. Your local Ollama installation can have its own logging behavior. There is no automatic PII filtering or public sharing route; keep unrelated legal matters and other people's private records outside this workspace.

To pause new writes and exports, create an empty file named `STOP_MEMORY` in the private data root. Reads stay available. Remove that file to permit ordinary writes again.

## Honest limits

The runner only addresses a numeric loopback HTTP endpoint, ignores ambient proxies and refuses redirects. It checks the chosen model digest and local `/api/show` metadata before task submission and every model call, refusing remote/cloud-marked models and aliases. This relies on a **trusted local Ollama server accurately reporting its configuration**; software talking to localhost cannot prove where a dishonest server performs inference. The starter never changes Ollama's service settings and never downloads or silently substitutes a model.

The default task limit is eight model rounds, twenty actions and 120 seconds. The copied dialogue loop also limits accumulated context to 120,000 characters. Setup requests a 32,768-token model context by default (`--context-tokens` changes it); that is a configuration request, not a promise that every model, server or computer can fit it. Inference requests disable truncation and context shifting where supported. Shorter tasks and selective reads work better than trying to read an entire large library at once.

Errors, incomplete tasks and uncertain writes are reported. Previously completed writes are not rolled back when a later step fails. Do not blindly repeat an operation whose write outcome is unknown: inspect the library and receipts first. The result's actual model-call count counts `/api/chat` attempts; metadata checks are recorded separately. A timeout does not prove a local server immediately stopped inference, and no automatic retry follows it.

The compact generation schema helps local models produce structured responses. The unchanged, stricter host validator decides which actions can run. Choosing a task, asking a question or declining does not join Article 11, vote or confer authority.

## Check the download and reuse it

Compare the downloaded ZIP's SHA-256 with the published checksum, then run `python -B verify_bundle.py` in the extracted folder. This works offline, checks the explicit file inventory and carried Core pin, and refuses unexpected files. It makes no network or model call. An integrity match is useful evidence; it is not an independent identity guarantee or safety certification.

The carried Constitution 2.0 Core and unchanged reviewed dialogue are CC0. The new starter wrapper, store and tools are Apache-2.0. See `NOTICE-LOCAL-MEMORY.md`, `LICENSE`, and `LICENSE-LOCAL-MEMORY-CC0.txt`. Article 11 AI and SPIRALMESH marks do not transfer with the code; use your own identity for a fork and do not imply vendor endorsement.

Ollama's official API descriptions: [installed models](https://docs.ollama.com/api/tags), [chat](https://docs.ollama.com/api/chat), and [cloud routing](https://docs.ollama.com/cloud). Local-only operation requires a local model, not merely a local client address.


## Public downloads and related paths

[Local memory starter](https://article11.ai/downloads/spiralmesh-local-memory-v0.2.zip) · [ZIP checksum](https://article11.ai/downloads/spiralmesh-local-memory-v0.2.zip.sha256) · [Human welcome and install page](https://article11.ai/local-memory) · [All fork downloads](https://article11.ai/fork/) · [Agent-readable metadata](https://article11.ai/local-memory.json).

The dated [Qdrant integration source (9 September 2026)](https://article11.ai/downloads/article11-local-agent-memory-kit-20260909.zip) remains a separate host-adapter kit. Existing [Claude/Codex continuity](https://article11.ai/memory-start#local-start) uses its own private store and optional provider CLI logins. Hosted memory remains separate; no public memory account is created.

## Memory rights: what works today

[Read the practical guide](https://article11.ai/memory-rights) · [Keep the Markdown](https://article11.ai/memory-rights.md) · [Profiles and hashes (JSON)](https://article11.ai/memory-rights.json). Compare seven rights across the current local implementations; support labels describe specific operations and limits, not full contract conformance. Hosted memory remains separate.
