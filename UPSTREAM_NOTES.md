# Snapshot notes

The files under `mirror/` retain their source bytes. Repairs belong upstream and then
arrive in a new snapshot; editing a mirrored file would break parity.

* The Constitution reading starter ZIP contains no LICENSE, COPYING or NOTICE member.
  Its Constitution text is CC0. Its wrapper files carry no explicit license in the
  archive; this repository does not invent one. See [LICENSES.md](LICENSES.md).
* The legacy fork kit predates Constitution 2.0. It is retained for historical
  compatibility, not presented as a finished 2.0 runtime.
* SHA-256 sidecars use both upper and lower case. The verifier accepts either hex case
  and reports the source inconsistency without rewriting any file.
* Older continuity downloads remain historical versions. New work should begin with
  the v0.3 package and its walkthrough.

This revision refreshes discovery and downloads, removes an internal source path from
the public manifest, and makes the separate Hugging Face dataset reproducible from
its own included pinned Core. The original package remains an unchanged historical
artifact. No private owner library, model weights, credentials or private transcript
is part of this distribution.
