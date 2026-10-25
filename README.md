<div align="center">

# ✦ NEXORA — Your Digital Universe

**Discover apps, AI experiments, websites, and tools made by curious builders.**

[![Deploy to GitHub Pages](https://github.com/RamizUddin404/-Nexora-App-Store/actions/workflows/pages.yml/badge.svg)](https://github.com/RamizUddin404/-Nexora-App-Store/actions/workflows/pages.yml)
[![CodeQL](https://github.com/RamizUddin404/-Nexora-App-Store/actions/workflows/codeql.yml/badge.svg)](https://github.com/RamizUddin404/-Nexora-App-Store/actions/workflows/codeql.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-65f0e1.svg)](LICENSE)
[![Static HTML](https://img.shields.io/badge/Stack-HTML%20%7C%20CSS%20%7C%20JavaScript-7195ff.svg)](#-technology)

### 🌐 [Open NEXORA](https://ramizuddin404.github.io/-Nexora-App-Store/)

[Website](https://ramizuddin404.github.io/-Nexora-App-Store/) · [Report a bug](https://github.com/RamizUddin404/-Nexora-App-Store/issues/new?template=bug_report.yml) · [Request a feature](https://github.com/RamizUddin404/-Nexora-App-Store/issues/new?template=feature_request.yml)

</div>

---

## Overview

NEXORA is a responsive, motion-rich **digital project showcase** designed to help people discover apps, AI concepts, websites, Android experiments, and developer utilities. It uses a deep-space visual system, cyan/violet accents, animated orbital artwork, and interactive project cards.

> **Project status:** Front-end showcase. It is not yet a production multi-user marketplace. See [Current scope and limitations](#-current-scope-and-limitations).

## ✨ Features

- **Responsive storefront** designed for desktop and mobile screens
- **Animated visual identity** with CSS orbital effects and 3D-inspired interactions
- **Project discovery** with search and category filters
- **Saved projects** with a browser-local saved list
- **Add-project form** with basic input validation and URL protocol checks
- **Project details modal** with source/demo links when supplied
- **Light/dark theme toggle** with browser-local preference
- **Keyboard-friendly dialogs** with Escape-to-close support
- **Reduced-motion consideration** for pointer-based card effects
- **GitHub Actions deployment** for GitHub Pages
- **CodeQL workflow** for repository security analysis

## 🚀 Live website

**Production URL:** <https://ramizuddin404.github.io/-Nexora-App-Store/>

If the site does not open yet, check the [deployment workflow](https://github.com/RamizUddin404/-Nexora-App-Store/actions/workflows/pages.yml) and the repository's [Pages settings](https://github.com/RamizUddin404/-Nexora-App-Store/settings/pages). The link becomes usable after the first successful deployment finishes.

## 🧭 Getting started

No Node.js, package manager, build step, or API key is required for the current static version.

1. Open or download this repository.
2. Open `index.html` in a modern browser.
3. Or serve the repository root using any static web server.

### Run in Termux

```bash
pkg update
pkg install python
git clone https://github.com/RamizUddin404/-Nexora-App-Store.git
cd -Nexora-App-Store
python -m http.server 8080
```

Then open <http://127.0.0.1:8080> in your phone's browser.

## 🛠 Technology

- Semantic HTML
- CSS custom properties, responsive layouts, animation and transitions
- Vanilla JavaScript (no framework or build tooling)
- Browser `localStorage` for local preferences and saved/custom showcase items
- GitHub Actions and GitHub Pages for publishing

## 📦 Deployment

The repository contains a workflow at [`.github/workflows/pages.yml`](.github/workflows/pages.yml).

1. Open [Repository Settings → Pages](https://github.com/RamizUddin404/-Nexora-App-Store/settings/pages).
2. Under **Build and deployment**, set **Source** to **GitHub Actions**.
3. Save the setting if GitHub displays a Save button.
4. Open [Actions](https://github.com/RamizUddin404/-Nexora-App-Store/actions).
5. Wait for **Deploy NEXORA to GitHub Pages** to complete successfully.
6. Open the production URL linked above.

Every push to `main` triggers the deployment workflow. A manual run is also available through the workflow's **Run workflow** control.

## 🧪 Quality checks

A lightweight HTML check runs before publishing to catch malformed essentials, duplicate static IDs, and missing local files. CodeQL runs separately for repository analysis. These checks help catch common issues; they do not replace cross-browser, accessibility, or real-device testing.

## 🔒 Current scope and limitations

NEXORA is currently a **static showcase**, not a complete app marketplace backend.

- Projects added through the form are stored only in the current browser's `localStorage`; they are not published to the shared website and do not sync across devices.
- Saved projects and theme preference are local to the current browser.
- The starter catalogue includes project concepts. Verify availability, ownership, release status, and destination links before treating any entry as an official product.
- There is no user account system, shared database, moderation queue, server-side admin panel, review system, or secure upload/download pipeline yet.
- Do not enter passwords, API keys, private URLs, or other secrets into this static site.

A production marketplace requires a trusted backend, authentication and authorization, database rules, moderation/abuse controls, verified project metadata, and an appropriate privacy policy. Never put privileged credentials in client-side JavaScript.

## 🗺 Roadmap

- [ ] Connect a database for a shared catalogue
- [ ] Add authenticated administrator tools and server-side authorization
- [ ] Import public GitHub repository metadata with rate-limit handling
- [ ] Add verified releases, changelogs, screenshots, and platform labels
- [ ] Add review/reporting and moderation workflows
- [ ] Expand automated accessibility and browser testing
- [ ] Add privacy and content policies before collecting user data

## 🤝 Contributing

Suggestions and bug reports are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md), then open an issue with reproducible details. Please do not submit credentials or personal data in issues.

## 📄 License

Distributed under the [MIT License](LICENSE).

---

<div align="center">

**Built with curiosity by Ramiz Uddin** · [GitHub profile](https://github.com/RamizUddin404)

</div>
