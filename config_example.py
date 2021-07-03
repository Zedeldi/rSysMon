"""rSysMon configuration file."""

from typing import Any

from rich.layout import Layout
from rich.panel import Panel
from rich.text import Text

from rsysmon.widgets import dict_to_tree
from rsysmon.widgets.clock import Clock
from rsysmon.widgets.disk import DiskUsage, DiskIO
from rsysmon.widgets.media import NowPlaying, Lyrics
from rsysmon.widgets.network import NetworkAddress, NetworkIO
from rsysmon.widgets.py3status import Py3statusCompat
from rsysmon.widgets.system import (
    Username,
    SystemInfo,
    Uptime,
    CPUUsage,
    RAMUsage,
    SensorTemperature,
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
