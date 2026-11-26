[English](IMAGES.en.md) | [Magyar](IMAGES.hu.md) · [README](../README.hu.md)

# A képek eredete és sértetlensége
Eredeti archívum: `Nyx_I-raw_textures.zip`, PlanetFab / [VerseGuide PTU](https://ptu.verseguide.com/tools/textures), előzetes 5.0.0 EPTU. A program lábléce november 19-re datálja a textúraexportot; a bányászati adatok pontos buildjével való azonosság nem igazolt. A `nyx-i_surface.png` és `nyx-i_biome.png` változatlan 8192×4096-as, 8 bites RGB PNG, veszteségmentes DEFLATE tömörítéssel. A felszíni kép előre kiszámított domborzati árnyékot tartalmaz (nyugati nap 20° magasan, nagy formák 2×, finom részlet 1×). A biomtérkép Whittaker-klímaosztályokat használ, nem játékbeli geológiai címkéket. Vetület: equirectangular 2:1, észak felül, hosszúság −180 és +180 között, egyenlítő középen.

Az alábbi 18 előfordulás (15 egyedi kép) a futtatható JS sorrendjét követi. A hash a dekódolt PNG-bájtokra vonatkozik, NEM a Base64 szövegre. A duplikátumokat külön előfordulásként őrizd meg. A `PNG P` indexelt palettás PNG. Az eredeti képek be vannak ágyazva; a pontos újraépítéshez nem kell letöltés. Ha újra beszerzed a textúrákat, ugyanazt az archivált pillanatképet keresd; új export eltérhet. A terjesztési jog nem igazolt: [NOTICE](../NOTICE).

| ID | Hivatkozás | Méret | Formátum | Bájt | SHA-256 |
|---|---|---|---|---:|---|
| IMG_01 | `surface` | 8192×4096 | PNG RGB | 27726655 | `d40a50cf254862fea080088c59a1dd5afabbc0007c688068f400ca1fcbf64cd9` |
| IMG_02 | `biome` | 8192×4096 | PNG RGB | 2119121 | `f3f656a2e2587c5a168916b6cab9f02c262833833b43e97b5984146c29405877` |
| IMG_03 | `assets.arid_01.fills["#e8ab54"]` | 4096×2048 | PNG P | 32340 | `780fbfd9fba43a653523944cade9a7ff6ec879b1f6961171a903b676a44858de` |
| IMG_04 | `assets.arid_01.fills["#8899aa"]` | 4096×2048 | PNG P | 32340 | `66b4b9a42a39c4bf1307fc1ab31947f87d0604e51f3b563b310afa5eb48f3a9f` |
| IMG_05 | `assets.arid_01.edges["4"]` | 2048×1024 | PNG P | 7283 | `70426aecfdaebd8c3b076fd75f06cf03a7212b13f5c0ab10d01f139b103ec5d4` |
| IMG_06 | `assets.arid_01.edges["2"]` | 4096×2048 | PNG P | 19928 | `f37d777de5f9756627861006cfa3827764bc0e55255bd250bdbf7b95a01e7477` |
| IMG_07 | `assets.arid_01.edges["1"]` | 4096×2048 | PNG P | 19928 | `f37d777de5f9756627861006cfa3827764bc0e55255bd250bdbf7b95a01e7477` |
| IMG_08 | `assets.semi_arid_01.fills["#92cb79"]` | 4096×2048 | PNG P | 113700 | `da5f08f0f147edc07f960f0a4c1b423cca839ec1c5c5d84e3f89c1d24b6fd791` |
| IMG_09 | `assets.semi_arid_01.fills["#33ccaa"]` | 4096×2048 | PNG P | 113700 | `ca8064cc8f6754dc9618fd5fc05ea0578f66785224abc495fa8f383cd06e9683` |
| IMG_10 | `assets.semi_arid_01.edges["4"]` | 2048×1024 | PNG P | 24314 | `69085bb895ffb6115c7fab41434a7f107d7765911d7be6929189d2ba03e9b577` |
| IMG_11 | `assets.semi_arid_01.edges["2"]` | 4096×2048 | PNG P | 71109 | `cf88772d8124134e85c4735325c74a5bcc4997face700d6c09cd7e3c519753f3` |
| IMG_12 | `assets.semi_arid_01.edges["1"]` | 4096×2048 | PNG P | 71109 | `cf88772d8124134e85c4735325c74a5bcc4997face700d6c09cd7e3c519753f3` |
| IMG_13 | `assets.balanced_01.fills["#64cbd7"]` | 4096×2048 | PNG P | 54205 | `0bf93c12ce695b3b5a6a1c6616ce915ba19d45166ea6d85ad3c6cf763ea9735e` |
| IMG_14 | `assets.balanced_01.fills["#ffaa33"]` | 4096×2048 | PNG P | 54205 | `dfb0ac1a2142d1ef071bf09095a4de1866d786b13329e413a578e29f4be9986c` |
| IMG_15 | `assets.balanced_01.fills["#8899aa"]` | 4096×2048 | PNG P | 54205 | `1aa503e3ee4a9504f59e9bcc21e1a980ff864e0c39c24488fff014fb49be5263` |
| IMG_16 | `assets.balanced_01.edges["4"]` | 2048×1024 | PNG P | 10549 | `f834daf5090ff4500f18cdb0053fc3642de28ee6625ad6a7399e470e03c8c128` |
| IMG_17 | `assets.balanced_01.edges["2"]` | 4096×2048 | PNG P | 29775 | `07d7bdeb2bb64c6b28f37c2b96f7524ba0dd22ac09dfc28dc2e082fa943d5358` |
| IMG_18 | `assets.balanced_01.edges["1"]` | 4096×2048 | PNG P | 29775 | `07d7bdeb2bb64c6b28f37c2b96f7524ba0dd22ac09dfc28dc2e082fa943d5358` |

## Maszkok előállítása (történeti algoritmus)
A biomtérképen pontos RGB-egyezés: Desert #ffe010, Savanna #91e500, Grassland #ddf774. Kitöltés: logikai maszkból L 0/255 kép, NEAREST átméretezés 4096×2048-ra, >127 küszöb. Perem: n=4 → 2048×1024; n=2 vagy 1 → 4096×2048. BOX átméretezés, >127 küszöb, bináris zárás, majd nyitás 3×3 igaz struktúrával. Vízszintes körbeforgó 1 pixeles padding, minimum_filter(size=3, mode='nearest'), padding levágása; perem = maszk ÉS NEM erózió. Peremszín #fff0a0. Python Pillow, NumPy és SciPy használatával készült. A 0 palettaindex átlátszó, az 1 színes: `Image.fromarray(mask.astype('uint8')).convert('P')`, `putpalette([0,0,0,*rgb(color)]+[0]*762)`, `save(format='PNG',bits=1,transparency=0)`. Újrakódoláskor a könyvtárverziók miatt eltérhetnek a bájtok; pontos újraépítéshez a beágyazott PNG-ket használd.

A dekódolt méreteket, SHA-256-ot, PNG-szerkezetet, CRC-t, felbontást és DEFLATE adatfolyamot a `python scripts/verify.py` ellenőrzi. A 06/07, 11/12, 17/18 perempárok szándékosan azonosak. Az `images/` képei böngészőből mentett JPEG-ek, nem futásidejű képek.
