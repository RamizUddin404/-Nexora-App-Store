# NEXORA — Your Digital Universe

A responsive, motion-rich digital project storefront for showcasing apps, AI experiments, websites, and developer utilities.

**Live preview:** enable GitHub Pages in repository settings and select the `main` branch / root folder.

## Design principles

- Deep-space palette with cyan and violet accents
- CSS orbital emblem and floating 3D-inspired hero
- Responsive project cards with subtle pointer tilt
- Search, category filters, saved projects, and theme switch
- Add-project modal with browser-local persistence
- Reduced-motion accessibility support
- Safe URL validation and escaped project text rendering

## Run locally

Open `index.html` in a modern browser, or serve this directory with any static web server.

## Important current scope

This first version is a **front-end showcase**, not a production multi-user app marketplace. Custom projects and saved items are stored in the current browser using localStorage. They do not automatically sync to GitHub or other devices. The starter catalogue includes illustrative project entries; verify each project's actual availability and destination before presenting it as a live product.

## Publish with GitHub Pages

1. Open repository **Settings → Pages**.
2. Choose **Deploy from a branch**.
3. Select branch `main` and folder `/(root)`.
4. Save and wait for the Pages build to complete.

The published URL will be shown in the Pages settings when deployment is ready.

## Suggested next production milestones

1. Connect an authenticated admin backend and database.
2. Add a verified GitHub repository importer and release/version metadata.
3. Add real screenshots, changelogs, downloads, and privacy information for each project.
4. Add abuse-resistant reviews and ratings (without fabricated reviews).
5. Add CI checks, accessibility testing, and performance budgets.

## Security notes

Do not place API keys or privileged credentials in this static front-end. A production admin workflow must use server-side authentication and authorization. Review every external download and source link before listing it.

Built for Ramiz Uddin.
