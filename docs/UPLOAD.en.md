[English](UPLOAD.en.md) | [Magyar](UPLOAD.hu.md) · [README](../README.md)

# Upload and publish (only after rights clearance)
The HTML is 40,845,886 bytes (~38.95 MiB). GitHub browser upload is limited to 25 MiB per file; regular Git blocks files above 100 MiB, so this file fits regular Git. Release assets must be under 2 GiB. Pages sites must be at most 1 GB; the package fits the size limits, but rights/plan/settings still apply.

## Option A — Git command line
1. Review [NOTICE](../NOTICE) and [LICENSE](../LICENSE). Obtain the required permissions before uploading game-derived assets. Choose the original-code license. Do not publish until cleared.
2. Create a local folder `spg-nyx-i-ore-map`. Save each delivered file at its exact relative path; enable hidden files to see `.github` and `.gitattributes`. Do not open and resave the HTML. Do not include the source ZIP or generated reconstruction. Install [Git](https://git-scm.com/downloads), Python and Node if needed.
3. In GitHub, create a **new empty** repository named `spg-nyx-i-ore-map` under `DuczaPeter` (private initially, only if upload is permitted). Do not auto-create README, license or gitignore. Open PowerShell inside the local folder. Run `python scripts/verify.py` before committing. Set Git author identity locally if Git prompts; use your preferred GitHub no-reply address instead of publishing personal email. Authenticate via Git Credential Manager/browser, never put a token in a file.
4. Run the following commands. Review `git status` before commit, then push only after permission is established. If the repository already exists, do not force push; reconcile with its contents first.
```powershell
git init -b main
git add .
git status
git commit -m "Add verified V10 documentation package"
git remote add origin https://github.com/DuczaPeter/spg-nyx-i-ore-map.git
git push -u origin main
```
5. Open GitHub → Actions → Verify V10 integrity; inspect the result. A workflow definition is not proof of a hosted run. On failure, fix the cause, not the expected hash.

## Option B — GitHub Desktop
Install [GitHub Desktop](https://desktop.github.com/), sign in. File → Add Local Repository → select the local folder; if it is not a Git repo, create one at that location (do not nest another folder). Review changes, commit to main, Publish repository; keep private if permitted, choose the name above. For an already-created remote, clone it first, copy the package into the clone, commit and push. Do not duplicate the repository or force push.

## Releases alternative
After permissions are clear: Releases → Draft a new release → tag `v10` → target verified main commit → title `V10 documentation release` → attach the exact HTML file → include SHA-256 `068b865c6327ab3000e3db41aad2fa5a286b5494bb434e0a78d5249277b5bd04` in the notes → publish. Planned download URL: [V10 release asset](https://github.com/DuczaPeter/spg-nyx-i-ore-map/releases/download/v10/sPg_Nyx_I_V10_dokumentalt.html) (not active until published). If the HTML is distributed only through Releases instead of Git, the included workflow cannot verify it on checkout; keep the canonical HTML in Git for this package, or design a separate explicitly approved asset-fetch verification workflow. Release-only does not provide Pages hosting. Do not delete the tracked copy without updating the verification design.

## GitHub Pages
Only after rights clearance: Settings → Pages → Deploy from a branch → `main` → `/(root)` → Save. The included `.nojekyll` serves files as static assets. Since the only HTML retains its original filename, the direct demo URL is [https://duczapeter.github.io/spg-nyx-i-ore-map/sPg_Nyx_I_V10_dokumentalt.html](https://duczapeter.github.io/spg-nyx-i-ore-map/sPg_Nyx_I_V10_dokumentalt.html), not necessarily the root URL. Wait for the Pages deployment to finish, then open the direct URL and test it. Pages may be public even for private repos; do not enable it merely to test private assets. Free-plan Pages requires a public repo. No hosting or automatic publishing is configured in this package.

## Check the download
```powershell
Get-FileHash ./sPg_Nyx_I_V10_dokumentalt.html -Algorithm SHA256
```
Expected: `068b865c6327ab3000e3db41aad2fa5a286b5494bb434e0a78d5249277b5bd04` (case-insensitive comparison). If different, do not use it.

- [GitHub large-file limits](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github)
- [GitHub Releases](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases)
- [Pages limits](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits) · [Pages setup](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)
