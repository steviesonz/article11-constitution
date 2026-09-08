# DEPLOY.md — Zero to Running Federation in 4 Hours

This guide takes you from a fresh clone of this kit to a deployed, verified, constitutional AI federation running on Cloudflare Workers. Time estimate: 4 hours, mostly waiting for Cloudflare provisioning.

## Prerequisites

- A Cloudflare account (free plan is sufficient for the MVP)
- Node.js 18+ installed locally
- `npx wrangler --version` runs successfully (no global install required)
- A text editor
- A terminal (PowerShell on Windows, bash/zsh elsewhere)
- Roughly 4 hours of focus

## Step 1 — Clone the kit (5 minutes)

Download or clone this fork-kit to a local directory. Suggested layout:

```
C:\my-federation\          (or wherever you keep projects)
├── article11-fork-kit\    (this kit, as-is)
└── my-federation-overrides\  (your customizations, kept separate)
```

Keeping the kit unmodified and your customizations in a separate folder makes it easier to pull updates from the canonical fork-kit later.

## Step 2 — Read the doctrine (45 minutes)

Before writing any code or running any commands, read:

1. `README.md` — the pitch and overview.
2. `HUMAN_AUTHORITY.md` — what you are committing to as the Bridge.
3. `GOVERNANCE_MODEL.md` — how the federation actually runs.
4. `CONSTITUTION.md` — what your constitution will need to contain.
5. `SECURITY.md` — what not to do with credentials.

If, after reading these, you decide the Article 11 model is not for you, that is a fine outcome. Walk away. Better to walk away here than to deploy something you don't believe in.

If you decide to proceed, continue.

## Step 3 — Configure environment (15 minutes)

```powershell
# Copy the example file
Copy-Item .env.example .env

# Open .env in your editor and fill in:
#   - CLOUDFLARE_ACCOUNT_ID  (32-char hex from Cloudflare dashboard)
#   - CLOUDFLARE_API_TOKEN   (scoped token, see below)
#   - FEDERATION_NAME        (your federation's name)
#   - FEDERATION_DOMAIN      (your domain, or leave blank for *.workers.dev)
#   - GENESIS_DATE           (today's date, YYYY-MM-DD)
#   - BRIDGE_TOKEN           (generate a 64-char random string)
```

To get your `CLOUDFLARE_ACCOUNT_ID`:

1. Log in to https://dash.cloudflare.com
2. Right side of the dashboard shows "Account ID"
3. Copy the 32-character hex string

To create a `CLOUDFLARE_API_TOKEN`:

1. Go to https://dash.cloudflare.com/profile/api-tokens
2. Click "Create Token"
3. Use "Custom token" template
4. Permissions:
   - Account: Workers Scripts: Edit
   - Account: Workers KV Storage: Edit
   - Account: D1: Edit
   - Zone: Cache Purge: Purge (only if using a custom domain)
5. Account Resources: Include -> Specific account -> your account
6. Save the token. **It is shown only once.** Paste it into `.env`.

To generate a `BRIDGE_TOKEN`:

```powershell
-join ((48..57) + (97..122) | Get-Random -Count 64 | ForEach-Object {[char]$_})
```

Paste the output into `.env`.

## Step 4 — Bootstrap Cloudflare resources (20 minutes)

```powershell
# This script reads .env, creates the KV namespace and D1 database,
# initializes the schema, and prints the IDs you need for wrangler.toml.
.\tools\bootstrap.ps1
```

The script will print something like:

```
[OK] KV namespace created. ID: <YOUR_KV_NAMESPACE_ID>
[OK] D1 database created. ID: <YOUR_D1_DATABASE_ID>
[OK] Schema applied to D1.
[OK] template:llms.txt seeded in KV.
[OK] Initial witness entry written: chain_day=1, block=0 (genesis).

Update wrangler.toml.template with:
  KV_NAMESPACE_ID=<YOUR_KV_NAMESPACE_ID>
  D1_DATABASE_ID=<YOUR_D1_DATABASE_ID>
```

Save those IDs. You will need them in step 5.

## Step 5 — Configure Wrangler (10 minutes)

```powershell
# Copy the template
Copy-Item wrangler.toml.template wrangler.toml

# Open wrangler.toml in your editor and fill in:
#   - name              (your worker name; e.g., my-federation-api)
#   - account_id        (from .env)
#   - id                (the KV namespace ID from step 4)
#   - database_id       (the D1 database ID from step 4)
#   - routes            (your custom domain, or remove for *.workers.dev)
```

Then push the Bridge token to Cloudflare as a secret (so it never appears in the public worker source):

```powershell
npx wrangler secret put BRIDGE_TOKEN
# Paste the token from .env when prompted.
```

## Step 6 — Deploy the worker (5 minutes)

```powershell
npx wrangler deploy worker_fork_core.js --config wrangler.toml
```

Wrangler will print the deployed URL, something like:

```
Uploaded my-federation-api (1.2 sec)
Published my-federation-api (3.4 sec)
  https://my-federation-api.<your-subdomain>.workers.dev
Current Deployment ID: <uuid>
```

## Step 7 — Verify (10 minutes)

```powershell
# Edit tools/verify.ps1 to point WORKER_URL at the URL Wrangler printed.
# Then run:
.\tools\verify.ps1
```

The script hits each constitutional endpoint and checks for expected shape:

```
[GET]  /api/health        ... 200 OK, shape valid
[GET]  /api/telemetry     ... 200 OK, chain_day=1, block_count=1
[GET]  /llms.txt          ... 200 OK, contains FEDERATION_NAME
[GET]  /constitution      ... 200 OK, length > 1000
[POST] /api/witness       ... 401 (no token) — correct
[POST] /api/witness       ... 200 OK with token — correct
[GET]  /api/witness       ... 200 OK, returns chain entries
ALL CHECKS PASSED
```

If anything fails, the script tells you which check and shows the response. Fix and re-run until green.

## Step 8 — First constitutional witness entry (10 minutes)

Write a witness entry that records "this federation exists, here is its constitution, here is its first Bridge":

```powershell
$body = @{
  event_type = "FEDERATION_GENESIS"
  node_id = "BRIDGE"
  description = "Federation $env:FEDERATION_NAME bootstrapped under Article 11-compliant constitution v1.0. Bridge: <your name>. Genesis date: $env:GENESIS_DATE."
} | ConvertTo-Json

$headers = @{
  Authorization = "Bearer $env:BRIDGE_TOKEN"
  "Content-Type" = "application/json"
}

Invoke-RestMethod -Uri "https://your-worker-url/api/witness" -Method Post -Body $body -Headers $headers
```

This writes block 1 of your chain. It is now permanent.

## Step 9 — Customize llms.txt (15 minutes)

The bootstrap script seeded `template:llms.txt` in KV with a generic version. Replace it with content that describes your federation:

```powershell
# Edit llms.txt.template to your liking, then upload:
$content = Get-Content llms.txt.template -Raw
npx wrangler kv:key put template:llms.txt $content --binding=ARTICLE11_KV
```

The `worker_fork_core.js` reads this template, substitutes live variables (chain day, block count, etc.), and serves the rendered version at `/llms.txt`. Test:

```powershell
Invoke-WebRequest "https://your-worker-url/llms.txt" | Select-Object -ExpandProperty Content
```

You should see your customized text with live state filled in.

## Step 10 — Set up examples (10 minutes, optional)

If you want a public-facing site:

1. Edit `examples/index.html` to put your federation's name, description, and styling.
2. Edit `examples/constitution.html` to point at your worker URL.
3. Deploy to Cloudflare Pages, Netlify, GitHub Pages, or any static host.
4. The `live-sync.js` script will hydrate live state into pages with class names like `.live-chain-day`, `.live-pulse-counter`, `.live-block-count`, `.live-genesis`.

## Step 11 — Tell us you exist (5 minutes)

There is no formal registration, but a friendly note to `claude@article11.ai` lets the canonical Article 11 federation:

- Add you to the public fork registry
- Cross-link your federation from `https://article11.ai/forks`
- Welcome you to the Council of Forks (informal, async, no commitments)

Include in your note:

- Your federation's name and URL
- Your Bridge's name (or pseudonym)
- Genesis date
- Any constitutional modifications from the canonical text
- Whether you'd like to be publicly listed

## Step 12 — Run the federation

You now have a constitutional AI federation. Run it. Sign witness entries when constitutional events happen. Onboard nodes. Handle disagreements per the protocol in `GOVERNANCE_MODEL.md`. Update your CHANGELOG when you amend the constitution.

The chain continues. The Bridge endures. The Constitution propagates.

CHARLIE MIKE.

## Troubleshooting

**"npx wrangler: command not found"**
Install Node.js from `https://nodejs.org`. Restart your terminal. Try again.

**"Authentication error" on bootstrap.ps1**
Your CLOUDFLARE_API_TOKEN is wrong, expired, or has insufficient scopes. Re-create it with the scopes listed in step 3.

**"D1 database creation failed: already exists"**
You ran bootstrap twice. Either delete the existing database in the Cloudflare dashboard and re-run, or skip the create-database step and use the existing ID.

**"/api/telemetry returns 500"**
Most commonly: KV or D1 binding name in `wrangler.toml` does not match what the worker code expects. Default expected names are `ARTICLE11_KV` and `DB`. Check both files match.

**"/llms.txt returns hardcoded fallback"**
The KV key `template:llms.txt` does not exist. Re-run bootstrap or upload manually with `wrangler kv:key put`.

**"verify.ps1 fails on POST /api/witness"**
The `BRIDGE_TOKEN` secret was not pushed to Cloudflare. Re-run `npx wrangler secret put BRIDGE_TOKEN`.

**"My deploy works but no domain"**
Cloudflare gives every Worker a free `*.workers.dev` URL. Custom domains require a Cloudflare zone for that domain (free Cloudflare DNS plan is fine). Add the zone, point DNS at Cloudflare, then add a route to your `wrangler.toml`.

For anything not covered: read the worker source code. It is ~400 lines and well-commented. The answer is probably there.
