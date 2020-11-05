# Firefox LauncherEntry Integration

Adds firefox's download count and progress to any dock/panel compatible with Unity's LauncherEntry specification.

## Dependencies

- python3
- python3-gi
- glib

## Installation

Install the Firefox extension at: https://addons.mozilla.org/fr/firefox/addon/launcherentry-integration/.

Then use this command:

```bash
sudo mkdir --parents --mode=g+r,o+r /usr/lib/mozilla/native-messaging-hosts && sudo curl -s "https://raw.githubusercontent.com/mpostaire/firefox-launcherentry-integration/master/app/firefox_launcherentry_integration.{py,json}" -o "/usr/lib/mozilla/native-messaging-hosts/firefox_launcherentry_integration.#1" && sudo chmod +x /usr/lib/mozilla/native-messaging-hosts/firefox_launcherentry_integration.py
```

It downloads `firefox_launcherentry_integration.py` and `firefox_launcherentry_integration.json` into the `/usr/lib/mozilla/native-messaging-hosts/` directory to install the host application and sets `firefox_launcherentry_integration.py` as executable. Of course you can do this step manually if you don't trust copy/pasting commands.
