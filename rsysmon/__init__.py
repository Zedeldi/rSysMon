"""rSysMon - a Rich System Monitor."""

import time
from typing import Any, NoReturn

from rich.layout import Layout
from rich.live import Live


def run(
    layout: Layout,
    widgets: list[Any],
    update_interval: int,
    refresh_per_second: int,
) -> NoReturn:
    """Start the live display and update widgets every interval."""
    with Live(layout, refresh_per_second=refresh_per_second, transient=True):
        while True:
            for widget in widgets:
                widget.update()
        time.sleep(update_interval)
