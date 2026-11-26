[English](UPLOAD.en.md) | [Magyar](UPLOAD.hu.md) · [README](../README.hu.md)

# Feltöltés és publikálás (csak jogosultsági ellenőrzés után)
Az HTML 40 845 886 bájt (~38,95 MiB). A GitHub böngészős feltöltése fájlonként 25 MiB-ra korlátozott; a normál Git 100 MiB felett blokkol, tehát ez a fájl belefér a normál Gitbe. A Release-eszközöknek 2 GiB alatt kell lenniük. Pages webhely legfeljebb 1 GB lehet; a csomag mérete belefér, de a jogok, csomag és beállítások továbbra is számítanak.

## A lehetőség — Git parancssor
1. Olvasd el a [NOTICE](../NOTICE) és [LICENSE](../LICENSE) fájlt. Szerezz megfelelő engedélyt a játékból származó tartalmak feltöltéséhez. Válassz sajátkód-licencet. Ne publikálj a tisztázás előtt.
2. Hozz létre helyben egy `spg-nyx-i-ore-map` mappát. Minden átadott fájlt pontosan a megadott relatív útvonalra ments; engedélyezd a rejtett fájlok megjelenítését a `.github` és `.gitattributes` miatt. Az HTML-t ne nyisd meg szerkesztésre és ne mentsd újra. Az eredeti ZIP-et és a rekonstruált másolatot ne töltsd fel. Telepítsd a [Gitet](https://git-scm.com/downloads), a Pythont és a Node-ot, ha szükséges.
3. A GitHubon készíts **új, üres** `spg-nyx-i-ore-map` tárolót a `DuczaPeter` fiókban (először privátként, csak ha a feltöltés megengedett). Ne generáltass README-t, licencet vagy gitignore-t. Nyiss PowerShellt a helyi mappában. Commit előtt futtasd: `python scripts/verify.py`. Ha a Git kéri, helyileg állítsd be a szerzői azonosítást; személyes e-mail közzététele helyett használhatod a GitHub no-reply címed. Git Credential Manager/böngésző segítségével jelentkezz be, tokent soha ne írj fájlba.
4. Futtasd az alábbi parancsokat. Commit előtt nézd meg a `git status` eredményét; push csak tisztázott jogosultságokkal. Ha a tároló már létezik, ne force pusholj; előbb egyeztesd a meglévő tartalmat.
```powershell
git init -b main
git add .
git status
git commit -m "Add verified V10 documentation package"
git remote add origin https://github.com/DuczaPeter/spg-nyx-i-ore-map.git
git push -u origin main
```
5. GitHub → Actions → Verify V10 integrity: nézd meg az eredményt. A workflow definíció nem igazol GitHubon lefutott tesztet. Hiba esetén az okot javítsd, ne az elvárt hash-t.

## B lehetőség — GitHub Desktop
Telepítsd a [GitHub Desktopot](https://desktop.github.com/), jelentkezz be. File → Add Local Repository → válaszd ki a helyi mappát; ha még nem Git-tároló, hozd létre ott (ne készíts alá egy másik mappát). Ellenőrizd a változásokat, commit main ágra, Publish repository; ha megengedett, maradjon privát, a fenti névvel. Már létrehozott tárolónál előbb klónozd, másold bele a csomagot, commit és push. Ne duplikáld a tárolót és ne force pusholj.

## Releases alternatíva
Tisztázott engedélyek után: Releases → Draft a new release → `v10` tag → ellenőrzött main commit → cím `V10 documentation release` → csatold a pontos HTML-fájlt → a kiadási jegyzetben add meg az SHA-256-ot: `068b865c6327ab3000e3db41aad2fa5a286b5494bb434e0a78d5249277b5bd04` → publikálás. Tervezett letöltési cím: [V10 Release fájl](https://github.com/DuczaPeter/spg-nyx-i-ore-map/releases/download/v10/sPg_Nyx_I_V10_dokumentalt.html) (publikálásig nem aktív). Ha az HTML kizárólag a Releases alatt van, a Gitből klónozott workflow nem tudja ellenőrizni; ennél a csomagnál tartsd meg a hiteles HTML-t a Gitben is, vagy külön, jóváhagyott asset-letöltési workflow-t kell tervezni. A csak Release-ből történő terjesztés nem ad Pages tárhelyet. Ne töröld a követett példányt az ellenőrzés áttervezése nélkül.

## GitHub Pages
Csak tisztázott jogok után: Settings → Pages → Deploy from a branch → `main` → `/(root)` → Save. A mellékelt `.nojekyll` statikus fájlként szolgálja ki a tartalmat. Mivel az egyetlen HTML megtartotta az eredeti nevét, a közvetlen demócím [https://duczapeter.github.io/spg-nyx-i-ore-map/sPg_Nyx_I_V10_dokumentalt.html](https://duczapeter.github.io/spg-nyx-i-ore-map/sPg_Nyx_I_V10_dokumentalt.html), nem feltétlenül a gyökér URL. Várd meg a Pages telepítés befejezését, nyisd meg a közvetlen URL-t és teszteld. A Pages privát tárolónál is lehet nyilvános; ne kapcsold be csak privát tartalom teszteléséhez. Ingyenes csomagban a Pages nyilvános tárolóhoz használható. A csomagban nincs bekapcsolt tárhely vagy automatikus publikálás.

## Letöltés ellenőrzése
```powershell
Get-FileHash ./sPg_Nyx_I_V10_dokumentalt.html -Algorithm SHA256
```
Elvárt: `068b865c6327ab3000e3db41aad2fa5a286b5494bb434e0a78d5249277b5bd04` (kis-/nagybetű nem számít). Eltérés esetén ne használd.

- [GitHub nagyfájl-korlátok](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github)
- [GitHub Releases](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases)
- [Pages korlátai](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits) · [Pages beállítása](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)
