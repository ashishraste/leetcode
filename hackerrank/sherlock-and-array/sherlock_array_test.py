from sherlock_array import balancedSums

def test_single_element_array():
    assert 'YES' == balancedSums([1])
    assert 'YES' == balancedSums([10000])

def test_unbalanced_arrays():
    assert 'NO' == balancedSums([1,2,1,5])
    assert 'NO' == balancedSums([1,2,2,1])
    assert 'NO' == balancedSums([1,2,3])

def test_balanced_arrays():
    assert 'YES' == balancedSums([1,2,3,3])
    assert 'YES' == balancedSums([0,0,2,0])
    assert 'YES' == balancedSums([2,0,0,0])
    assert 'YES' == balancedSums([1,1,4,1,1])