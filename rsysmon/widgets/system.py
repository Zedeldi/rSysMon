"""Widgets to display system information."""

import os
from datetime import datetime
from itertools import chain
from typing import Optional

import psutil

from rsysmon.widgets import Information, Usage


def get_uname() -> str:
    """Return host and kernel information."""
    info = os.uname()
    return (
        f"Host: {info.nodename}\n"
        f"Kernel: {info.sysname} {info.release} {info.machine}"
    )


def get_uptime() -> str:
    """Return time since system boot."""
    delta = datetime.now() - datetime.fromtimestamp(psutil.boot_time())
    uptime = str(delta).split(".")[0]  # Remove decimal
    return f"Uptime: {uptime}"


def get_sensor_temperature(sensor_name: str) -> Optional[float]:
    """Return current temperature of sensor_name."""
    temperatures = chain(*psutil.sensors_temperatures().values())
    for temp in temperatures:
        if temp.label == sensor_name:
            return temp.current
    else:
        return None


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


class Uptime(Information):
    """Display system uptime since boot."""

    def __init__(self) -> None:
        """Initialise parent Information with uptime."""
        super().__init__(get_uptime)


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


class SensorTemperature(Information):
    """Display sensor temperature of specified name."""

    def __init__(self, sensor_name: str, label: str = "Temperature: ") -> None:
        """Initialise parent Information with sensor temperature."""
        super().__init__(
            lambda: f"{label}{temperature}°C"
            if (temperature := get_sensor_temperature(sensor_name))
            else "Cannot find device"
        )
