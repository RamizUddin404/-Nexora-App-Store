# Publishing an App on NEXORA

NEXORA is hosted on GitHub Pages, which serves static files. It cannot securely receive and store uploaded APKs by itself. The APK helper on the website calculates a local SHA-256 checksum only; it does not upload the selected file.

## Publish an Android APK

1. Build the app and confirm the build completed successfully.
2. Test the APK on a device you control. Confirm the package name, app version, minimum Android version, permissions, and signing details.
3. Calculate and save the SHA-256 checksum. NEXORA's **App Publishing Desk** can calculate it in your browser.
4. Open the app's GitHub repository → **Releases** → **Draft a new release**.
5. Choose a version tag such as `v1.0.0`, add release notes, and attach the APK file as a release asset.
6. Publish the release. Open the release page in a private/incognito browser to confirm that the asset can be downloaded publicly.
7. Add the public release asset URL to the matching entry in the `appCatalog` array in `index.html` using an `apk` field, for example:
   `apk: 'https://github.com/OWNER/REPO/releases/download/v1.0.0/AppName-v1.0.0.apk'`
8. Update the description and installation guide, commit the change to `main`, and confirm the Pages workflow succeeds.

The website's catalogue renderer uses an `apk` URL only when you explicitly add one. Never claim an APK is downloadable until the published asset has been verified.

## Submit an app for review

Anyone can use the [app submission issue form](https://github.com/RamizUddin404/-Nexora-App-Store/issues/new?template=app_submission.yml). The maintainer should verify ownership, source, permissions, release files, version, checksum, and safety before adding an entry to the public catalogue.

## Publishing other downloads

For scripts, archives, and desktop packages, use a GitHub Release asset or a trusted package registry. Add platform, version, file size, checksum, installation steps, and a clear permissions/security note.

## For automatic uploads from the website

A real multi-user upload service requires a backend with authentication, file-size/type limits, malware scanning, moderation, access rules, and durable storage. Do not place a GitHub personal access token, cloud storage secret, or admin credential in `index.html`. A public static site cannot securely perform privileged uploads without a server-side service.
