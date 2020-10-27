# Firefox LauncherEntry Integration

Adds download count and progress to any dock/panel compatible with Unity's LauncherEntry specification.

## Dependencies

- python3
- python3-gi
- glib

## Installation

Install the Firefox extension at: www.example.com.

Then place `firefox_launcherentry_integration.py` and `firefox_launcherentry_integration.json` in the `/usr/lib/mozilla/native-messaging-hosts/` directory to install the host application. You need to make `firefox_launcherentry_integration.py` executable.

Alternatively you can use this command:

```bash
sudo curl -s --create-dirs "https://raw.githubusercontent.com/mpostaire/firefox-launcherentry-integration/master/app/firefox_launcherentry_integration.{py,json}" -o "/usr/lib/mozilla/native-messaging-hosts/firefox_launcherentry_integration.#1" && sudo chmod +x /usr/lib/mozilla/native-messaging-hosts/firefox_launcherentry_integration.py
```
