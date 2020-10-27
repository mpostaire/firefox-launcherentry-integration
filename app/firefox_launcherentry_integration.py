#!/usr/bin/python3

import sys
import json
import struct
from gi.repository import GLib, Gio


def update(count, progress, bus):
    data = GLib.Variant("a{sv}", {
        "count": GLib.Variant("x", count),
        "count-visible": GLib.Variant("b", count > 0),
        "progress": GLib.Variant("d", progress),
        "progress-visible": GLib.Variant("b", count > 0 and progress > 0)
    })
    params = GLib.Variant.new_tuple(
        GLib.Variant("s", "application://firefox.desktop"),
        data
    )
    bus.emit_signal(None, "/com/canonical/unity/launcherentry",
                    "com.canonical.Unity.LauncherEntry", "Update", params)


def getMessage(source, condition, data):
    text_length_bytes = source.read(4)
    if len(text_length_bytes) == 0:
        return False

    text_length = struct.unpack('@I', text_length_bytes)[0]
    text = source.read(text_length).decode('utf-8')
    msg = json.loads(text)

    parsed = msg.split(":")
    update(int(parsed[0]), float(parsed[1]), data)

    return True


if __name__ == "__main__":
    bus = Gio.bus_get_sync(Gio.BusType.SESSION)
    stdin = GLib.IOChannel.unix_new(sys.stdin.fileno())
    stdin.set_encoding(None)
    stdin.set_buffered(False)
    GLib.io_add_watch(stdin, GLib.PRIORITY_DEFAULT,
                      GLib.IOCondition.IN, getMessage, bus)

    loop = GLib.MainLoop()
    loop.run()
