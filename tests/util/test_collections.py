import pytest

from bonobo.util import ensure_tuple, sortedlist
from bonobo.util.collections import cast, tuplize


def test_sortedlist():
    l = sortedlist()
    l.insort(2)
    l.insort(1)
    l.insort(3)
    l.insort(2)
    assert l == [1, 2, 2, 3]


def test_ensure_tuple():
    assert ensure_tuple('a') == ('a',)
    assert ensure_tuple(('a',)) == ('a',)
    assert ensure_tuple(()) is ()


@pytest.mark.parametrize('tuplize', [tuplize, cast(tuple)])
def test_tuplize(tuplize):
    tuplized_lambda = tuplize(lambda: [1, 2, 3])
    assert tuplized_lambda() == (1, 2, 3)

    @tuplize
    def some_generator():
        yield 'c'
        yield 'b'
        yield 'a'

    assert some_generator() == ('c', 'b', 'a')
