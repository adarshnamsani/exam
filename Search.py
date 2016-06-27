from placeholders import *

def linear_search (a,find):
    for i in range (0,len(a)-1,1):
        if a[i]==find:
            return True

    return False

def binary_search(a,find):
   l=0
   h=len(a)-1
   while  l!=h:
       mid = (l + h) / 2
       if find<a[mid]:
           h=mid-1
       if find>a[mid]:
           h=mid+1
       else :
           h=mid
       if find ==a[h]:
           return True
       return False

def test_linear_search() :
    assert True==linear_search([2,1,5,6,3],5)
    assert True==linear_search([5,7,3,10,17,11],17)
    assert False==linear_search([2,4,1,5],3)
def test_binary_search():
    assert True==binary_search([1,2,3,4,5],3)
    assert True==binary_search([9,8,7,6],8)
    assert False==binary_search([1,3,5,7,9],6)