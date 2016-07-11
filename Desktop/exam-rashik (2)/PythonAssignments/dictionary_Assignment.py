'''1. Write a Python script to sort (ascending and descending) a dictionary by value.'''
import operator
import math

def sorting_asc(d):
    x = sorted(d.items(), key=operator.itemgetter(1))
    #y=sorted(d.items(), key=operator.itemgetter(1),reverse=True)
    return x

def test_sorting_asc():
    assert [('c', 1), ('b', 2), ('a', 3)]==sorting_asc({'a':3,'b':2,'c':1})

def sorting_desc(d):
    #x = sorted(d.items(), key=operator.itemgetter(1))
    y=sorted(d.items(), key=operator.itemgetter(1),reverse=True)
    return y

def test_sorting_desc():
    assert [('a',3),('b',2),('c',1)]==sorting_desc({'a':3,'b':2,'c':1})



'''2. Write a Python script to add key to a dictionary.

Sample Dictionary : {0: 10, 1: 20}
Expected Result : {0: 10, 1: 20, 2: 30}'''

def add_key(d):
    d.update({2:30})
    return d

def test_add_key():
    assert {0: 10, 1: 20, 2: 30}==add_key({0: 10, 1: 20})



'''3. Write a Python script to concatenate following dictionaries to create a new one.

Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}'''


def concat(d1,d2,d3):
    d=dict()
    d.update(d1)
    d.update(d2)
    d.update(d3)
    return d

def test_concat():
    assert {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}==concat({1:10, 2:20},{3:30, 4:40},{5:50,6:60})



'''4. Write a Python script to check if a given key already exists in a dictionary.'''

def check1(d,k):
    if k in d.keys():
        return True
    else:
        return False

def test_check():
    assert True==check1({1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60},3)
    assert False==check1({1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60},7)

'''5. Write a Python program to iterate over dictionaries using for loops. '''


def iterating1(d):
    for k,v in d.items():
        print (k,v)
    return True


def test_iterating():
    assert True==iterating1({1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60})



'''6. Write a Python script to generate and print a dictionary that contains number (between 1 and n) in the form (x, x*x).
Sample Dictionary ( n = 5) :
Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}'''


def generate(n):
    d=dict()
    for i in range(1,n+1):
        d.update({i:i*i})
    return d

def test_generate():
    assert {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}==generate(5)



'''7. Write a Python script to print a dictionary where the keys are numbers between 1 and 15
 (both included) and the values are square of keys.
Sample Dictionary
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}'''

def generate2():
    d=dict()
    for i in range(1,16):
        d.update({i:i*i})
    return d

def test_generate2():
    assert {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}==generate2()




'''8. Write a Python script to merge two Python dictionaries. '''

def merge(d1,d2):
    d1.update(d2)
    return d1

def test_merge():
    assert {1:1,2:2,3:3,4:4,5:5}==merge({1:1,2:2,3:3},{4:4,5:5})




'''9. Write a Python program to iterate over dictionaries using for loops.'''

def iterating2(d):
    for k,v in d.items():
        print (k,v)
    return True


def test_iterating2():
    assert True==iterating2({1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60})



'''10. Write a Python program to sum all the items in a dictionary.'''


def suming(d):
    return sum(d.values())

def test_suming():
    assert 6==suming({1:1,2:2,3:3})



'''11. Write a Python program to multiply all the items in a dictionary.'''

def multiplying(d):
    ans=1
    for i in d.values():
        ans*=i
    return ans

def test_multiplying():
    assert 6==multiplying({1:1,2:2,3:3})


'''12. Write a Python program to remove a key from a dictionary.'''

def removing(d,k):
    del d[k]
    return d

def test_removing():
    assert {1:1,3:3}==removing({1:1,2:2,3:3},2)


'''13. Write a Python program to map two lists into a dictionary.'''

def mapping(l1,l2):
    d=dict()
    for i in range(len(l1)):
        d.update({l1[i]:l2[i]})
    #print d
    return d

def test_mapping():
    assert {1:1,2:2,3:3}==mapping([1,2,3],[1,2,3])


'''14. Write a Python program to sort a dictionary by key.'''

def sorting_key(d):
    d=sorted(d.items(),key=operator.itemgetter(0))
    print d
    return d

def test_sorting_key():
    assert [(1, 1), (2, 2), (3, 3)]==sorting_key({2:2,3:3,1:1})


'''15. Write a Python program to get the maximum and minimum value in a dictionary.'''

import sys
def max_min(d):
    max=-sys.maxint-1
    min=sys.maxint
    for i in d.values():
        if i<min:
            min=i
        if i>max:
            max=i
    return (max,min)

def test_max_min():
    assert (3,1)==max_min({2:2,3:3,1:1})


'''16. Write a Python program to get a dictionary from an object's fields.'''

class dictObj:
    def __init__(self):
        self.x = 'red'
        self.y = 'Yellow'
        self.z = 'Green'

def calling():
    test=dictObj()
    print test.__dict__
    return test.__dict__

def test_dictObj():
    assert {'y': 'Yellow', 'x': 'red', 'z': 'Green'}==calling()



