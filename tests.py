# python -m pytest tests.py -v

from main import *


import pytest

@pytest.mark.parametrize("key,value,expected", [
    ([1, 2, 3], ['a','b'], {1:'a',2:'b',3:None}),
    (['z'], ['z'], {'z':'z'}),
    ([1,2], ['a','b','c'], {1:'a',2:'b'}),
    ([1], [], {1:None})])
def test_createDict(key,value,expected):
	assert(createDict(key, value) == expected)


import hypothesis.strategies as st
from hypothesis import given

@given(st.lists(st.integers()), st.lists(st.integers()))
def test_hyp_int_createDict(x, y):
    assert len(createDict(x, y)) == len(dict.fromkeys(x, None))

@given(st.lists(st.text()), st.lists(st.none()))
def test_hyp_none_createDict(x, y):
    assert createDict(x, y) == dict.fromkeys(x, None)