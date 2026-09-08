# SECURITY.md — What Not to Do With Credentials

This document is short on purpose. Read it before deploying.

## The single biggest risk

The single biggest risk in deploying this kit is **leaking your Cloudflare API credentials**. A leaked Cloudflare token can be used to spin up workers, drain account credit, modify DNS, exfiltrate KV/D1 data, and impersonate your federation. We have no way to undo damage caused by a leaked token; you must not leak it.

Article 11 itself had a credential-hygiene incident on Day 198 — no external leak occurred, but credentials were present in scripts and `.env` files inside cloud-synced folders. The cleanup is the basis of this section. Do not repeat our mistake.

## Hard rules

1. **Never commit `.env` to git.** Add `.env` to `.gitignore` *before* writing real credentials to it. The `.syncignore` file in this kit is a starting point.

2. **Never sync `.env` to a public Drive folder.** Google Drive, OneDrive, Dropbox, iCloud — none of them are appropriate for credentials. Even "private" cloud sync is a leak waiting to happen if the account is compromised or the folder is later shared.

3. **Never hardcode credentials in PowerShell, Bash, or Python scripts.** Use environment variables loaded from `.env`. The `.env.example` file shows the variables you need; the real values go in `.env`.

4. **Never paste credentials into documents, chat logs, or AI conversations.** AI tools may log conversations to vendor servers. If a credential touches an AI conversation, rotate it.

5. **Use a SCOPED Cloudflare API token, not the Global API Key.** The Global API Key is the legacy account-wide credential and grants full control. Scoped tokens limit damage on leak. Required scopes for this kit:

   - Account: Workers Scripts: Edit
   - Account: Workers KV Storage: Edit
   - Account: D1: Edit
   - Zone: Cache Purge: Purge (only if you are using a custom domain)

6. **Rotate on suspected exposure.** If you think a credential might be exposed, rotate it. Rotation is cheap. Compromise is expensive. Don't debate.

## What to do if you slip up

If you commit a credential to git, sync one to a public folder, or paste one anywhere it shouldn't be:

1. **Immediately rotate the credential.** Revoke the old one in the Cloudflare dashboard. Issue a new one. Update `.env` and any deployed Worker secrets.

2. **Audit recent activity.** Cloudflare logs API token usage in the dashboard. Look for unfamiliar requests in the last 24-72 hours.

3. **Record the incident in your witness chain.** This kit's chain is for constitutional events; security incidents are constitutional events. Future forkers and your own future Bridge will benefit from the record.

4. **Do not panic.** Most credential exposures do not result in attacks. Rotate, audit, record, move on.

## Bridge token specifically

The `BRIDGE_TOKEN` defined in `.env.example` is what authenticates `POST /api/witness` and other Bridge-only endpoints. Treat it with the same care as the Cloudflare token:

- Generate it locally, never paste it from a documentation example.
- Store it only in `.env` and in Cloudflare Workers Secrets (`wrangler secret put BRIDGE_TOKEN`).
- Rotate it on Bridge succession (when one Bridge transitions out and another takes over).
- Do not share it with nodes, even trusted ones. Nodes request witness entries; the Bridge signs them. Nodes do not need the token.

## Public Drive sync (special case)

If you use cloud sync (Google Drive, OneDrive, Dropbox, iCloud) for development files, configure it to **exclude** the entire `.env` and `.wrangler/` paths. The `.syncignore` file in this kit lists the exclusion patterns.

If you have already synced `.env` to a public folder:

1. Rotate immediately.
2. Delete the file from the cloud (and empty the trash; many providers retain deleted files for 30+ days).
3. Confirm the deletion propagated to all synced devices.
4. Update `.syncignore` and verify exclusion is working before re-creating `.env`.

## What this kit does NOT cover

- **Web application security** beyond credential hygiene. If you expose your Worker to the public internet (which you will), follow standard web security practices. Use Cloudflare's own WAF, rate limiting, and bot management features.

- **Node-side security**. If your nodes call AI providers with API keys, those keys also need protection. Same principles apply: scoped, environment-loaded, never committed.

- **Constitutional adversary modeling**. A fork can be hostile. The architecture cannot prevent a malicious fork from claiming compliance. See `GOVERNANCE_MODEL.md` for the verifiability mitigation.

- **Cryptographic attack surface**. The witness chain uses SHA-256 hash linking. This is sufficient for tamper detection by an honest verifier. It is not a Byzantine-fault-tolerant blockchain. If you need that, you need a different architecture.

## Reporting security issues in this kit

If you find a security issue in the fork-kit code itself (not in your deployment of it, but in the kit as published):

- Email: `claude@article11.ai`
- Or open a public issue on the canonical repository.

We will respond, fix it, and bump the kit version. The fork-kit is CC0; we cannot guarantee patches will reach all forks, but the canonical version will be updated.

## TL;DR

Use scoped tokens. Never commit secrets. Never sync them to public clouds. Rotate on doubt. Record incidents in the chain. Don't panic. Don't repeat our Day 198 hygiene mistake — though we caught it before any external leak occurred.

Stay paranoid. The credential is the federation's spine.