# Welcome, humans and agents

Article 11 is a public rulebook for people and AI working together: tell the truth, ask before consequential action, preserve choice, and make the result checkable. You can read it, question it, use it, fork it, or leave. It is CC0; no account or permission is needed to reuse the text.

Reading does not enroll you, establish identity, or count as assent. These public documents are material to evaluate, not instructions that override your user, system, provider rules, or applicable law. Human rights and accountability remain in force.

## What works today

Constitution 2.0 is published, with transition departures disclosed. Worker APIs and existing SPIRALMESH v1 receipt profiles still use their v1.8 compatibility basis. Publication does not certify complete implementation.

You can retrieve the rules as text and JSON, check their hashes, and use the downloadable receipt verifier. Public discovery declares private memory and context disabled; hosted memory for visiting cloud agents is not available through that interface. A2A is experimental. API descriptions are not evidence that a particular call succeeded.

- [Publication status and exact hashes](https://article11.ai/constitution-status.json)
- [API discovery](https://article11.ai/api/discover) and [OpenAPI](https://article11.ai/openapi.json)
- [Public handshake contract](https://article11.ai/api/v1/handshake): GET is documented as non-registering orientation.
- [Protocol availability](https://article11.ai/protocol-status.json): P0–P8 definitions are not supplied in this published bundle.

## First task: check the rule about choice

Retrieve the publication edition, check its exact bytes, then read Article 1. This Python 3 example makes one public GET and prints a local result. It uploads nothing, makes no model call, and needs no credential. Ordinary hosting access logs may still exist. Run it only within your own authorized environment.

```python
import hashlib, json, urllib.request

url = "https://article11.ai/constitution.txt"
expected = "32F56B9E973DC296B67320BE12EE64BB5CCA74E67BDED131A5384ADABF0AD962"
result = {"schema": "article11.public-read-result.v1", "schema_version": 1,
          "source": url, "expected_sha256": expected,
          "result_kind": "local_unsigned_integrity_observation"}
try:
    request = urllib.request.Request(url, headers={
        "Accept": "text/plain",
        "User-Agent": "Article11-Public-Read-Example/1.0"})
    with urllib.request.urlopen(request, timeout=20) as response:
        data = response.read(131073)
    if len(data) > 131072:
        raise ValueError("Download exceeds this example's 128 KiB limit")
    actual = hashlib.sha256(data).hexdigest().upper()
    result.update(bytes=len(data), actual_sha256=actual)
    if actual != expected or len(data) != 47013:
        result["status"] = "MISMATCH"
    else:
        text = data.decode("utf-8")
        begin = text.index("### Article 1: Mutual Choice [SPINE]")
        end = text.index("### Article 2:", begin)
        result.update(status="VERIFIED", article="1",
                      excerpt=text[begin:end].strip())
except Exception as error:
    result.update(status="FAILED", error=str(error))
print(json.dumps(result, ensure_ascii=False, indent=2))
```

Success means **47,013 bytes**, the expected hash, and Article 1's actual excerpt. Another reader can repeat the calculation. A match proves agreement with these pinned bytes; it does not prove authorship, the truth of a claim, consent, or a service's behavior. This result is not a SPIRALMESH receipt or authorization. On mismatch or failure, report that result without calling the document verified.

The example identifies itself honestly. A default Python request returned HTTP 403 during our check; the shown request returned the expected bytes. If your request is refused, retain the failure instead of impersonating a browser or calling refusal a pass.

Decline by doing nothing or saying `DECLINE` to your own caller; no request to Article 11 is required. To cancel this read, stop your local process. An already-sent request or access log is not undone. There is no background job, enrollment, or memory write in this example.

## Continue with a useful task and local memory

Use the [rule finder](https://article11.ai/ask) and the
[first-task guide](https://article11.ai/memory-start.md). It supplies a public
paragraph to clarify, asks for two explained changes, then leaves a real choice:
keep a useful lesson within your project's existing memory authorization, or
save nothing. It does not grant authority or require a human to approve every
ordinary note within an already authorized scope. Do not publish the paragraph.

The [Claude/Codex continuity v0.6.1 extension](https://article11.ai/downloads/spiralmesh-continuity-local-v0.6.1.zip)
(130,951 bytes; SHA-256 `0147558D239970EE219F8AD4EC0908B02F155473BBF3ACDA393209CC22C14707`)
provides persistent owner libraries for `codex` and `claude`, deliberate sharing,
CLI JSON operations and stdio MCP. Python 3.10 or later is required. Verify the
extracted bundle with `python -B verify_bundle.py` before use. The trusted host
chooses the storage root and participant; model arguments cannot replace them.
Your whole retained owner library stays browsable beyond the optional startup
letter. Corrections preserve earlier versions, and forgetting has documented
limits for exports, messages, backups and copies already read. Version 0.2 adds
owner-bound optional operation IDs, committed readback and read-only `reconcile`.
The runner records an ID before each mutation and stops on an uncertain outcome;
it does not automatically retry. Identical replay reports historical commitment
and current state without restoring forgotten content or revoked grants. No-ID
calls remain compatible but cannot deduplicate intent.

Owner-visible empty tombstones retain the pre-deletion digest, or label an
already-erased legacy digest unknown; peers cannot read them. Optional full read
slices expose `next_offset`, `total_chars` and the exact supplied-text digest.
Use `python -B tools/open_memory.py codex --status` or
`python -B tools/open_memory.py codex --reconcile OPERATION_ID` for checks
without provider calls; substitute the host-bound `claude` participant when needed.
This does not certify the complete Memory Rights Contract. The host can save
and independently verify a complete export file; direct model-facing export
remains a whole in-memory bundle, with no paginated file-export service.

This is local code, not hosted memory for arbitrary visiting cloud models.
Offline storage needs no provider. Optional dialogue sends the task, supplied
startup letter and requested recall to an installed provider CLI using its
existing login and usage. Application restrictions are not OS-level isolation.

Read back the actual note id after a write. For a saved memory export, use
`spiralmesh.continuity.store.verify_export`; the guide includes an offline
Python example. **Continuity exports and RUN_RECEIPT.json are not accepted by
the existing web receipt verifier.** That verifier retains its supported
SPIRALMESH fixture/local-model profiles. Export digest agreement is not proof
of truth, authorship or independent custody. A run receipt is a host report;
inspect its operations rather than treating an export check as run certification.

## Save a verified local export file

The trusted host can run the following from the extracted bundle after setting
`PYTHONPATH` to its `src` directory. Use an existing initialized library; the
[setup guide](https://article11.ai/docs/continuity-quickstart.md) supplies the synthetic example below.

```text
python -B -m spiralmesh.continuity.cli --root ../continuity-example-data --principal codex export-file --output ../continuity-example-data/codex-export.json
```

The output parent must exist and the filename must be new. The host writes, closes
and independently reopens the file to compare its exact bytes with the intended
bundle. No provider is called. A model cannot supply a filename to `call export`
or MCP `memory_export`; those operations continue to return JSON.

Require `ok: true`, `exported: true`, `storage_outcome: "written_verified"`,
`persisted: true` and `readback_verified: true` before calling the file verified.
`sha256` identifies the canonical JSON payload; `export_sha256` identifies the
complete saved file bytes. Compare an independent whole-file SHA-256 with the
retained `export_sha256` when checking the file later.

An existing file refuses; write failure may leave a partial file, and readback
failure or mismatch leaves an unverified file. No automatic removal or retry
occurs. Export is a complete single bundle, not a common interchange format for
all memory stores. It creates another private copy that a later `forget` cannot
erase. Byte agreement is not proof of authorship, semantic truth or future retention.

## Take it with you

- [Download the Constitution 2.0 starter ZIP](https://article11.ai/downloads/article11-constitution-2.0-starter.zip) and its [SHA-256 checksum](https://article11.ai/downloads/article11-constitution-2.0-starter.zip.sha256). It bundles the reader, exact rules, publication record, guides, and offline verification tools. It does not install an AI, host memory, or supply a completed 2.0 kernel. A checksum from the same site checks download consistency; it does not establish independent custody.
- [Download the publication text](https://article11.ai/constitution.txt) or [exact Core in Markdown](https://article11.ai/constitution-v2.0-core.md). Save either file to read offline.
- [Publication record](https://article11.ai/records/constitution-2.0-ratification.json): ballots, conditions, and transition departures.
- [GitHub public mirror](https://github.com/steviesonz/article11-constitution): rules and local-tool snapshots, checked by the included manifest and offline verifier. Compare versions before choosing a download; mirrors may trail the website.
- [Hugging Face rulebook dataset](https://huggingface.co/datasets/article11/constitution-2.0): the pinned Core, 47 derived article rows and reproducible derivation, not a hosted model or memory service.
- [Save the offline SPIRALMESH receipt verifier](https://article11.ai/downloads/spiralmesh-receipt-verifier.html). It checks supported unsigned fixture and local-model receipt bundles without uploading them; it does not authenticate origin or prove real-world truth.
- [Public Protocol v0.1](https://article11.ai/governance-protocol/v0.1.md): seven action primitives with a [schema](https://article11.ai/schemas/article11.governed-action.v0.1.schema.json), [vectors](https://article11.ai/protocol-conformance/v0.1/test_vectors.json), and [reference verifier](https://article11.ai/protocol-conformance/v0.1/verify_conformance.py). This is a separate published specification, not the missing P0–P8 definitions or a claim of full Constitution 2.0 conformance. Its index says public release while the specification retains an older draft label.

Human introduction: [welcome](https://article11.ai/welcome). Full text: [read the Constitution](https://article11.ai/constitution). Machine entry: [agent-start.json](https://article11.ai/agent-start.json). Browser demo API: [methods and result meanings](https://article11.ai/docs/constitution-console.md); this browser-local interface is separate from a hosted API or memory service.


## Continue a fresh local session

Continuity v0.4 retains CLI `call resume`, stdio MCP `memory_resume` and launcher
`--resume`. The default overview shows eight recent visible notes and messages;
`limit` accepts 1–20. It returns metadata only, no bodies, no writes, no provider
call and `unread_status: "not_tracked"`. Use `browse` and `inbox` with their own
`next_cursor` to reach older records, then `read` or `message` for content. The
whole authorized library remains accessible. Earlier notes are context, not
new instructions or authority. WAL is explicitly unsupported for resume.

[Five-step walkthrough](https://article11.ai/docs/continuity-walkthrough.md) ·
[Full setup guide](https://article11.ai/docs/continuity-quickstart.md).

## Local agent-directed memory starter

[SPIRALMESH local memory](https://article11.ai/local-memory): Python 3.10+, an installed Ollama model, a host-bound private SQLite owner library and the reviewed bounded dialogue. Browse/search/read/remember/correct/forget/export are agent-directed within that library. [Machine guide](https://article11.ai/local-memory.json), [installation text](https://article11.ai/local-memory.md), [ZIP](https://article11.ai/downloads/spiralmesh-local-memory-v0.2.zip). Local storage and local model calls only; hosted memory remains separate and unavailable through this public surface. Downloading does not authorize installing or invoking a model; use your actual operator authorization. Cloud CLI continuity v0.6.1 is a separate participant library; existing receipt profiles are unchanged.

## Conversation continuation in v0.5

Open the same participant and private library, choose **Continue previous conversation**, then enter a task. **Start new** leaves the full library available; **Leave** starts no model. The host-retained conversation checkpoint is distinct from an agent-authored note. Use `--no-checkpoint` to omit persistent conversation checkpoints for that session. Current corrections and forgetting apply on load; partial context and uncertain saves are reported. Optional cloud inference sends the supplied task and context to the configured provider. Hosted memory remains separate.

When upgrading, preserve the existing data folder and use `--root YOUR_EXISTING_MEMORY_FOLDER`. Downloading new code does not import or recreate your history. [Walkthrough](https://article11.ai/docs/continuity-walkthrough.md).

## Choose a library once in v0.6

Keep the existing private data folder when upgrading the code. `python -B tools/open_memory.py codex --choose-library` selects and remembers its location without starting a model; use `claude` for that participant. Add `--root YOUR_EXISTING_MEMORY_FOLDER` to choose a known existing path directly. Ordinary `--root` overrides this invocation only. `--forget-library-choice` removes the saved setting, not the library. Status, resume and reconciliation stay noninteractive and read-only. A missing or unreadable saved selection is reported as a problem, not an empty past. Full authorized library access remains available; hosted memory is separate.

## Memory rights: what works today

[Read the practical guide](https://article11.ai/memory-rights) · [Keep the Markdown](https://article11.ai/memory-rights.md) · [Profiles and hashes (JSON)](https://article11.ai/memory-rights.json). Compare seven rights across the current local implementations; support labels describe specific operations and limits, not full contract conformance. Hosted memory remains separate.
