[English](RULES.en.md) | [Magyar](RULES.hu.md) · [README](../README.md)

# Contribution and modification rules
1. Change only exact, uniquely anchored text/code spans. Never perform global search-and-replace on HTML with Base64; never format or reserialize the whole file as a side effect.
2. After every change, check SHA-256 of all 18 decoded PNG occurrences against both documentation manifests. If an unexpected hash differs, stop and restore the trusted version. Any explicitly approved image update needs new provenance, hashes and full regression testing; never silently refresh expected hashes.
3. Only call a release ready after actual Chrome testing: picture loads, all 13 ores, three views, clear behavior, thin edge. Test the actual candidate hash, not the previous release. 0.65px is a historic design goal, not a verified invariant in V10.
4. If browser execution is blocked, report it clearly; no unverified “works” claim. Distinguish local file and set_content, Chromium and Chrome, actual vs expected results.
5. Preserve working loading, textures, compression, ore order and colors unless required by the approved change. Never mix PTU and LIVE or assign unverified ore locations. Preserve source version and provenance.
6. For each new release, update the embedded reconstruction template, documentation, manifests and changelog with the actual code, increase version using targeted replacements, and re-test. Keep previous baseline. The CI verifier deliberately pins V10; a new reviewed baseline requires explicit update of both expected file hashes, docs and tests, not merely deleting the guard.
7. No passwords, tokens, personal/private data in code, screenshots, logs, commits or documentation. Use GitHub's own authentication; no hard-coded credentials. No unapproved publication. Check third-party permissions and owner license decision first.

Submit changes on a separate branch with a focused diff, explanation, exact candidate hash, deterministic verification and browser evidence. Do not commit rebuilt duplicates or generated temporary files. `scripts/verify.py` is read-only unless `--output` specifies a new file; see [REBUILD](REBUILD.en.md).
