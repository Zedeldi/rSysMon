"""Widgets to monitor disk status."""

import human_readable
import psutil

from rsysmon.widgets import Usage, Information


def get_disk_io() -> str:
    """Return disk I/O statistics."""
    stats = psutil.disk_io_counters()
    read = human_readable.file_size(stats.read_bytes, binary=True)
    write = human_readable.file_size(stats.write_bytes, binary=True)
    return f"Read: {read}\nWrite: {write}"


class DiskUsage(Usage):
    """Usage bar indicating used storage space."""

    def __init__(self, mountpoint: str, label: str = None) -> None:
        """
        Initialise parent Usage and create function for mountpoint.

        If label is not specified, use mountpoint.
        """
        if not label:
            label = mountpoint
        super().__init__(
            lambda: psutil.disk_usage(mountpoint).used,
            label,
            total=psutil.disk_usage(mountpoint).total,
            expand=True,
        )


class DiskIO(Information):
    """Show I/O statistics about all disks."""

    def __init__(self) -> None:
        """Initialise parent Information with disk I/O."""
        super().__init__(get_disk_io)
