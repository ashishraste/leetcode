import pytest
from square_ten_tree import SquareTenTree

@pytest.fixture
def square_ten_tree(scope="module"):
    return SquareTenTree()

def test_max_level_length(square_ten_tree):
    # Test the formula 10^(2^(k-1)); k being the level number
    st = square_ten_tree
    assert 10 == st.get_level_length(0)
    assert 10 == st.get_level_length(1)
    assert 10**2 == st.get_level_length(2)
    assert 10**4 == st.get_level_length(3)
    assert 10**8 == st.get_level_length(4)

def test_level_number(square_ten_tree):
    st = square_ten_tree
    assert 0 == st.find_level(3)
    assert 2 == st.find_level(501)
    assert 1 == st.find_level(42)