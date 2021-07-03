# rSysMon

[![GitHub license](https://img.shields.io/github/license/Zedeldi/rSysMon?style=flat-square)](https://github.com/Zedeldi/rSysMon/blob/master/LICENSE) [![GitHub last commit](https://img.shields.io/github/last-commit/Zedeldi/rSysMon?style=flat-square)](https://github.com/Zedeldi/rSysMon/commits) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square)](https://github.com/psf/black)

An extensible rich system monitor.

## Description

rSysMon is a system monitor for your terminal, which uses `rich` for a styled output. The screen is implemented using a [`Live`](https://rich.readthedocs.io/en/latest/live.html) display, showing a renderable [`Layout`](https://rich.readthedocs.io/en/latest/layout.html) object -- though any renderable object is supported.

Compatibility with [py3status](https://github.com/ultrabug/py3status) modules is provided through `rsysmon.widgets.py3status`. To create a widget from a py3status module, use `Py3statusCompat("module_name")`.

## Configuration

An example configuration file is located at `config_example.py`. Currently, the file must contain a `layout` object, an iterable of `widgets` to refresh, and constants `UPDATE_INTERVAL` & `REFRESH_PER_SECOND`.

## Installation

1. Clone: `git clone https://github.com/Zedeldi/rSysMon.git`
2. Install build: `pip3 install build`
3. Build: `python3 -m build`
4. Install wheel: `pip3 install dist/rSysMon-*-py3-none-any.whl`
5. Run: `rsysmon -c /path/to/config.py`

Alternatively, to try rSysMon with the default settings, run `python -m rsysmon`.

Libraries:

- [rich](https://pypi.org/project/rich/) - Rich terminal graphics
- [psutil](https://pypi.org/project/psutil/) - System information
- [human-readable](https://pypi.org/project/human-readable/) - Humanisation of large numbers

## Contributing

To contribute to rSysMon, add new widgets to `rsysmon/widgets/` in the relevant file (feel free to create a new one if necessary). Any other improvements are also welcome. Code is formatted with [`black`](https://github.com/psf/black).

## Todo

- Colour support

## License

rSysMon is licensed under the GPL v3 for everyone to use, modify and share freely.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

[![GPL v3 Logo](https://www.gnu.org/graphics/gplv3-127x51.png)](https://www.gnu.org/licenses/gpl-3.0-standalone.html)

## Donate

If you found this project useful, please consider donating. Any amount is greatly appreciated! Thank you :smiley:

My bitcoin address is: [bc1q5aygkqypxuw7cjg062tnh56sd0mxt0zd5md536](bitcoin://bc1q5aygkqypxuw7cjg062tnh56sd0mxt0zd5md536)
