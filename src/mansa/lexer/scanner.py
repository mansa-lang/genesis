from dataclasses import dataclass
from enum import StrEnum, auto
from typing import NamedTuple


class Span(NamedTuple):
    """Zero-cost source location (start, end, line, column)."""

    start: int
    end: int
    line: int
    column: int
