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


@dataclass(frozen=True, slots=True)
class Position:
    """A position in the character stream."""

    start: int
    end: int
    line: int
    column: int

    def span(self) -> Span:
        """Get the span from this position."""
        return Span(self.start, self.end, self.line, self.column)


@dataclass(frozen=True, slots=True)
class CharStream:
    """A single character stream with position tracking."""

    source: str

    def __post_init__(self):
        if not isinstance(self.source, str):
            raise TypeError("source must be a string")

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
