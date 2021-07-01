"""Widgets to display system information."""

import os

import psutil

from rsysmon.widgets import Usage, Information


def get_uname() -> str:
    """Return host and kernel information."""
    info = os.uname()
    return (
        f"Host: {info.nodename}\n"
        f"Kernel: {info.sysname} {info.release} {info.machine}"
    )


class Username(Information):
    """Display username of current user."""

    def __init__(self, label: str = "Username: ") -> None:
        """Initialise parent Information with username."""
        super().__init__(lambda: f"{label}{os.getlogin()}")


class SystemInfo(Information):
    """Display system information from uname."""

    def __init__(self) -> None:
        """Initialise parent Information with uname function."""
        super().__init__(get_uname)


class CPUUsage(Usage):
    """Display CPU usage as a percentage bar."""

    def __init__(self, label: str = "CPU") -> None:
        """Initialise parent Usage with CPU percent."""
        super().__init__(psutil.cpu_percent, label, expand=True)


class RAMUsage(Usage):
    """Display memory usage as percentage bar."""

    def __init__(self, label: str = "RAM") -> None:
        """Initialise parent Usage with virtual memory percentage."""
        super().__init__(
            lambda: psutil.virtual_memory().percent, label, expand=True
        )