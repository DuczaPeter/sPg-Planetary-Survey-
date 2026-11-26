[English](REBUILD.en.md) | [Magyar](REBUILD.hu.md) · [README](../README.hu.md)

# V10 pontos újraépítése
## Előfeltételek
A változatlan [V10 HTML](../sPg_Nyx_I_V10_dokumentalt.html) a hiteles bemenet. Python 3 és Node.js csak az ellenőrzéshez szükséges. Nem kell eredeti ZIP, hálózat, könyvtár vagy külső kép a beágyazott dokumentációból és a 18 képelőfordulásból történő újraépítéshez. E bájtok nélkül a pontos újraépítés nem lehetséges; képernyőkép vagy újragenerált térkép nem helyettesíti őket.

1. Klónozd/töltsd le a tárolót, az HTML bájtjait ne módosítsd. Telepítsd a Python 3-at és a Node.js 22-t (vagy kompatibilis verziót). Nyiss terminált a tároló gyökerében.
2. Olvasd el a beágyazott `script[type="text/plain"]#ai-ujraepitesi-dokumentacio` blokkot. A teljes V9 forrássablon a pontos `BEGIN_V9_TEMPLATE` és `END_V9_TEMPLATE` sorok között van. Őrizd meg a teljes eredeti dokumentációs elemet az újsorokkal együtt; ne futtasd.
3. Csak ezt a pontos elemet távolítsd el a bemenetből. Nyerd ki a 18 `data:image/png;base64,` URI-t a futó script sorrendjében. Szigorúan dekódold, ellenőrizd a felbontást, bájtméretet és hash-t az [IMAGES](IMAGES.hu.md) és a beágyazott lista szerint. Minden URI maradjon szöveghű, a duplikátumok is.
4. Emeld ki a sablont a két határoló sor közül (a két határoló újsor nélkül, záró újsor nélkül). Csak az egzakt `@@IMG_01@@` … `@@IMG_18@@` helyőrzőket cseréld a teljes megfelelő URI-kra, az `@@SCRIPT_END@@` helyére a script záró tagját illeszd. Soha ne végezz globális verzió- vagy szövegcserét Base64-et tartalmazó HTML-en. Az eredeti V9 elvárt SHA-256: `e83152dd788a4aa5dd0505a3a3463fe8d37f245f0d0be13b7675bf0f6b67c55f`.
5. A teljes változatlan dokumentációs elemet közvetlenül az egyedi `<meta charset="utf-8">` jelölés után illeszd a rekonstruált V9-be. Az eredmény V10, UTF-8 záró újsor nélkül, SHA-256: `068b865c6327ab3000e3db41aad2fa5a286b5494bb434e0a78d5249277b5bd04`.
6. A mellékelt script automatikusan végrehajtja ezeket a lépéseket, és `node --check` ellenőrzést futtat kizárólag a végrehajtható JS-en. A kimenet új fájl legyen; ne írd felül az eredetit.

```powershell
python scripts/verify.py --output reconstructed-v10.html
Get-FileHash ./sPg_Nyx_I_V10_dokumentalt.html -Algorithm SHA256
Get-FileHash ./reconstructed-v10.html -Algorithm SHA256
```

Elvárt: mindkét V10 hash pontosan egyezik; a script PASS-t ír 18 előfordulásra, a V9/V10 újraépítésre és a JS szintaxisára. Eltérésnél állj meg, állítsd vissza a hiteles eredetit, és vizsgáld ki a hibát. Nyisd meg az újraépített fájlt Chrome-ban, majd kövesd a [TESTING](TESTING.hu.md) útmutatót. Tiltott helyi megnyitásnál ne állíts sikeres Chrome-tesztet. A `.gitattributes` védi a hiteles HTML-t a Git sorvég-konverziójától.
