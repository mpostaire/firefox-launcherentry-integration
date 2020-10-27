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
curl https://raw.githubusercontent.com/mpostaire/firefox-launcherentry-integration/master/app/firefox-launcherentry-integration.py | sudo tee /usr/bin/firefox-launcherentry-integration.py && curl https://raw.githubusercontent.com/mpostaire/firefox-launcherentry-integration/master/app/firefox-launcherentry-integration.json | sudo tee /usr/lib/mozilla/native-messaging-hosts/firefox-launcherentry-integration.json
```
