[English](CHANGELOG.en.md) | [Magyar](CHANGELOG.hu.md) · [README](../README.md)

# Development log

## V4
Clickable sidebar, 13 ores, original 8K textures. Boundaries too hard to see on similar colors; no independent outline. Full browser test not performed.

## V5
Double SVG outline: dark #101820 3.5px and white #ffffff 1.4px. Too thick and visually noisy; outlines also appeared without a single ore selection. Cause: two wide strokes and overly complex paths. No full visual test.

## V6
Intended 0.65px light-yellow edge for selected ore only. Map did not load and selection failed; the initial diagnosis was multi-megabyte complex SVG outlines. Later byte inspection also identified corrupted embedded images; complexity alone is not a proven sole cause.

## V7
Simplified outlines and masks, returned to V4. Map still did not load and layer switching failed. Confirmed cause: global V4→V7 replacement touched Base64. Outline simplification did not repair image bytes. Browser test blocked.

## V8
Reduced size via 8K JPEG quality 89 and PNG masks; selection switched to estimate. Texture broke into horizontal stripes, colors distorted, Gold retained old coloration. Confirmed cause: global V7→V8 replacement again corrupted Base64, including the biome PNG; the independent cause of stale Gold coloring was not proven. V9 explicitly clears overlays. No complete browser test.

## V9
Restored byte-identical V4 textures; confirmed root cause was version replacement inside embedded image data. Precomputed indexed PNG masks, explicit clear, Gold has no mask. Chromium interactions succeeded; file:// blocked, intermittent image.decode failure in historical test. Raster thickness is zoom-dependent; 0.65px was a design target.

## V10
Documentation-only head block after charset, complete V9 template and manifests. Runtime identical; V9 title intentionally unchanged. No data update or functionality change. Earlier test had a timeout; subsequent Chromium tests and reconstruction passed, local file blocked. This package adds separate docs and CI without modifying V10.

Historical decode checks: V4/V5 both original PNGs identical to V9; V6/V7 both corrupted; V8 surface decodable but changed, biome corrupted; V9/V10 restored original PNGs. See embedded development log for exact historical evidence.
