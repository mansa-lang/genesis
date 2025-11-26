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

"""
Unit tests for the source character stream with position tracking.

These are essential for accurate lexing and error reporting.
"""

import pytest
from mansa.lexer.stream import CharStream, EOF as StreamEOF, Position


# ----
# CharStream Tests
# ----
def test_char_stream_iteration():
    source = "ab\nc"
    stream = CharStream(source)

    expected = [
        (0, "a", Position(0, 1, 1, 1)),
        (1, "b", Position(1, 2, 1, 2)),
        (2, "\n", Position(2, 3, 1, 3)),
        (3, "c", Position(3, 4, 2, 1)),
    ]

    for (idx, ch, pos), (exp_idx, exp_ch, exp_pos) in zip(stream, expected):
        assert idx == exp_idx
        assert ch == exp_ch
        assert pos == exp_pos


def test_char_stream_empty():
    source = ""
    stream = CharStream(source)

    assert list(stream) == [(0, "\0", Position(0, 0, 1, 1))]


def test_char_stream_single_line():
    source = "hello"
    stream = CharStream(source)

    expected = [
        (0, "h", Position(0, 1, 1, 1)),
        (1, "e", Position(1, 2, 1, 2)),
        (2, "l", Position(2, 3, 1, 3)),
        (3, "l", Position(3, 4, 1, 4)),
        (4, "o", Position(4, 5, 1, 5)),
    ]

    for (idx, ch, pos), (exp_idx, exp_ch, exp_pos) in zip(stream, expected):
        assert idx == exp_idx
        assert ch == exp_ch
        assert pos == exp_pos


def test_char_stream_multiple_lines():
    source = "line1\nline2\nline3"
    stream = CharStream(source)

    expected = [
        (0, "l", Position(0, 1, 1, 1)),
        (1, "i", Position(1, 2, 1, 2)),
        (2, "n", Position(2, 3, 1, 3)),
        (3, "e", Position(3, 4, 1, 4)),
        (4, "1", Position(4, 5, 1, 5)),
        (5, "\n", Position(5, 6, 1, 6)),
        (6, "l", Position(6, 7, 2, 1)),
        (7, "i", Position(7, 8, 2, 2)),
        (8, "n", Position(8, 9, 2, 3)),
        (9, "e", Position(9, 10, 2, 4)),
        (10, "2", Position(10, 11, 2, 5)),
        (11, "\n", Position(11, 12, 2, 6)),
        (12, "l", Position(12, 13, 3, 1)),
        (13, "i", Position(13, 14, 3, 2)),
        (14, "n", Position(14, 15, 3, 3)),
        (15, "e", Position(15, 16, 3, 4)),
        (16, "3", Position(16, 17, 3, 5)),
    ]

    for (idx, ch, pos), (exp_idx, exp_ch, exp_pos) in zip(stream, expected):
        assert idx == exp_idx
        assert ch == exp_ch
        assert pos == exp_pos


def test_char_stream_non_string_source():
    with pytest.raises(TypeError):
        CharStream(123)  # type: ignore


def test_char_stream_eof():
    source = "abc"
    stream = CharStream(source)

    # Advance to the end
    for _ in range(len(source)):
        stream.advance()

    # Next advance should return EOF
    _, eof_result, pos = stream.advance()
    assert eof_result is StreamEOF
    assert pos.start == pos.end
    assert pos.line == 1
    assert pos.column == 4

    # Peek at EOF
    idx, ch, pos = stream.peek()
    assert idx == len(source)
    assert ch == "\0"
    assert pos == Position(len(source), len(source), stream.line, stream.column)


def test_char_stream_substring():
    source = "Hello, World!"
    stream = CharStream(source)

    substring = stream.sub(7, 12)
    assert substring == "World"


def test_char_stream_substring_out_of_bounds():
    source = "Hello"
    stream = CharStream(source)

    with pytest.raises(IndexError):
        stream.sub(-1, 3)

    with pytest.raises(IndexError):
        stream.sub(2, 10)

    with pytest.raises(IndexError):
        stream.sub(4, 2)


# ----
# Position Tests
# ----
def test_position_span():
    pos = Position(start=5, end=10, line=2, column=3)
    span = pos.span()

    assert span.start == 5
    assert span.end == 10
    assert span.line == 2
    assert span.column == 3


def test_position_equality():
    pos1 = Position(start=0, end=1, line=1, column=1)
    pos2 = Position(start=0, end=1, line=1, column=1)
    pos3 = Position(start=1, end=2, line=1, column=2)

    assert pos1 == pos2
    assert pos1 != pos3


def test_position_immutability():
    pos = Position(start=0, end=1, line=1, column=1)

    with pytest.raises(AttributeError):
        pos.start = 5  # type: ignore


def test_position_repr():
    pos = Position(start=10, end=20, line=3, column=5)
    repr_str = repr(pos)

    assert "Position" in repr_str
    assert "start=10" in repr_str
    assert "end=20" in repr_str
    assert "line=3" in repr_str
    assert "column=5" in repr_str


def test_position_invalid_values():
    with pytest.raises(ValueError):
        Position(start=-1, end=5, line=1, column=1)

    with pytest.raises(ValueError):
        Position(start=5, end=3, line=1, column=1)

    with pytest.raises(ValueError):
        Position(start=0, end=5, line=0, column=1)

    with pytest.raises(ValueError):
        Position(start=0, end=5, line=1, column=0)
