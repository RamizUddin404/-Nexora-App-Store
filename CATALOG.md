# NEXORA Catalogue

This file documents the public projects currently represented in the NEXORA app and tool catalogue. The catalogue is curated rather than a blind execution launcher.

## Included public projects

| Project | Type | Current access |
|---|---|---|
| Neon Toolkit | Termux / Python | Setup commands and individual-tool guide |
| Android Master Tool | Android / ADB | Setup guide; review device-control actions carefully |
| JarvisApp | Android source | Build workflow / artifact check |
| AI Voice Assistant | Android source | Build workflow / artifact check |
| New App / MYRA | Android source | Source and build guidance |
| Life OS | Android source | Source and build guidance |
| Neuralink Voice Assistant | Android source | Build workflow / artifact check |
| NextDNS App Manager | Android / Expo | Build workflow / artifact check |
| Video Tool Suite | Web / Python | Deployment guide |
| Movies Hub | Web | Source and environment setup guide |
| Blood Donation BD | Web | Browser/source guide; real donor data requires privacy controls |
| Android Files Utilities | Shell scripts | Inspect-first setup guide |
| My Scripts | Python / shell | Inspect-first setup guide |
| Video Downloader Pro | Web / Python | Source guide; only use for authorized media |
| NEXORA Tool Lab | Browser tools | Base64, JSON, URL encoding, SHA-256 |

## Browser-native tools

The Tool Lab runs the following operations locally in the browser:

- Base64 encode/decode
- JSON parse, format and minify
- URL component encode/decode
- SHA-256 text digest

No input is intentionally sent to a backend by these tools. Avoid entering secrets into any shared or public computer.

## Repository visibility

Private repositories are not listed in the public catalogue. Making private source or releases public requires a deliberate visibility and release decision by the owner.

## Security and safety curation

Some legacy repositories contain mixed-purpose or high-risk scripts. NEXORA does not offer one-click execution for modules designed for unauthorized access, credential theft, spoofing, surveillance, or disruptive activity. Use diagnostic and administration tools only on devices and systems you own or have explicit permission to test.

## APK availability

Source code is not an installable APK. A project is marked as directly downloadable only after a public release asset is published and the URL is verified. GitHub Actions artifacts may expire; use a GitHub Release for stable public downloads.
