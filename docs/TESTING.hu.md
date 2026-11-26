[English](TESTING.en.md) | [Magyar](TESTING.hu.md) · [README](../README.hu.md)

# Tesztterv és rögzített eredmények
Alapállapot SHA-256: `068b865c6327ab3000e3db41aad2fa5a286b5494bb434e0a78d5249277b5bd04`. 2026. november 26., valódi headless Chromium 144.0.7559.96, 1820×1050. A közvetlen `file://` navigáció rendszergazdai tiltásba ütközött; minden interakciós ellenőrzés a **teljes változatlan HTML** Playwright `set_content` betöltésével történt. Ez nem a külön Google Chrome helyi fájlos tanúsítása. Hét szerkesztetlen, 85-ös minőségű böngésző-JPEG található az `images/` mappában. GIF nem készült. Nyers eredmény: [browser-results.json](browser-results.json).

## Manuális lépések
1. Nyisd meg a fájlt asztali Chrome-ban (ne chat előnézetben). Nyisd meg a DevTools konzolt. Ne legyen csík, dekódolási hiba vagy kivétel. Először futtasd: `python scripts/verify.py`.
2. Kattints sorban minden ércre. A számok alább a kitöltőképek / peremképek darabszámát jelölik. Kezdetben minden érc látszik; ismeretlen helyhez ne legyen kitalált zóna. Ellenőrizd az aktív gombot és adatlapot.

| # | Ore / Érc | Expected / Elvárt | Result / Eredmény |
|---:|---|---|---|
| 1 | Savrilium | Csak Grassland, #ffaa33, #fff0a0 perem; 1/1 | PASS |
| 2 | Gold | Eredeti felszín; 0/0; ismeretlen hely | PASS |
| 3 | Bexalite | Eredeti felszín; 0/0; ismeretlen hely | PASS |
| 4 | Laranite | Csak Savanna, #33ccaa, #fff0a0 perem; 1/1 | PASS |
| 5 | Aslarite | Eredeti felszín; 0/0; ismeretlen hely | PASS |
| 6 | Titanium | Csak Savanna, #33ccaa, #fff0a0 perem; 1/1 | PASS |
| 7 | Agricium | Csak Savanna, #33ccaa, #fff0a0 perem; 1/1 | PASS |
| 8 | Torite | Eredeti felszín; 0/0; ismeretlen hely | PASS |
| 9 | Hephaestanite | Eredeti felszín; 0/0; ismeretlen hely | PASS |
| 10 | Tin | Csak Grassland, #8899aa, #fff0a0 perem; 1/1 | PASS |
| 11 | Quartz | Eredeti felszín; 0/0; ismeretlen hely | PASS |
| 12 | Copper | Csak Desert, #8899aa, #fff0a0 perem; 1/1 | PASS |
| 13 | Aluminum | Csak Desert, #8899aa, #fff0a0 perem; 1/1 | PASS |

3. Sorban végezd el a következő vezérlési próbákat. A DOM-állapot mellett nézd meg a térképet és adatlapokat is.

| Eset | Elvárt | Eredmény |
|---|---|---|
| Kezdőnézet / összes | 8192×4096 alapkép, 3 kitöltés, 0 perem, 14 gomb az összessel, 6 rétegkártya | PASS |
| Savrilium → Gold → Copper | 1/1 → 0/0 → 1/1, nincs régi rávetítés | PASS |
| Rétegkártya gombja | Ugyanaz a kijelölés, mint oldalt | PASS |
| Felszín | Eredeti felszín, 0/0 | PASS |
| Biom | Eredeti biom, 0/0 | PASS |
| Becsült nézet | Felszín, a kiválasztott ismert kitöltés/perem | PASS |
| Érckattintás biomnézetből | Estimate-re váltás, render | PASS |
| Nagyítás 1, 2, 4, 8, vissza 1 | stage 100–800%, egy helyes perem; nincs duplikáció | PASS |
| Színezés 0,45,100 | Csak kitöltés, perem átlátszósága 1 marad | PASS |
| Hálózat | Csak rács kapcsolása | PASS |
| Húzás / koordináták | Scroll változik, koordináta frissül az egérmozgásra | PASS |
| Régiók | Nyitás/zárás; 8 elem | PASS |
| Alaphelyzet | Összes, estimate, 1×, 45%, hálózat be, scroll 0,0 | PASS |
| 700px mobil szélesség | Oldalsáv elöl, egy oszlop | PASS |
| Helyi fájlmegnyitás | A pontos HTML közvetlenül megnyílik | BLOCKED — rendszergazdai tiltás |
| Konzol / külső kérések | Nincs JS-hiba, nincs külső hálózati kérés használat közben | PASS |
| Vékony sárga perem | Savriliumnál 1×-esen vizuálisan vékony; pontos 0,65px nem garantált | PASS 1× vizuális ellenőrzés; állandó vastagság nem támogatott |


## Automatikus tesztek ismétlése
Telepíts Python, Node és Playwright környezetet (`python -m pip install playwright`). A `CHROME_PATH` értéke legyen a telepített Chrome futtatható fájlja (PowerShell példa: `$env:CHROME_PATH = 'C:\Program Files\Google\Chrome\Application\chrome.exe'`). Alternatíva a Playwright Chromium (`python -m playwright install chromium`). A gyökérből futtasd: `python scripts/browser_test.py`. Valódi képernyőképeket és JSON-bizonyítékot ment; a helyi megnyitás helyettesítő módját naplózza, nem állítja sikeresnek. Nézd meg kézzel is a megjelenést, különösen minden nagyításnál. A natív billentyűkezelés nem egyedi, külön nem teszteltük. A GitHub Actions csak determinisztikus ellenőrzést futtat, nem böngészős tanúsítást. Kiadás előtt futtasd az [REBUILD](REBUILD.hu.md) pontos újraépítését. Kötelező teszt hibája vagy tiltása esetén jelezd az állapotot; ne tanúsítsd a kiadást.
