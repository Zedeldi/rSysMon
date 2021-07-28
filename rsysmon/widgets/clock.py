"""Widgets to display time-related information."""

import math
from datetime import datetime, timedelta

from rsysmon.widgets import Information


class Clock(Information):
    """Display the current time in the specified format."""

    def __init__(self, format_: str = "%H:%M:%S - %a %d/%m/%Y") -> None:
        """
        Initialise parent Information with clock.

        format_ is a string to pass to strftime.
        """
        super().__init__(lambda: datetime.now().strftime(format_))


class Countdown(Information):
    """
    Display time until given date, prefixed by label.

    If ms is True, include microseconds.
    """

    def __init__(
        self, date: datetime, label: str = "Countdown: ", ms: bool = False
    ) -> None:
        """Initialise parent Information with countdown."""
        super().__init__(lambda: f"{label}{self.get_countdown(date, ms)}")

    @staticmethod
    def get_countdown(date: datetime, ms: bool) -> timedelta:
        """
        Return timedelta for time until date.

        Round up microseconds if ms is False.
        """
        delta = date - datetime.now()
        if not ms:
            delta = timedelta(seconds=math.ceil(delta.total_seconds()))
        return delta
