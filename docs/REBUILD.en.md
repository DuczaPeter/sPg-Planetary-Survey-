[English](REBUILD.en.md) | [Magyar](REBUILD.hu.md) · [README](../README.md)

# Rebuild V10 exactly
## Requirements
The unchanged [V10 HTML](../sPg_Nyx_I_V10_dokumentalt.html) is the canonical input. Python 3 and Node.js are required for verification only. No original ZIP, network, library or external images are required to reconstruct the program from the embedded document and its 18 image occurrences. Without those bytes, exact reconstruction is impossible; a screenshot or regenerated map is not a substitute.

1. Clone/download the repository and keep the HTML bytes unchanged. Install Python 3 and Node.js 22 (or another compatible version). Open a terminal in the repository root.
2. Read the embedded `script[type="text/plain"]#ai-ujraepitesi-dokumentacio`. Its complete V9 source template is between the exact `BEGIN_V9_TEMPLATE` and `END_V9_TEMPLATE` lines. Retain the original full documentation wrapper including newlines; do not run it.
3. Remove only that exact wrapper from the input. Extract the 18 `data:image/png;base64,` URIs in executable-script order. Decode strictly, verify dimensions, byte counts and hashes against [IMAGES](IMAGES.en.md) and the embedded manifest. Preserve every URI verbatim, including duplicates.
4. Extract the template between the marker lines (exclude both delimiting newlines, no trailing newline). Replace exact `@@IMG_01@@` … `@@IMG_18@@` placeholders with the corresponding full URIs, and `@@SCRIPT_END@@` with the script closing tag. Never run global version or text replacement on HTML containing Base64. The result must be original V9 SHA-256 `e83152dd788a4aa5dd0505a3a3463fe8d37f245f0d0be13b7675bf0f6b67c55f`.
5. Insert the unchanged full documentation wrapper immediately after the unique `<meta charset="utf-8">` anchor in rebuilt V9. The result is V10, UTF-8 with no trailing newline, SHA-256 `068b865c6327ab3000e3db41aad2fa5a286b5494bb434e0a78d5249277b5bd04`.
6. Use the included script to execute these exact steps automatically; it also runs `node --check` on executable JS only. Output must be a new file; never overwrite the original.

```powershell
python scripts/verify.py --output reconstructed-v10.html
Get-FileHash ./sPg_Nyx_I_V10_dokumentalt.html -Algorithm SHA256
Get-FileHash ./reconstructed-v10.html -Algorithm SHA256
```

Expected: both V10 hashes match exactly; script prints PASS for 18 occurrences, V9/V10 reconstruction and JS syntax. If anything differs, stop, restore the trusted original and investigate. Open the reconstructed file in Chrome and follow [TESTING](TESTING.en.md). Do not claim successful local Chrome testing if it is blocked. `.gitattributes` prevents Git line-ending conversion on the canonical HTML.
