[English](TESTING.en.md) | [Magyar](TESTING.hu.md) · [README](../README.md)

# Test plan and recorded results
Baseline SHA-256: `068b865c6327ab3000e3db41aad2fa5a286b5494bb434e0a78d5249277b5bd04`. 26 November 2026, real headless Chromium 144.0.7559.96, 1820×1050. Direct `file://` navigation blocked by administrator policy; all interaction checks used the **full unchanged HTML** via Playwright `set_content`. This is not a branded Google Chrome local-file certification. Seven unedited browser JPEG captures at quality 85 are in `images/`. No GIF was produced. Raw results: [browser-results.json](browser-results.json).

## Manual steps
1. Open the file in desktop Chrome (not chat preview). Open DevTools Console. Confirm no stripes, decode errors or exceptions. Run `python scripts/verify.py` first.
2. Click each ore in order. Counts below mean fill images / edge images. The initial view is all ores; unknown locations must show no invented zone. Confirm the selected button and data card.

| # | Ore / Érc | Expected / Elvárt | Result / Eredmény |
|---:|---|---|---|
| 1 | Savrilium | Only Grassland, #ffaa33, #fff0a0 edge; 1/1 | PASS |
| 2 | Gold | Original surface; 0/0; unknown location | PASS |
| 3 | Bexalite | Original surface; 0/0; unknown location | PASS |
| 4 | Laranite | Only Savanna, #33ccaa, #fff0a0 edge; 1/1 | PASS |
| 5 | Aslarite | Original surface; 0/0; unknown location | PASS |
| 6 | Titanium | Only Savanna, #33ccaa, #fff0a0 edge; 1/1 | PASS |
| 7 | Agricium | Only Savanna, #33ccaa, #fff0a0 edge; 1/1 | PASS |
| 8 | Torite | Original surface; 0/0; unknown location | PASS |
| 9 | Hephaestanite | Original surface; 0/0; unknown location | PASS |
| 10 | Tin | Only Grassland, #8899aa, #fff0a0 edge; 1/1 | PASS |
| 11 | Quartz | Original surface; 0/0; unknown location | PASS |
| 12 | Copper | Only Desert, #8899aa, #fff0a0 edge; 1/1 | PASS |
| 13 | Aluminum | Only Desert, #8899aa, #fff0a0 edge; 1/1 | PASS |

3. Perform the following controls in order. Inspect the actual map and data cards as well as DOM state.

| Case | Expected | Result |
|---|---|---|
| Initial / all | 8192×4096 base, 3 fills, 0 edges, 14 buttons including all, 6 layer cards | PASS |
| Savrilium → Gold → Copper | 1/1 → 0/0 → 1/1, no stale overlay | PASS |
| Layer card button | Same selection as sidebar | PASS |
| Surface view | Original surface, 0/0 | PASS |
| Biome view | Original biome, 0/0 | PASS |
| Estimate view | Surface, selected known fill/edge | PASS |
| Ore click from biome | Switch to estimate, render | PASS |
| Zoom 1, 2, 4, 8, back to 1 | stage 100–800%, one correct edge; no duplicate edge | PASS |
| Opacity 0,45,100 | Fill only, edge opacity remains 1 | PASS |
| Grid | Toggle only grid | PASS |
| Drag / coordinates | Scroll changes; coordinate readout updates on pointer movement | PASS |
| Regions | Expand/collapse; 8 entries | PASS |
| Reset | All, estimate, 1×, 45%, grid on, scroll 0,0 | PASS |
| 700px mobile width | Sidebar first, one column | PASS |
| Local file opening | Exact HTML opens directly | BLOCKED — administrator policy |
| Console / external requests | No JS errors, no external network requests during interaction | PASS |
| Thin yellow edge | Visually thin on Savrilium at 1×; exact 0.65px not guaranteed | PASS at 1× visual check; invariant thickness not supported |


## Repeat automated tests
Install Python, Node and Playwright (`python -m pip install playwright`). Set `CHROME_PATH` to the installed Chrome executable (PowerShell example: `$env:CHROME_PATH = 'C:\Program Files\Google\Chrome\Application\chrome.exe'`). Alternatively install Playwright Chromium (`python -m playwright install chromium`). From root run `python scripts/browser_test.py`. It writes real screenshots and JSON evidence; local-file fallback is recorded, not silently treated as a pass. Check visuals manually, especially at each zoom. Native keyboard behavior is not custom and was not separately tested. GitHub Actions runs deterministic checks only, not browser certification. Run [REBUILD](REBUILD.en.md) for exact reconstruction before release. If mandatory tests are blocked or fail, report that status; do not certify a release.
