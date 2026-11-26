[English](RULES.en.md) | [Magyar](RULES.hu.md) · [README](../README.hu.md)

# Hozzájárulási és módosítási szabályok
1. Csak pontos, egyedi horgonnyal meghatározott szöveg- vagy kódrészleteket módosíts. Soha ne futtass globális keresés-cserét Base64-et tartalmazó HTML-en; ne formázd vagy szerializáld újra mellékhatásként az egész fájlt.
2. Minden módosítás után ellenőrizd a 18 dekódolt PNG-előfordulás SHA-256 összegét mindkét dokumentációs listával. Váratlan eltérésnél állj meg és állítsd vissza a hiteles verziót. Kifejezetten jóváhagyott képcsere esetén új forrásigazolás, hash és teljes regressziós teszt szükséges; ne frissítsd csendben az elvárt értékeket.
3. Új kiadást csak tényleges Chrome-teszt után nevezz késznek: kép betölt, mind a 13 érc, három nézet, törlés, vékony perem. A tényleges jelölt hash-ét teszteld, ne az előző kiadást. A 0,65px történeti tervezési cél, nem igazolt állandó a V10-ben.
4. Tiltott böngészőfuttatásnál ezt egyértelműen jelezd; ne állíts ellenőrizetlen „működik” eredményt. Különítsd el a helyi fájlt és set_content-et, Chromiumot és Chrome-ot, tényleges és elvárt eredményt.
5. Őrizd meg a működő betöltést, textúrákat, tömörítést, ércsorrendet és színeket, ha a jóváhagyott változtatás nem igényli őket. Ne keverd a PTU és LIVE adatokat, ne rendelj hozzá igazolatlan lelőhelyet. Őrizd meg a forrásverziót és eredetet.
6. Minden új kiadásnál frissítsd a beágyazott forrássablont, dokumentációt, ellenőrzőlistákat és naplót a valós kóddal, célzottan emeld a verziót és teszteld újra. Az előző alap maradjon meg. A CI szándékosan rögzíti a V10-et; új, jóváhagyott alaphoz mindkét elvárt fájlhash, a dokumentáció és a tesztek kifejezett frissítése kell, nem a védelem törlése.
7. Jelszó, token, személyes vagy privát adat ne kerüljön kódba, képre, naplóba, commitba vagy dokumentációba. A GitHub saját hitelesítését használd; ne írj be kulcsokat a kódba. Nincs jóváhagyás nélküli publikálás. Előbb tisztázd a külső jogosultságokat és a tulajdonosi licencdöntést.

Külön ágon nyújts be célzott diffet, magyarázatot, pontos jelölthash-t, determinisztikus ellenőrzést és böngészős bizonyítékot. Ne commitolj rekonstruált másolatokat vagy ideiglenes fájlokat. A `scripts/verify.py` csak olvas, kivéve ha a `--output` új fájlt ad meg; lásd [REBUILD](REBUILD.hu.md).
