from magic_square import *

def get_3x3_square():
    return [[4, 8, 2], [4, 5, 7], [6, 1, 6]]
   
def test_magic_square():
    m = get_3x3_square()
    r = formingMagicSquare(m)
    assert r == 4