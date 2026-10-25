# Contributing to NEXORA

Thanks for helping improve NEXORA.

## Before opening a change

1. Search existing issues to avoid duplicates.
2. For a bug, include steps to reproduce, expected behavior, actual behavior, and browser/device details.
3. For a feature, explain the user problem and the smallest useful solution.
4. Do not include passwords, API keys, personal data, or private URLs in issues or commits.

## Development

NEXORA is currently a static HTML/CSS/vanilla JavaScript project.

- Edit `index.html` for the storefront.
- Keep the experience responsive and keyboard accessible.
- Prefer semantic HTML and dependency-free solutions where practical.
- Validate external URLs and escape user-provided text before rendering it.
- Respect the `prefers-reduced-motion` setting.
- Do not add secrets to frontend code.

Run the local checks with:

```bash
python scripts/check_site.py
```

Open `index.html` in a modern browser or run `python -m http.server 8080` to preview it.

## Pull requests

Keep changes focused, describe user-visible changes, and list the checks you ran. Do not claim that a feature is tested if it was not tested.
