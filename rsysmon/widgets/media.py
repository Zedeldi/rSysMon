"""Widgets to display media information."""

import subprocess
from typing import Optional

from rsysmon.widgets import Information


def get_song_info() -> tuple[str, str]:
    """
    Return song title and artist.

    Requires playerctl to be installed.
    """
    title = (
        subprocess.check_output(["playerctl", "metadata", "title"])
        .decode()
        .strip("\n")
    )
    artist = (
        subprocess.check_output(["playerctl", "metadata", "artist"])
        .decode()
        .strip("\n")
    )
    return (title, artist)


def get_lyrics() -> str:
    """
    Return lyrics for the currently playing song.

    Requires playerctl and clyrics to be installed.
    """
    lyrics = subprocess.check_output(["clyrics", *get_song_info()]).decode()
    return lyrics


class NowPlaying(Information):
    """
    Display track information of currently playing song.

    Metadata is separated by separator.
    """

    def __init__(self, separator: str = " - ") -> None:
        """Initialise parent Information with song information."""
        super().__init__(lambda: separator.join(get_song_info()))


class Lyrics(Information):
    """Display lyrics of currently playing song."""

    def __init__(self) -> None:
        """Initialise parent Information with lyrics."""
        super().__init__(get_lyrics)
        self._song_info: Optional[tuple[str, str]] = None

    def update(self) -> None:
        """Update lyrics if the song has changed."""
        if self._song_info != (info := get_song_info()):
            self._song_info = info
            super().update()
