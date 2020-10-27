# Firefox LauncherEntry Integration

Adds download count and progress to any dock/panel compatible with Unity's LauncherEntry specification.

## Dependencies

- python3
- python3-gi
- glib

## Installation

Install the Firefox extension at: www.example.com.

Then use this command to install the host application:

```bash
curl -s https://raw.githubusercontent.com/mpostaire/firefox-launcherentry-integration/master/app/firefox_launcherentry_integration.py | sudo tee /usr/bin/firefox_launcherentry_integration.py > /dev/null && curl -s https://raw.githubusercontent.com/mpostaire/firefox-launcherentry-integration/master/app/firefox_launcherentry_integration.json | sudo tee /usr/lib/mozilla/native-messaging-hosts/firefox_launcherentry_integration.json > /dev/null
```
