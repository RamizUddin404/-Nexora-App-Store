<div align="center">

# ✦ NEXORA — App Store & Tool Lab

**A curated home for Android apps, browser utilities, Termux tools and developer projects.**

[![Deploy to GitHub Pages](https://github.com/RamizUddin404/-Nexora-App-Store/actions/workflows/pages.yml/badge.svg)](https://github.com/RamizUddin404/-Nexora-App-Store/actions/workflows/pages.yml)
[![CodeQL](https://github.com/RamizUddin404/-Nexora-App-Store/actions/workflows/codeql.yml/badge.svg)](https://github.com/RamizUddin404/-Nexora-App-Store/actions/workflows/codeql.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-65f0e1.svg)](LICENSE)

### 🌐 [Open NEXORA](https://ramizuddin404.github.io/-Nexora-App-Store/)

[Repository](https://github.com/RamizUddin404/-Nexora-App-Store) · [App publishing guide](APP_PUBLISHING.md) · [Catalogue](CATALOG.md) · [Submit an app](https://github.com/RamizUddin404/-Nexora-App-Store/issues/new?template=app_submission.yml)

</div>

---

## What NEXORA includes

NEXORA combines a responsive storefront with a local browser Tool Lab and a guided Termux setup area.

### App catalogue

- Curated public projects from the maintainer's repositories
- Search and platform/category filters
- Source repository and build-workflow actions where available
- Clear distinction between source code, build artifacts, and verified public APK releases
- Installation guidance and permissions notes
- An issue form for public app/tool submissions, reviewed before inclusion

### Browser Tool Lab

The following tools run in the user's browser without sending their input to a NEXORA server:

- **Base64 encoder/decoder** — UTF-8-safe text conversion
- **JSON formatter** — validate, pretty-print and minify JSON
- **URL encoder/decoder** — encode or decode URL components
- **SHA-256** — calculate a text digest using the Web Crypto API

### Termux setup guides

Step-by-step command sets are provided for:

- Initial Termux package setup
- Neon Toolkit installation and launch
- Basic network diagnostics
- Python development setup
- Git and repository access

Commands are displayed for review and copying; the website cannot run shell commands on the visitor's phone.

## App publishing and downloads

**A source repository is not an installable app.** An Android APK must be built, tested, and published as a downloadable release asset before NEXORA can offer a stable direct download.

- [Read the app publishing guide](APP_PUBLISHING.md)
- The App Publishing Desk can calculate an APK's size and SHA-256 checksum locally. It does **not** upload the file.
- Use the app submission issue form to propose an app or tool for review.
- Once a public GitHub Release asset is verified, add its URL to the relevant `appCatalog` item as `apk`. The site will then show a direct APK download button.
- GitHub Actions artifacts may expire; a published release is preferred for durable public downloads.

## Catalogue scope and safety

See [CATALOG.md](CATALOG.md) for the current project inventory and curation rules.

Private repositories are not included in the public catalogue. Some mixed-purpose legacy repositories contain high-risk modules; NEXORA does not provide one-click execution for offensive, credential-theft, spoofing, surveillance, or disruptive functionality. Safe diagnostics and authorized administration workflows are preferred.

## Technology

- Semantic HTML, CSS custom properties, responsive design and CSS animation
- Vanilla JavaScript; no frontend build step
- Browser `localStorage` for saved projects, theme and user-added showcase entries
- Web Crypto API for SHA-256
- GitHub Actions for validation and GitHub Pages deployment

## Run locally in Termux

```bash
pkg update
pkg install python git
git clone https://github.com/RamizUddin404/-Nexora-App-Store.git
cd -- -Nexora-App-Store
python -m http.server 8080
```

Open <http://127.0.0.1:8080> in your browser.

## Deploy to GitHub Pages

1. Open [Settings → Pages](https://github.com/RamizUddin404/-Nexora-App-Store/settings/pages).
2. Set **Build and deployment → Source** to **GitHub Actions**.
3. Push changes to `main`, or manually run the [Pages workflow](https://github.com/RamizUddin404/-Nexora-App-Store/actions/workflows/pages.yml).
4. Check the workflow for a successful result, then open <https://ramizuddin404.github.io/-Nexora-App-Store/>.

## Current limitations

NEXORA is a **static site**, not yet a multi-user app marketplace backend.

- Saved items, theme preferences and custom showcase entries are stored in the current browser only.
- The website does not yet accept and store APK uploads on a server.
- The APK helper calculates a local checksum; publishing must happen through a release workflow.
- No account system, secure admin panel, shared database, malware scanning, moderation backend, or automated release ingestion is configured.
- Repository build links do not guarantee that a successful APK artifact exists.
- Before real users submit software, add server-side validation, moderation, storage access rules, rate limits, malware scanning, and privacy terms.

Never put GitHub tokens, API secrets, signing keys, or privileged credentials in client-side JavaScript or public repository files.

## Quality checks

The deployment workflow runs `python scripts/check_site.py` before publishing. This catches common static HTML problems; it does not replace manual browser, mobile, accessibility, and release testing.

## Contributing and security

- [CONTRIBUTING.md](CONTRIBUTING.md)
- [SECURITY.md](SECURITY.md)
- [Report a bug](https://github.com/RamizUddin404/-Nexora-App-Store/issues/new?template=bug_report.yml)
- [Request a feature](https://github.com/RamizUddin404/-Nexora-App-Store/issues/new?template=feature_request.yml)

## License

MIT — see [LICENSE](LICENSE).

<div align="center">

Built with curiosity by Ramiz Uddin · [GitHub profile](https://github.com/RamizUddin404)

</div>
