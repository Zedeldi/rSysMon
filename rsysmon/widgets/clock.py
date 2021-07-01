"""Widgets to display time-related information."""

from datetime import datetime

from rsysmon.widgets import Information


class Clock(Information):
    """Display the current time in the specified format."""

    def __init__(self, format_: str = "%H:%M:%S - %a %d/%m/%Y") -> None:
        """
        Initialise parent Information with clock.

        format_ is a string to pass to strftime.
        """
        super().__init__(lambda: datetime.now().strftime(format_))
