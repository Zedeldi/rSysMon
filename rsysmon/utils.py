"""Collection of helper functions."""

import importlib.util
import subprocess
from types import ModuleType
from typing import Any, Generator, Union


def import_abs_path(path: str, name: str = "module") -> ModuleType:
    """Import and return module at path, with specified name."""
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def flatten_iter(
    data: Union[dict[Any, Any], list[Any], tuple[Any, ...], set[Any]]
) -> Generator[Any, None, None]:
    """Return generator of elements from nested iterables (excl. strings)."""
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
