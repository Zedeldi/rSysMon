"""Collection of helper functions."""

import subprocess
from typing import Any, Union, Generator


def flatten_iter(
    data: Union[dict[Any, Any], list[Any], tuple[Any, ...], set[Any]]
) -> Generator[Any, None, None]:
    """Return list of elements from nested iterables (excluding strings)."""
    if isinstance(data, dict):
        data = list(data.values())
    for item in data:
        if isinstance(item, (dict, list, tuple, set)):  # Exclude strings
            yield from flatten_iter(item)
        else:
            yield item


def sys_exec(command: list[str]) -> str:
    """Return stdout of command, where command is a list of arguments."""
    return (
        subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        .stdout.read()
        .decode()
    )
