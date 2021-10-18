"""Widgets to display media information."""

from rsysmon.utils import sys_exec
from rsysmon.widgets import Information


def get_song_info() -> tuple[str, str]:
    """
    Return song title and artist.

    Requires playerctl to be installed.
    """
    try:
        title = sys_exec(["playerctl", "metadata", "title"]).strip("\n")
        artist = sys_exec(["playerctl", "metadata", "artist"]).strip("\n")
    except OSError:
        title, artist = "", ""
    return (title, artist)


def get_lyrics(song_info: tuple[str, str]) -> str:
    """
    Return lyrics for the currently playing song.

    Requires clyrics to be installed.
    """
    try:
        lyrics = sys_exec(["clyrics", *song_info])
    except OSError:
        lyrics = ""
    return lyrics


class NowPlaying(Information):
    """
    Display track information of currently playing song.

    Metadata is separated by separator.
    """

    def __init__(
        self, separator: str = " - ", placeholder: str = "Now playing: N/A"
    ) -> None:
        """Initialise parent Information with song information."""
        super().__init__(
            lambda: separator.join(info)
            if all(info := get_song_info())  # Require all info to be present
            else placeholder
        )


class Lyrics(Information):
    """Display lyrics of currently playing song."""

    def __init__(self) -> None:
        """Initialise parent Information with lyrics."""
        super().__init__(lambda: get_lyrics(self._song_info))
        self._song_info: tuple[str, str] = ("", "")

    def update(self) -> None:
        """Update lyrics if the song has changed."""
        if self._song_info != (info := get_song_info()) or not self.plain:
            self._song_info = info
            super().update()
