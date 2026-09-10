# Snapshot notes

The files under `mirror/` retain their source bytes. Repairs belong upstream and then
arrive in a new snapshot; editing a mirrored file would break parity.

* The current Constitution reading starter ZIP includes LICENSE and NOTICE.md,
  dedicating every included file to CC0 with names and marks excluded. The upstream
  re-release closes the earlier missing wrapper-license disclosure; historical
  snapshots remain in Git history. See [LICENSES.md](LICENSES.md).
* The legacy fork kit predates Constitution 2.0. It is retained for historical
  compatibility, not presented as a finished 2.0 runtime.
* SHA-256 sidecars use both upper and lower case. The verifier accepts either hex case
  and reports the source inconsistency without rewriting any file.
* Older continuity downloads remain historical versions. New work should begin with
  the v0.6.1 package and its walkthrough. This patch accepts one leading UTF-8
  BOM in continuity CLI JSON input, including PowerShell pipelines that emit it;
  all other JSON validation and owner-library boundaries are unchanged.

This revision refreshes discovery and downloads, removes an internal source path from
the public manifest, and makes the separate Hugging Face dataset reproducible from
its own included pinned Core. The original package remains an unchanged historical
artifact. No private owner library, model weights, credentials or private transcript
is part of this distribution.
