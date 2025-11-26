# Copyright [2025] Rufai Limantawa <rufailimantawa@gmail.com>

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from dataclasses import dataclass
from typing import Iterator
from .token import Span

# Errors
ERR_SUBSTRING_OUT_OF_BOUNDS = IndexError("Substring indices are out of bounds.")
ERR_INVALID_SOURCE_TYPE = TypeError("Source must be a string.")
ERR_INVALID_POSITION_RANGE = ValueError("Invalid position range")
ERR_INVALID_POSITION_LINE_COLUMN = ValueError(
    "Line and column numbers must be positive integers"
)

# EOF character constant
EOF = "\0"


@dataclass(frozen=True, slots=True)
class Position:
    """A position in the character stream."""

    start: int
    end: int
    line: int
    column: int

    def __post_init__(self) -> None:
        if self.start < 0 or self.end < self.start:
            raise ERR_INVALID_POSITION_RANGE
        if self.line < 1 or self.column < 1:
            raise ERR_INVALID_POSITION_LINE_COLUMN

    def span(self) -> Span:
        """Get the span from this position."""
        return Span(self.start, self.end, self.line, self.column)


@dataclass(frozen=True, slots=True)
class CharStream:
    """A single character stream with position tracking."""

    source: str
    chars: list[str]
    current_index: int
    line: int
    column: int

    def __init__(self, source: str):
        object.__setattr__(self, "source", source)
        object.__setattr__(self, "chars", list(source))
        object.__setattr__(self, "current_index", 0)
        object.__setattr__(self, "line", 1)
        object.__setattr__(self, "column", 1)
        self.__post_init__()

    def __post_init__(self) -> None:
        if not isinstance(self.source, str):
            raise ERR_INVALID_SOURCE_TYPE

    def advance(self) -> tuple[int, str, Position]:
        """Advance to the next character and return it with its position."""
        idx, ch, pos = self.peek()
        if ch != EOF:
            object.__setattr__(self, "current_index", self.current_index + 1)

        if ch == "\n":
            object.__setattr__(self, "line", self.line + 1)
            object.__setattr__(self, "column", 1)
        else:
            object.__setattr__(self, "column", self.column + 1)
        return idx, ch, pos

    def is_eof(self) -> bool:
        """Check if the stream has reached EOF."""
        return self.current_index >= len(self.chars)

    def peek(self) -> tuple[int, str, Position]:
        """Peek the next character without consuming it."""
        if self.current_index < len(self.chars):
            return (
                self.current_index,
                self.chars[self.current_index],
                Position(
                    self.current_index,
                    self.current_index + 1,
                    self.line,
                    self.column,
                ),
            )
        else:
            return (
                len(self.source),
                EOF,
                Position(
                    len(self.source),
                    len(self.source),
                    self.line,
                    self.column,
                ),
            )  # EOF position

    def sub(self, start: int, end: int) -> str:
        """Get a substring from the source."""
        if start < 0 or end > len(self.source) or start > end:
            raise ERR_SUBSTRING_OUT_OF_BOUNDS
        return self.source[start:end]

    def __iter__(self) -> Iterator[tuple[int, str, Position]]:
        line = col = 1
        for idx, ch in enumerate(self.source):
            pos = Position(idx, idx + 1, line, col)
            yield idx, ch, pos
            if ch == "\n":
                line += 1
                col = 1
            else:
                col += 1
        # EOF character
        yield (
            len(self.source),
            EOF,
            Position(len(self.source), len(self.source), line, col),
        )
