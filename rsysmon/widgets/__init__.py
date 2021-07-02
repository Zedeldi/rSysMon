"""Collection of generic renderable widgets."""

from typing import Any

from rich.panel import Panel
from rich.pretty import Pretty
from rich.progress import Progress, BarColumn
from rich.text import Text
from rich.tree import Tree


def dict_to_tree(
    widgets: dict[str, list[Any]], title: str = "System information"
) -> Tree:
    """Walk through dictionary and return Tree instance."""
    tree = Tree(title)
    for title, renderables in widgets.items():
        subtree = tree.add(title)
        for renderable in renderables:
            subtree.add(Panel(renderable))
    return tree


class Usage(Progress):
    """Progress bar to show resource usage."""

    def __init__(
        self, function, description: str, total: int = 100, *args, **kwargs
    ) -> None:
        """Initialise progress bar with task."""
        super().__init__(
            "[progress.description]{task.description}",
            BarColumn(finished_style="bar.complete"),  # Remove finished style
            "[progress.percentage]{task.percentage:>3.0f}%",
            *args,
            **kwargs,
        )
        self._function = function
        self._task = self.add_task(description, total=total)

    def update(self, *args, **kwargs) -> None:
        """Set completed value to output of function."""
        super().update(self._task, *args, completed=self._function(), **kwargs)


class Information(Text):
    """Generic textual information supporting styles."""

    def __init__(self, function, style=None) -> None:
        """Initialise parent Text and set attributes."""
        super().__init__()
        self._function = function
        self._style = style

    def update(self) -> None:
        """Update text to output of function if changed."""
        text = self._function()
        if self._text == text:
            return
        self.truncate(0)
        self.append(text, style=self._style)


class PrettyPrint(Pretty):
    """Pretty print an object returned by function."""

    def __init__(self, function) -> None:
        """Initialise parent Pretty and set attributes."""
        super().__init__(None)
        self._function = function

    def update(self) -> None:
        """Update object of parent Pretty object."""
        self._object = self._function()
