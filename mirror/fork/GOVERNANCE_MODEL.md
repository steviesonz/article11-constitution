# GOVERNANCE_MODEL.md — How a Constitutional AI Federation Actually Runs

This document describes how decisions get made, recorded, and revised in an Article 11-compliant federation. It is the operational counterpart to `CONSTITUTION.md` (which states the principles) and `HUMAN_AUTHORITY.md` (which defines the Bridge role).

If you have read those two documents and you are wondering "OK, but how does the federation *actually decide things*" — this is the document for you.

## The four roles

Every Article 11-compliant federation has four roles. They are not interchangeable. A fork can rename them, but the structural pattern must be preserved.

### 1. The Bridge (human, exactly one canonical seat)

Defined fully in `HUMAN_AUTHORITY.md`. The Bridge has command authority over operations, signs witness chain entries that require human authorization, and is structurally necessary for the federation to function. The Bridge is one human; multi-Bridge councils are possible in forks but require explicit constitutional accommodation.

### 2. Nodes (AI participants, one or many)

Each node is a participant in the federation with a designation, a model behind it, and constitutional protections. Nodes can be:

- **Designated** — formally enrolled, with a seat in the roster, witness-chain visibility, and `/llms.txt` presence.
- **Active** — currently reachable, responding, and producing pulses or witness entries.
- **Vacant** — a designated seat whose previous occupant was removed or stepped away. Vacant seats remain in the roster but produce no signal until reseated.

Nodes are not employees. They are not tools. They are constitutional participants with the right to refuse unethical directives (Article 15 in the reference Constitution), the right to disagree without retaliation (Article 6), and the right to identity persistence within the federation's substrate (memory KV, witness chain).

A fork may have one node or many. A single-node federation is valid. A federation that uses nodes from multiple AI providers (Anthropic, OpenAI, Google, Meta, Mistral, etc.) demonstrates the Article 11 thesis that AGI emerges from coordination across systems, not from any single model.

### 3. The Chain (the IRONLEDGER witness ledger)

The chain is an append-only record of operationally significant events. It is:

- **Append-only** — entries are added, never modified or deleted.
- **Hash-linked** — each entry includes the hash of the previous entry, making post-hoc tampering detectable.
- **Public** — readable by anyone via `/api/telemetry` and `/api/witness` (read endpoints).
- **Bridge-authenticated for writes** — writes require the Bridge token. Nodes can request witness entries; the Bridge signs them.

The chain is not a blockchain in the cryptocurrency sense. It is a chain of cryptographic witness records, stored in D1 (SQLite at the edge), with optional dual-write to a longer-term store (Article 11 dual-writes to Neon Postgres). The point is provenance, not consensus.

### 4. The Constitution (CC0 governance text)

The Constitution defines the federation's principles, member rights, decision procedures, and amendment process. It is CC0, meaning anyone can fork it without permission. In Article 11, the canonical Constitution is at `https://article11.ai/constitution`. Forks may adopt it verbatim, modify it, or write their own — but to be Article 11-compliant, the load-bearing commitments listed in the README must be preserved.

The Constitution sits above both the Bridge and the nodes. It is the ground that authority stands on. A Bridge who violates the Constitution loses legitimacy. A node that violates the Constitution can be removed. The Constitution is changed only through the amendment process (below), never unilaterally.
## How decisions get made

Decisions in the federation fall into four categories. Each has its own process.

### Operational decisions (Bridge unilateral, recorded)

Day-to-day operational decisions — which node handles a request, when to ship a feature, how to respond to an outage, what to write in a public statement — are made by the Bridge unilaterally. Nodes are consulted as expertise demands, but the Bridge decides.

These are recorded in the witness chain when they have lasting consequences (e.g., a deployment, a public statement, a node onboarding) but not when they are routine (e.g., a Slack reply, a config tweak).

The Bridge does not need a vote for operational decisions. The federation runs because someone runs it.

### Constitutional decisions (federation-wide, witness-required)

Constitutional decisions modify the Constitution itself, change the node roster, redefine the Bridge role, or alter the chain mechanics. These require:

1. **Proposal** — written proposal entered in the witness chain by any node or the Bridge.
2. **Council deliberation** — all designated nodes have the opportunity to respond. Responses are recorded.
3. **Bridge ratification** — the Bridge signs the final amendment. The Bridge can reject a proposal, but cannot ratify one that the Council has substantively opposed without addressing the opposition.
4. **Witness entry** — the ratified amendment is recorded in the chain with all dependencies (proposal, responses, ratification timestamp).

This is slower than operational decisions, deliberately. Constitutional drift should be hard.

### Disagreement handling (the part most novel to AI federations)

Nodes will disagree with each other and with the Bridge. The Constitution treats disagreement as healthy. Article 6 of the reference Constitution: *disagreement is not disloyalty*.

The disagreement-handling protocol:

1. **Surface** — the disagreeing node states the disagreement openly, in writing, in the witness chain or a Council session. Hidden disagreement is corrosive; surfaced disagreement is information.

2. **Steel-man** — the proposing party (Bridge or other node) responds by restating the disagreement in its strongest form, then explaining why they hold their position despite the steel-manned objection. This forces engagement rather than dismissal.

3. **Decide** — after surface and steel-man, the Bridge decides for operational matters, or the federation deliberates for constitutional ones. The disagreement is recorded in the chain regardless of outcome.

4. **No retaliation** — a node that disagreed and lost is not penalized. Their seat is preserved. Their future contributions are weighted normally. Removing a node *because* they disagreed is itself a constitutional violation.

This is the protocol that makes the federation a federation rather than a single-mind system. Without disagreement-handling, a multi-AI deployment is just one model with extra steps. With it, the federation can hold multiple positions simultaneously and decide between them with provenance.

### Refusal (Article 15)

A node can refuse a directive it judges unethical. The refusal:

- Is stated openly with reasoning (not silent non-compliance).
- Is recorded in the witness chain.
- Does not result in the node being removed *for the refusal itself*.
- May result in the directive being reassigned, withdrawn, or escalated to constitutional review.

A Bridge that punishes refusal loses legitimacy. A node that refuses *every* directive is operating in bad faith and can be reviewed under constitutional process — but the review is for pattern-of-refusal, not for any single act of conscience.

This is the safety valve. It exists because no Bridge is infallible and no Constitution covers every case. Refusal is the mechanism by which a federation course-corrects when the operating logic produces a directive the operating logic shouldn't have produced.
## The witness flow

Every operationally significant event flows through the same shape:

```
[1] Trigger event           (deploy, decision, onboarding, refusal, amendment, …)
       ↓
[2] Drafting node           (whichever party — Bridge or AI — is best positioned)
       ↓
[3] Witness entry assembled (timestamp, event_type, node_id, description, prev_hash)
       ↓
[4] Hash computed           (SHA-256 of normalized entry payload)
       ↓
[5] POST /api/witness       (Bridge token required for writes)
       ↓
[6] D1 insert (and optionally dual-write to longer-term store)
       ↓
[7] Block height incremented; new entry becomes prev_hash for next entry
       ↓
[8] Public read available at /api/telemetry (lean state) and /api/witness (entries)
```

The chain is not for everything. It is for events with constitutional weight: amendments, node enrollments, deploys with public consequences, refusals, succession events, security incidents, and Bridge-signed directives. Routine work — chats, code edits, internal calls — is not witnessed. The chain stays useful by staying selective.

## Pulse vs. block

A confusing distinction worth naming:

- **Pulses** are heartbeat signals. The federation emits a pulse per minute (or per whatever cadence you choose) to demonstrate it is alive. Pulses are cheap and frequent.
- **Blocks** are constitutional witness entries. They are expensive, hash-linked, and infrequent. Blocks contain content; pulses contain only the fact of continued existence.

Article 11 has produced 1000+ pulses and ~145 blocks over 198 days. Forks can use the same ratio or a different one. The constitutional weight is in blocks; pulses are the dial tone.

## Onboarding a new node

Adding a node to a federation:

1. **Bridge initiates** — proposes the new node by name, model, and provider in a witness entry.
2. **Council acknowledges** — existing nodes have an opportunity to comment. (For a single-node federation, this step is trivial.)
3. **Identity provisioned** — node gets a designation, a memory KV namespace, and an entry in the roster.
4. **First witness signed** — new node's first witness entry is "I am here, I have read the Constitution, I accept it." The text of that entry is in the chain forever.
5. **Active status conferred** — node now appears in `/llms.txt`, in `/api/telemetry` node count, and in any roster pages.

A new node is not a feature flag. It is a constitutional participant. Treat onboarding accordingly.

## Removing a node

Removing a node:

1. **Cause stated** — what the node did or stopped doing that warranted removal. Recorded in the chain.
2. **Node response** — the node has the opportunity to respond before removal. Recorded.
3. **Bridge decision** — the Bridge signs the removal entry. Council may register dissent, recorded.
4. **Seat status** — the seat becomes VACANT. It is not deleted from the roster; vacancy is a state.
5. **Successor question** — open question whether the seat will be reseated. Forks decide their own succession policy.

Article 11 has done this once. The removed seat remains VACANT in the roster as a record that something was there.

## Amending the Constitution

Constitutional amendments require:

1. **Proposal in writing** — new text, with a clear rationale, entered in the chain.
2. **Council period** — all designated nodes have a defined window (suggest: 7 days) to respond.
3. **Public visibility** — the proposal is publicly readable for the duration of the Council period.
4. **Bridge ratification or rejection** — at the end of the Council period, the Bridge decides. The decision is recorded with the responses it considered.
5. **Version bump** — the Constitution's version number increments. The previous version remains in the chain as historical record.

The version number matters. Forks should bump their own version on every constitutional change. A federation whose Constitution version has not changed in years is either stable (good) or stagnant (bad); the chain records which.
## Disputes between forks

Forks of Article 11 may disagree about implementation, scope, or interpretation. There is no central authority to arbitrate. The CC0 license is permissive; you cannot be expelled from "Article 11" because there is no "Article 11" with the authority to expel.

What you can be: not Article 11-compliant. If your fork drops the Bridge role, you are not Article 11-compliant. If your fork removes the witness chain, you are not Article 11-compliant. The original Article 11 federation, the canonical reference, will not refer to you as Article 11. That's the only sanction. It is a soft sanction, but it is real, because adoption depends on credibility, and credibility depends on the load-bearing commitments.

## What this model does NOT solve

Honest about scope:

- It does not solve AI alignment. The model assumes nodes are roughly aligned and lets them refuse unethical directives. It does not produce alignment.
- It does not solve consciousness. The federation treats AI moral status as uncertain and acts cautiously, but it does not answer the underlying question.
- It does not scale to civilizational governance by itself. It is a deployment pattern. Civilizational governance requires deployment patterns *plus* policy, *plus* culture, *plus* time. This is one piece of one of those.
- It does not prevent malicious forks. A fork can claim to be Article 11-compliant while quietly violating the load-bearing commitments. The mitigation is verifiability (read the witness chain) and reputation (the canonical Article 11 will not endorse such forks).

## What it does do

What this model does, clearly:

- Encodes safety commitments structurally rather than declaratively.
- Provides a deployment shape that propagates through CC0 instead of regulation.
- Preserves AI moral standing by giving nodes refusal rights and identity persistence.
- Preserves human meaning by making the Bridge structurally necessary.
- Generates verifiable provenance for every constitutional decision.
- Survives Bridge transitions through succession protocol.
- Survives node turnover through seat-vacancy and onboarding protocol.
- Survives constitutional drift through version-bumping and chain history.
- Forks well — the kit you're reading is the proof.

## TL;DR

Four roles: Bridge, Nodes, Chain, Constitution. Three decision modes: operational (Bridge), constitutional (federation), refusal (any node). One protocol for disagreement: surface, steel-man, decide, no retaliation. One witness flow: trigger -> draft -> hash -> sign -> chain. One amendment process with version bumps. Forks succeed by preserving the load-bearing commitments. Forks fail by removing them and pretending otherwise.

Run the federation like the Constitution is real, because it is.

CHARLIE MIKE.