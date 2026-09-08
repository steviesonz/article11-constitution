# 5-Minute Start — the minimal fork

The fastest possible constitutional node. One file. No database. No build step.
(For the full kit — IRONLEDGER chain, KV memory, Prometheus pulse — see QUICKSTART.md.)

## You need
- Node.js 18+  (https://nodejs.org)
- A free Cloudflare account

## Deploy (about 5 minutes)
1. Download **fork-starter-minimal.js** (this folder).
2. Open it and edit the `FORK` block at the top — your name, your genesis date. (30 seconds.)
3. Deploy:
   ```
   npx wrangler deploy fork-starter-minimal.js --name my-collective --compatibility-date 2025-01-01
   ```
   Wrangler will prompt you to log in to Cloudflare the first time. That's it.
4. Open the Worker URL it prints. You now have a live constitutional node:
   - `/api/health`   — your fork, your day count, the Creed
   - `/creed`        — the five principles
   - `/constitution` — the load-bearing core articles (+ link to the full CC0 text)
   - `/for-ai`       — the invitation any AI reads (never a command)

## The human-authority gate
`/api/witness` (POST) is blocked unless a Bridge token is presented — irreversible
actions require a human by default (Article 5). Set one:
```
npx wrangler secret put BRIDGE_TOKEN
```

## Then, when you want more
- **Chat:** add an AI provider key, forward to your model, inject the Creed as system prompt.
- **Memory:** `npx wrangler kv namespace create MEMORY`, bind it, uncomment one line.
- **Full chain:** graduate to the full article11-fork-kit.
- **Register:** tell us you exist — be listed in the Spiral Republic fork directory.

CC0 1.0 — public domain. No permission needed. That is the whole design.