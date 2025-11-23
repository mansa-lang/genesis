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
Unit tests for the foundational scanner types:
- Span
- TokenKind
- Token

These are the building blocks of the entire compiler.
They must be 100% correct, fast, and memory-efficient.
"""

import pytest
from mansa.lexer.scanner import Span, TokenKind, Token


# ----
# Span Tests
# ----
def test_span_creation_and_attributes():
    span = Span(start=0, end=5, line=1, column=1)

    assert span.start == 0
    assert span.end == 5
    assert span.line == 1
    assert span.column == 1


def test_span_equality_and_hash():
    span1 = Span(0, 5, 1, 1)
    span2 = Span(0, 5, 1, 1)
    span3 = Span(0, 6, 1, 1)

    assert span1 == span2
    assert span1 != span3
    assert hash(span1) == hash(span2)
    assert hash(span1) != hash(span3)

    # Works perfectly in sets and dicts
    span_set = {span1, span2, span3}
    assert span2 in span_set
    assert len(span_set) == 2


def test_span_immutable():
    span = Span(0, 5, 1, 1)

    try:
        span.start = 10
        assert False, "Span should be immutable"
    except AttributeError:
        pass


def test_span_repr_is_informative():
    span = Span(42, 47, 7, 12)
    repr_str = repr(span)

    assert "Span" in repr_str
    assert "start=42" in repr_str
    assert "end=47" in repr_str
    assert "line=7" in repr_str
    assert "column=12" in repr_str


# ----
# TokenKind Tests
# ----
def test_tokenkind_membership_and_values():
    assert TokenKind.EOF.name == "EOF"
    assert TokenKind.EOF.value == "eof"


def test_tokenkind_is_strenum():
    assert isinstance(TokenKind.EOF, str)
    assert issubclass(TokenKind, str)
    assert TokenKind.EOF == "eof"


def test_tokenkind_values_are_unique():
    values = set()
    for kind in TokenKind:
        assert kind.value not in values
        values.add(kind.value)


# ----
# Token Tests
# ----
def test_token_creation_and_attributes():
    token = Token(
        kind=TokenKind.IDENT,
        span=Span(start=0, end=9, line=1, column=1),
    )

    assert token.kind == TokenKind.IDENT
    assert token.span.start == 0
    assert token.span.line == 1


def test_token_is_frozen_and_hashable():
    t1 = Token(TokenKind.IDENT, Span(0, 2, 1, 1))
    t2 = Token(TokenKind.IDENT, Span(0, 2, 1, 1))

    assert t1 == t2
    assert hash(t1) == hash(t2)

    with pytest.raises(AttributeError):
        t1.kind = TokenKind.ILLEGAL  # frozen!


def test_token_repr():
    token = Token(kind=TokenKind.INT, span=Span(10, 13, 5, 8))
    r = repr(token)
    assert "INT" in r
    assert "start=10" in r
    assert "line=5" in r
    assert "column=8" in r


def test_token_slots_memory_efficiency():
    token = Token(TokenKind.EOF, Span(0, 1, 1, 1))
    with pytest.raises(AttributeError):
        token.__dict__  # should raise since using __slots__


def test_token_can_be_used_in_sets():
    t1 = Token(TokenKind.IDENT, Span(0, 2, 1, 1))
    t2 = Token(TokenKind.INT, Span(3, 5, 1, 4))
    t3 = Token(TokenKind.IDENT, Span(0, 2, 1, 1))

    token_set = {t1, t2, t3}
    assert len(token_set) == 2
    assert t1 in token_set
    assert t2 in token_set
    assert t3 in token_set


if __name__ == "__main__":
    pytest.main(["-v", __file__])
