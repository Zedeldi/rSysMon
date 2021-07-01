"""Widgets to display media information."""

import subprocess

from rsysmon.widgets import Information


def get_song_info() -> tuple[str, str]:
    """
    Return song title and artist.

    Requires playerctl to be installed.
    """
    title = (
        subprocess.Popen(
            ["playerctl", "metadata", "title"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        .stdout.read()
        .decode()
        .strip("\n")
    )
    artist = (
        subprocess.Popen(
            ["playerctl", "metadata", "artist"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        .stdout.read()
        .decode()
        .strip("\n")
    )
    return (title, artist)


def get_lyrics(song_info: tuple[str, str]) -> str:
    """
    Return lyrics for the currently playing song.

    Requires playerctl and clyrics to be installed.
    """
    lyrics = (
        subprocess.Popen(
            ["clyrics", *song_info],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        .stdout.read()
        .decode()
    )
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
            if any(info := get_song_info())
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
        if self._song_info != (info := get_song_info()):
            self._song_info = info
            super().update()
