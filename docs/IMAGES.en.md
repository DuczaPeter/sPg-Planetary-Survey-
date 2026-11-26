[English](IMAGES.en.md) | [Magyar](IMAGES.hu.md) · [README](../README.md)

# Image provenance and integrity
Original archive: `Nyx_I-raw_textures.zip`, PlanetFab / [VerseGuide PTU](https://ptu.verseguide.com/tools/textures), preliminary 5.0.0 EPTU. The program footer dates the texture export November 19; exact build equivalence to the mining dataset is not established. `nyx-i_surface.png` and `nyx-i_biome.png` are untouched 8192×4096 8-bit RGB PNGs, losslessly DEFLATE-compressed. The surface has baked relief shading (western sun at 20°, large features 2×, fine detail 1×). The biome map uses Whittaker climate classes, not in-game geology labels. Projection: equirectangular 2:1, north up, longitude −180 to +180, equator centered.

The 18 occurrences (15 unique images) below appear in executable JS order. Hashes are for decoded PNG bytes, NOT Base64 text. Keep repeated images as separate occurrences. `PNG P` means indexed palette PNG. The original images are embedded; no download is needed for exact reconstruction. If obtaining textures again, use the same archived snapshot; new exports may differ. Redistribution rights remain unconfirmed: [NOTICE](../NOTICE).

| ID | Reference | Dimensions | Format | Bytes | SHA-256 |
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

## Mask generation (historical algorithm)
Select exact RGB in biome: Desert #ffe010, Savanna #91e500, Grassland #ddf774. Fill: convert Boolean mask to L 0/255, resize NEAREST to 4096×2048, threshold >127. Edge: n=4 → 2048×1024; n=2 or 1 → 4096×2048. Resize BOX, threshold >127, binary closing then opening with a 3×3 true structure. Horizontally wrap-pad one pixel, minimum_filter(size=3, mode='nearest'), crop padding; edge = mask AND NOT erosion. Edge color #fff0a0. Python Pillow, NumPy and SciPy were used. Encode with palette index 0 transparent, index 1 color: `Image.fromarray(mask.astype('uint8')).convert('P')`, `putpalette([0,0,0,*rgb(color)]+[0]*762)`, `save(format='PNG',bits=1,transparency=0)`. Re-encoding may change bytes due to library versions; use the embedded PNGs to reconstruct exactly.

Verify decoded sizes, SHA-256, PNG structure, CRC, dimensions and DEFLATE stream with `python scripts/verify.py`. The three edge pairs 06/07, 11/12, 17/18 are intentionally identical. Screenshots in `images/` are browser-generated JPEGs, not runtime assets.
