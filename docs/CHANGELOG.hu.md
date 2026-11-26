[English](CHANGELOG.en.md) | [Magyar](CHANGELOG.hu.md) · [README](../README.hu.md)

# Fejlesztési napló

## V4
Kattintható oldalsáv, 13 érc, eredeti 8K textúrák. Hasonló terepszínnél a határ nehezen látszott; nem volt külön körvonal. Teljes böngészőteszt nem történt.

## V5
Kettős SVG-kontúr: sötét #101820 3,5px és fehér #ffffff 1,4px. Túl vastag és zajos; egyetlen érc kijelölése nélkül is megjelent. Ok: két széles vonal és túl összetett útvonalak. Nem volt teljes vizuális teszt.

## V6
Tervezett 0,65px világossárga perem csak a kijelölt ércre. Nem töltött be a kép és nem működött a kiválasztás; akkori diagnózis a több MB-os túl összetett SVG-kontúr. Későbbi bájtvizsgálat sérült beágyazott képeket is azonosított; az SVG-terhelés nem igazolt egyedüli ok.

## V7
Egyszerűsített peremek és maszkok, visszatérés a V4-hez. A kép továbbra sem töltött be és a rétegváltás sem működött. Igazolt ok: globális V4→V7 csere belenyúlt a Base64-be. A kontúregyszerűsítés nem javította a képbájtokat. Böngészőteszt tiltott.

## V8
Méretcsökkentés 8K JPEG quality 89 és PNG-maszkok segítségével; ércválasztás estimate-re váltott. A textúra vízszintes csíkokra esett szét, a színezés torzult, Goldnál megmaradt a korábbi színezés. Igazolt ok: globális V7→V8 csere ismét megsértette a Base64-et, többek között a biom PNG-t; a Gold színezésének külön gyökéroka nem igazolt. V9 explicit töröl. Teljes böngészőteszt nem volt.

## V9
Bájtra azonos V4 textúrák visszaállítása; igazolt gyökérok a beágyazott képadatokon belüli verziócsere volt. Előre számított indexelt PNG-maszkok, explicit törlés, Goldhoz nincs maszk. Chromium-interakciók sikeresek; file:// tiltott, a történeti tesztben időnként image.decode hiba. Raszteres vastagság nagyításfüggő; a 0,65px tervezési cél volt.

## V10
Csak dokumentációs head-blokk a charset után, teljes V9 sablon és manifest. Futó kód azonos; a V9 cím szándékosan változatlan. Nincs adatfrissítés vagy funkcióváltás. A korábbi próbán időtúllépés történt; a következő Chromium-tesztek és újraépítés sikeresek, helyi fájl tiltott. Ez a csomag külön dokumentációt és CI-t ad hozzá a V10 változtatása nélkül.

Történeti dekódolási ellenőrzés: V4/V5 mindkét PNG V9-cel azonos; V6/V7 mindkettő sérült; V8 felszín dekódolható, de eltérő, biom sérült; V9/V10 eredeti PNG-k visszaállítva. A részletes történeti bizonyíték a beágyazott naplóban található.
