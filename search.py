from placeholders import *

def linear_search(a,find):
    for i in a:
        if find == i:
            return True

    return False


def binary_search(a,find):
    first= 0
    last= len(a)-1
    while first <= last:
        mid = int(first+last)/2
        if find < a[mid]:
            last= mid-1
        elif find > a[mid]:
            first= mid+1
        else:
            return True

    return False


def test_linear_search():
    assert True==linear_search([2,4,1,5,3],1)
    assert True==linear_search([9,2,6,4,7,1,0,5,8,3],5)
    assert False==linear_search([9,2,6,4,7,1,0,5,8,3],10)


def test_binary_search():
    assert True==binary_search([1,2,3,4,5],3)
    assert True==binary_search([1,3,5,7,9,11,12,15,18],5)
    assert False==binary_search([1,3,5,7,9,11,12,15,18],25)