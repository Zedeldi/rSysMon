"""rSysMon configuration file."""

from rich.layout import Layout
from rich.panel import Panel
from rich.text import Text

from rsysmon.widgets import dict_to_tree
from rsysmon.widgets.clock import Clock
from rsysmon.widgets.disk import DiskUsage, DiskIO
from rsysmon.widgets.media import NowPlaying, Lyrics
from rsysmon.widgets.network import NetworkAddress, NetworkIO
from rsysmon.widgets.system import Username, SystemInfo, CPUUsage, RAMUsage


# Constants
TITLE = "rSysMon - a Rich System Monitor"
UPDATE_INTERVAL = 1
REFRESH_PER_SECOND = 2


# Widgets
widgets = {
    "Tree": {
        "General": [Clock()],
        "System": [
            Username(),
            SystemInfo(),
            CPUUsage(),
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
        "Media": [NowPlaying()],
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
