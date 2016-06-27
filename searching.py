from placeholders import *


def linear_search(a_list, key):
    """This method returns index  when the key is found in the given list

    e.g a_list=[1,2,3] key =3  prints key found at an index ..."""

    for x in a_list:
        try:
            if a_list[x] == key:
                return x
        except:
            return "key not found"

def binsearch(array, key):
    """This method returns index of key ,if found by sorting and then searching in left sublist or right sublist """
    if array:
        array.sort()
        left = 0
        right = len(array) - 1

        res = -1

        while left <= right and res == -1:
            mid = (left + right) // 2

            if array[mid] == key:
                res = mid
            elif array[mid] > key:
                    right = mid - 1
            else:
                left = mid + 1

        return res
    return array



def test_linear_search():
    assert 2 == linear_search([1, 2, 3], 3)
    assert 5 == linear_search([1,2,3,4,5,6],6)
    assert "key not found" == linear_search(['a','b','c'],'d')


def test_binsearch():
    assert 2 == binsearch([1, 2, 3], 3)
    assert 5 == binsearch([1, 2, 3, 4, 5, 6], 6)
    assert -1 == binsearch(['a', 'b', 'c'], 'd')
    assert 2 == binsearch([2,3,1],3)
    assert [] == binsearch([],5)
