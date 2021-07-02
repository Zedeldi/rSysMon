"""
Widgets to provide compatibility with py3status.

Requires py3status to be installed.
"""

from importlib import import_module
from typing import Any, Optional

from py3status.core import Module
from py3status.module_test import MockPy3statusWrapper

from rsysmon.widgets import Information


def get_py3status_class(module_name: str):
    """
    Return the Py3status class with name module_name.

    Raise ModuleNotFoundError if py3status is not installed
    or module_name is invalid.
    """
    return import_module(f"py3status.modules.{module_name}").Py3status


def get_py3status_module(
    module_class, config: Optional[dict[str, Any]] = None
) -> Module:
    """Return py3status Module instance with config."""
    if not config:
        config = {}

    py3_config = {
        "general": {
            "color_bad": "#FF0000",
            "color_degraded": "#FFFF00",
            "color_good": "#00FF00",
        },
        "py3status": {},
        ".module_groups": {},
        "py3status_module": config,
    }

    wrapper = MockPy3statusWrapper(py3_config)

    module = module_class()
    m = Module("py3status_module", {}, wrapper, module)
    m.prepare_module()
    return m


def get_py3status_output(module: Module) -> str:
    """Run module and return latest output."""
    module.run()
    try:
        output = module.get_latest()[0]["full_text"]
    except (IndexError, KeyError):
        output = ""
    return output


class Py3statusCompat(Information):
    """Provide Information class compatible with py3status modules."""

    def __init__(
        self, module_name: str, config: Optional[dict[str, Any]] = None
    ) -> None:
        """Initialise py3status module and parent Information with output."""
        module_class = get_py3status_class(module_name)
        self._module = get_py3status_module(module_class, config)
        super().__init__(lambda: get_py3status_output(self._module))
