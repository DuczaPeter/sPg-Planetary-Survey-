[English](DATA.en.md) | [Magyar](DATA.hu.md) · [README](../README.hu.md)

# Ércadatok
Rögzített pillanatkép: SCMDB [5.0.0-ptu.13284307](https://github.com/KrovaxCode/SCMDB_DATA/blob/main/data/mining_data-5.0.0-ptu.13284307.json), nem LIVE. A V10 nem adatfrissítés. Csak főércek jelennek meg. A kategóriák megjelenítési színek, nem igazolt számszerű radarjelek. A százalék a **rétegen belüli** lelőhelyarány, nem az ércösszetétel vagy bolygószintű valószínűség. A D a forrás sűrűsége; egysége nem igazolt.

## Az oldalsáv sorrendje
| # | Érc | Kategória | Szín | Réteg: arány / D | Becsült biom | Maszk |
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

## Hat réteg
A következő GUID-ok a projekt kutatásából származó SCMDB-forrásazonosítók; az alkalmazás kisbetűs rétegkulcsokat használ (`granite_01` stb.), nem a GUID-okat.
| Réteg | Típus | GUID | D |
|---|---|---|---:|
| Granite 01 | Geológia | `902664c3-41da-75fe-6bae-3b5cefe924e8` | 0.2042 |
| Granite 02 | Geológia | `128033a2-1e36-1f31-6ea6-209a65a84fbf` | 0.132 |
| Limestone 02 | Geológia | `902664c3-42da-75fe-6baf-3b5cefe924e8` | 0.033 |
| Arid 01 | Talaj | `1173e6bf-fabc-beab-94cf-99f4ef6d9967` | 0.286 |
| Balanced 01 | Talaj | `39fa1baf-6128-f8de-ce91-b35b77784ae8` | 0.05072 |
| Semi Arid 01 | Talaj | `39fa1baf-6128-f8de-ce91-b25b77784ae8` | 0.1906 |

## A becsült keresőzónák digitális geometriája
| Layer / Réteg | Mask | Active pixels / Aktív pixelek | Image % | x range | y range | Longitude (°) | Latitude (°) |
|---|---|---:|---:|---|---|---|---|
| Arid 01 | IMG_03 | 297530 | 3.546834 | [347,3803) | [695,1348) | [-149.501953,154.248047] | [-28.476562,28.916016] |
| Semi Arid 01 | IMG_08 | 1050335 | 12.520969 | [0,4096) | [285,1781) | [-180,180] | [-66.533203,64.951172] |
| Balanced 01 | IMG_13 | 350917 | 4.183257 | [0,4096) | [508,1797) | [-180,180] | [-67.939453,45.351562] |

A pontos alak a 4096×2048-as kitöltőmaszk összes 1-es indexű pixelének uniója; a 0 index átlátszó. A befoglaló keret nem téglalap alakú keresőzóna. Az (x,y) pixel hosszúsága [-180+360*x/W, -180+360*(x+1)/W], szélessége [90-180*(y+1)/H, 90-180*y/H]. W=4096, H=2048. A szabálytalan területeknek nincs egyetlen középpontjuk vagy sugaruk. A valódi km² és játékbeli koordináták ismeretlenek; a százalékok csak a vetületi képre vonatkoznak. Mindhárom talaj–biom kapcsolat hipotézis. A Granite 01, Granite 02 és Limestone 02 réteghez **nincs igazolt földrajzi maszk**: hat érchez nem rajzolható zóna. A rétegnévből ne következtess lelőhelyre.

Összes érc kitöltőszínei: Arid #e8ab54, Semi Arid #92cb79, Balanced #64cbd7. Geológiai listaszín #a4afc4. Egy ércnél kategóriaszín, perem #fff0a0. Az összes maszk előfordulása: [IMAGES](IMAGES.hu.md).

A régiónevek csak listában szerepelnek, nem térképi határokként: Western Expanse, Keern Region, Northern Reach, Unified Autonomous Region, Fenwick Territories, Eastern Expanse, Planters Claim, Averson Region. Forrás: [Cavalera](https://cavalera.news/editions/2026-11-06).
