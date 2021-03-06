"""
rSysMon configuration file.

Required attributes:
    UPDATE_INTERVAL - how frequently to update widgets
    REFRESH_PER_SECOND - passed to the Live object
    widgets - an iterable of renderable objects
    layout - a renderable object with widgets
"""

from typing import Any

from rich.layout import Layout
from rich.panel import Panel
from rich.text import Text

from rsysmon.widgets import dict_to_tree
from rsysmon.widgets.clock import Clock
from rsysmon.widgets.disk import DiskIO, DiskUsage
from rsysmon.widgets.media import Lyrics, NowPlaying
from rsysmon.widgets.network import NetworkAddress, NetworkIO
from rsysmon.widgets.py3status import Py3statusCompat
from rsysmon.widgets.system import (
    CPUUsage,
    RAMUsage,
    SensorTemperature,
    SystemInfo,
    Uptime,
    Username,
)

# Constants
TITLE = "rSysMon - a Rich System Monitor"
UPDATE_INTERVAL = 1
REFRESH_PER_SECOND = 2


# Widgets
widgets: dict[str, Any] = {
    "Tree": {
        "General": [Clock()],
        "System": [
            Username(),
            SystemInfo(),
            Uptime(),
            CPUUsage(),
            SensorTemperature(sensor_name="Core 0", label="CPU "),
            RAMUsage(),
        ],
        "Disk": [
            DiskUsage("/"),
            DiskUsage("/home"),
            DiskIO(),
        ],
        "Network": [
            NetworkAddress("eno1"),
            NetworkIO(),
        ],
        "Media": [
            NowPlaying(),
            Py3statusCompat(
                "volume_status", config={"cache_timeout": UPDATE_INTERVAL}
            ),
        ],
    },
    "Main": Lyrics(),
}

# Layout
layout = Layout()

layout.split_column(
    Layout(name="title"),
    Layout(name="body"),
)

layout["title"].size = 3
layout["title"].update(Text(f"\n{TITLE}", style="bold", justify="center"))

layout["body"].split_row(
    Layout(name="left"),
    Panel(widgets["Main"]),
)

layout["left"].size = 60
tree = dict_to_tree(widgets["Tree"])
layout["left"].update(Panel(tree))
