[English](DATA.en.md) | [Magyar](DATA.hu.md) · [README](../README.md)

# Ore data
Frozen snapshot: SCMDB [5.0.0-ptu.13284307](https://github.com/KrovaxCode/SCMDB_DATA/blob/main/data/mining_data-5.0.0-ptu.13284307.json), not LIVE. V10 is not an update. Only primary ores are shown. Categories are display colors, not validated numeric radar signatures. Share is the proportion of deposits **within a layer**, not ore composition or planet-wide probability. D is source density; its unit is unverified.

## Sidebar order
| # | Ore | Category | Color | Layer: share / D | Estimated biome | Mask |
|---:|---|---|---|---|---|---|
| 1 | Savrilium | Legendary | `#ffaa33` | Balanced 01: 16.40% / 0.00832 | Grassland | IMG_13 |
| 2 | Gold | Rare | `#3399ff` | Granite 01: 17.19% / 0.0351; Granite 02: 26.59% / 0.0351 | — | — |
| 3 | Bexalite | Rare | `#3399ff` | Granite 01: 15.77% / 0.0322; Granite 02: 24.39% / 0.0322 | — | — |
| 4 | Laranite | Uncommon | `#33ccaa` | Semi Arid 01: 33.68% / 0.0642 | Savanna | IMG_08 |
| 5 | Aslarite | Uncommon | `#33ccaa` | Limestone 02: 100.00% / 0.033 | — | — |
| 6 | Titanium | Uncommon | `#33ccaa` | Semi Arid 01: 32.63% / 0.0622 | Savanna | IMG_08 |
| 7 | Agricium | Uncommon | `#33ccaa` | Semi Arid 01: 33.68% / 0.0642 | Savanna | IMG_08 |
| 8 | Torite | Uncommon | `#33ccaa` | Granite 01: 23.07% / 0.0471 | — | — |
| 9 | Hephaestanite | Common | `#8899aa` | Granite 01: 43.98% / 0.0898 | — | — |
| 10 | Tin | Common | `#8899aa` | Balanced 01: 83.60% / 0.0424 | Grassland | IMG_13 |
| 11 | Quartz | Common | `#8899aa` | Granite 02: 49.02% / 0.0647 | — | — |
| 12 | Copper | Common | `#8899aa` | Arid 01: 50.70% / 0.145 | Desert | IMG_03 |
| 13 | Aluminum | Common | `#8899aa` | Arid 01: 49.30% / 0.141 | Desert | IMG_03 |

## Six layers
The following GUIDs are SCMDB provenance identifiers from the project research; the application uses lowercase layer keys (`granite_01`, etc.), not the GUIDs.
| Layer | Kind | GUID | D |
|---|---|---|---:|
| Granite 01 | Geology | `902664c3-41da-75fe-6bae-3b5cefe924e8` | 0.2042 |
| Granite 02 | Geology | `128033a2-1e36-1f31-6ea6-209a65a84fbf` | 0.132 |
| Limestone 02 | Geology | `902664c3-42da-75fe-6baf-3b5cefe924e8` | 0.033 |
| Arid 01 | Soil | `1173e6bf-fabc-beab-94cf-99f4ef6d9967` | 0.286 |
| Balanced 01 | Soil | `39fa1baf-6128-f8de-ce91-b35b77784ae8` | 0.05072 |
| Semi Arid 01 | Soil | `39fa1baf-6128-f8de-ce91-b25b77784ae8` | 0.1906 |

## Digital geometry of estimated search zones
| Layer / Réteg | Mask | Active pixels / Aktív pixelek | Image % | x range | y range | Longitude (°) | Latitude (°) |
|---|---|---:|---:|---|---|---|---|
| Arid 01 | IMG_03 | 297530 | 3.546834 | [347,3803) | [695,1348) | [-149.501953,154.248047] | [-28.476562,28.916016] |
| Semi Arid 01 | IMG_08 | 1050335 | 12.520969 | [0,4096) | [285,1781) | [-180,180] | [-66.533203,64.951172] |
| Balanced 01 | IMG_13 | 350917 | 4.183257 | [0,4096) | [508,1797) | [-180,180] | [-67.939453,45.351562] |

The exact shape is the union of all index-1 pixels in each 4096×2048 fill mask; index 0 is transparent. The bounds are not rectangular search areas. For pixel (x,y), longitude spans [-180+360*x/W, -180+360*(x+1)/W] and latitude spans [90-180*(y+1)/H, 90-180*y/H]. W=4096, H=2048. These irregular regions have no single center or radius. True area in km² and in-game coordinates are unknown; percentages refer to the projected image only. All three soil-to-biome associations are hypotheses. Granite 01, Granite 02 and Limestone 02 have **no verified geographic mask**: six ores have no drawable zone. Never infer a location from the layer name.

All-ore fill colors: Arid #e8ab54, Semi Arid #92cb79, Balanced #64cbd7. Geological list color #a4afc4. Single-ore fill uses its category color; edge #fff0a0. See [IMAGES](IMAGES.en.md) for all mask occurrences.

Region names are a list, not plotted boundaries: Western Expanse, Keern Region, Northern Reach, Unified Autonomous Region, Fenwick Territories, Eastern Expanse, Planters Claim, Averson Region. Source: [Cavalera](https://cavalera.news/editions/2026-11-06).
