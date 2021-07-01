"""Read configuration and start rSysMon."""

import sys
from typing import NoReturn

from rsysmon import run
from rsysmon.config import layout, widgets, UPDATE_INTERVAL, REFRESH_PER_SECOND
from rsysmon.utils import flatten_iter


def main() -> NoReturn:
    """Parse widgets and start live display."""
    widget_list = list(flatten_iter(widgets))
    run(layout, widget_list, UPDATE_INTERVAL, REFRESH_PER_SECOND)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
