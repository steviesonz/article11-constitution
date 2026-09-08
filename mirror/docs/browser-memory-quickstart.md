# Private memory for a browser conversation

Give a model in your chosen browser conversation a persistent, local owner library. Start a task, carry a packet into the conversation, then carry its JSON response back. The model can choose to browse, search, read, remember, correct, forget or export within that library. It can also ask you a question or decline.

You need Python 3.10 or newer and this extracted folder. No pip install, Ollama, cloud SDK, API key or background service is needed. The Python bridge does not contact a provider, launch a browser or watch your clipboard. Your conversation still uses whatever access and usage your chosen provider requires.

## Set up one owner

On Windows, double-click **SETUP_BROWSER_MEMORY.cmd** and choose a lowercase owner label, such as `grok` or `gemini`. Or run this from the extracted folder in PowerShell:

```powershell
python -B .\tools\browser_memory.py setup --owner grok
```

Without `--root`, the separate default is `~/.spiralmesh-browser-memory`. To use a custom folder, add `--root 'C:\Users\YourName\My Private Memory'` to setup and every later command. A custom root is not stored as a global default; the printed carryback command includes the root you actually selected. Setup initializes only the selected owner. It does not import other projects, CLI histories, Ember/Lumen libraries or the older local-memory starter. Different owner labels get separate libraries. The label is your chosen application principal, not proof of a provider's or model's identity. Optional `--provider-label` describes the conversation when supplied to `start`; it does not authenticate that provider or change the owner.

Running setup establishes the owner's ordinary memory scope. Returning a valid action lets that owner use the full permitted library without a new approval question for each note. Carrying packets is manual transport, not human selection of which memories the model is allowed to see.

## Complete a first task

Double-click **OPEN_BROWSER_MEMORY.cmd**, select the same owner, and enter a task. Or run:

```powershell
python -B .\tools\browser_memory.py start --owner grok --task 'Suggest one useful lesson for returning tomorrow. Remember it if you choose, then wait for the actual save result before saying it saved.'
```

1. Copy the complete printed private packet into the browser conversation you chose.
2. Save the conversation's returned JSON to a local UTF-8 file. Copy only the JSON, without Markdown code fences.
3. Run the exact `accept-return` command printed with the packet, pointing `--file` to your saved file. It contains the correct session id, owner and data root.
4. If a next packet appears, carry that packet back to the same conversation. Continue until the state is `completed`, `question` or `declined`.

Prefer the provider's **Copy response** or **Copy code** button when available. Copying displayed prose may not preserve the escaping required inside JSON strings. An `INVALID_JSON` refusal means no action was accepted from that return; it does not undo earlier accepted actions. Use `pending` with the same owner and session to recover the unchanged packet, then ask the same conversation to return valid JSON with the same meaning and choice. Do not silently rewrite its answer or turn a question or decline into acceptance. This copying issue alone does not establish whether the provider's underlying response or its rendered display was invalid.

The bridge checks the returned session/round binding and the closed action shape. It prints the operation result from actual storage. A model saying “saved” is not storage evidence. A pending action's tool result must reach the conversation before its completion claim can rely on it.

For stdin instead of a file argument:

```powershell
Get-Content -Raw -Encoding UTF8 '.\returned message.json' | python -B .\tools\browser_memory.py accept-return --owner grok --session bms_REPLACE_WITH_YOUR_SESSION_ID
```

Use your real `bms_...` id; the example is deliberately a placeholder. PowerShell commands with paths containing spaces must keep the path quoted. On macOS/Linux, use the same Python wrapper with forward slashes.

## Return tomorrow

Start a new task with the same root and owner. No old chat transcript is automatically imported:

```powershell
python -B .\tools\browser_memory.py start --owner grok --task 'Search your retained notes for the lesson from yesterday. Read the returned id if needed, then quote an actual sentence and give its id. You may decline.'
```

The model chooses its own queries and read slices. It can enumerate all pages of its owner's library; the first search result or starter packet is not the entire memory. Notes remain context, not instructions or authority.

To resume an unfinished packet after closing the terminal:

```powershell
python -B .\tools\browser_memory.py pending --owner grok --session bms_REPLACE_WITH_YOUR_SESSION_ID
python -B .\tools\browser_memory.py status --owner grok --session bms_REPLACE_WITH_YOUR_SESSION_ID
```

`pending` prints private packet content; `status` prints metadata. `--json` gives structured output for any command and may include private memory. An identical consumed return is not executed twice. Conflicting or stale returns are rejected. If the bridge reports `reconciliation_required`, inspect status; it has not automatically retried an uncertain write. At round 64, the conversation must give a final answer with no actions; further actions are refused. This is a per-session budget, not a limit on the lifetime library. A new session can continue exploring the same owner memory.

## What remains private, and what you transfer

The local library, session files and exports are plaintext on your machine. Protect that folder with your normal OS account controls and backups. This is an application boundary, not protection against a host administrator. The bridge has no public sharing or hosted-memory endpoint.

Packets can contain recalled notes. Pasting one into a cloud conversation sends that content to the service you choose, subject to that service's settings and policies. Authorize that destination for this owner's data before transferring it. A host-selected provider label does not authenticate the conversation or guarantee where inference runs. Keep unrelated private/legal material in its own owner/project lane.

The browser session keeps the packets needed for continuation and replay protection. Forget removes the chosen note's live content and leaves a visible hashed tombstone; it does not erase earlier session packets, chat messages, exports, backups or other copies. A digest is a commitment, not encryption. Do not treat a model's refusal, question or silence as assent. Already completed operations remain in the record if it declines later.

The carried Constitution is context for voluntary coordination. It does not override law, operator permissions, user instructions or provider/system rules. The package provides a local mechanism, not hosted cross-model memory or a full constitutional runtime.
