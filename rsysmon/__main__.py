"""Read configuration and start rSysMon."""

import sys
from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser
from typing import NoReturn

from rsysmon import run
from rsysmon.utils import flatten_iter, import_abs_path


def main() -> NoReturn:
    """Parse arguments and widgets, then start live display."""
    parser = ArgumentParser(
        prog="rsysmon",
        description="rSysMon - Copyright (C) 2021 Zack Didcott",
        formatter_class=ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "-c",
        "--config",
        type=str,
        default="config_example.py",
        help="path to configuration file",
    )

    args = parser.parse_args()
    config = import_abs_path(args.config)

    widget_list = list(flatten_iter(config.widgets))
    try:
        run(
            config.layout,
            widget_list,
            config.UPDATE_INTERVAL,
            config.REFRESH_PER_SECOND,
        )
    except KeyboardInterrupt:
        sys.exit(0)


if __name__ == "__main__":
    main()
