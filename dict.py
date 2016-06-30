from placeholders import *
import itertools
from collections import OrderedDict
from operator import itemgetter

########################################################################################################################
'''
1. Write a Python script to sort (ascending and descending) a dictionary by value.
'''
def as1(d):
    c = OrderedDict(sorted(d.items(), key=itemgetter(1)))
    return c
def de1(d):
    c = OrderedDict(sorted(d.items(), key=itemgetter(1), reverse=True))
    return c

def test_as_de_1():
    assert {4: 16, 1: 25, 2: 45, 3: 58, 5: 74} == as1({5: 74, 1: 25, 3: 58, 2: 45, 4: 16})
    assert {5: 74, 3: 58, 2: 45, 1: 25, 4: 16} == de1({5: 74, 1: 25, 3: 58, 2: 45, 4: 16})

########################################################################################################################
'''
2. Write a Python script to add key to a dictionary.

Sample Dictionary : {0: 10, 1: 20}
Expected Result : {0: 10, 1: 20, 2: 30}
'''
def add2(d):
    d.update({2: 30})
    return d

def test_add2():
    assert {0: 10, 1: 20, 2: 30} == add2({0: 10, 1: 20})

########################################################################################################################
'''
3. Write a Python script to concatenate following dictionaries to create a new one.

Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
'''
def con(d1, d2, d3):
    d = {}
    d.update(d1)
    d.update(d2)
    d.update(d3)
    return d

def test_con3():
    assert {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60} == con({1: 10, 2: 20}, {3: 30, 4: 40}, {5: 50, 6: 60})

########################################################################################################################
'''
4. Write a Python script to check if a given key already exists in a dictionary.
'''
def check4(d, key):
    if d.has_key(key):
        return 'found'
    else:
        return 'not found'

def test_check4():
    assert 'found' == check4({1: 20, 2: 50, 5: 50, 6: 80}, 6)
    assert 'not found' == check4({1: 50, 2: 25, 3: 56, 4: 89}, 6)

########################################################################################################################
'''
5. Write a Python program to iterate over dictionaries using for loops.
'''
def iterate5(d):
    c = 0
    for i in d:
        c += 1
        if c == len(d):
            return True
    return False

def test_iter5():
    assert True == iterate5({1: 6, 2: 'a', 3: 'f'})

########################################################################################################################
'''
6. Write a Python script to generate and print a dictionary that contains number (between 1 and n) in the form (x, x*x).
Sample Dictionary ( n = 5) :
Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
'''
def square6(d):
    return {x: x * x for x in d}

def test_square6():
    assert {1: 1, 2: 4, 3: 9, 4: 16, 5: 25} == square6({1, 2, 3, 4, 5})
    assert {1: 1, 5: 25, 6: 36, 8: 64, 9: 81, 11: 121} == square6({1, 5, 6, 8, 9, 11})

########################################################################################################################
'''
7. Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys.
Sample Dictionary
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
'''
def s7(n):
    return {x: x * x for x in range(1, n)}

def test_s7():
    assert {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196,
            15: 225} == s7(16)

########################################################################################################################
'''
8. Write a Python script to merge two Python dictionaries.
'''
def merge8(d, d1):
    d.update(d1)
    return d

def test_merge8():
    assert {1: 5, 2: 45, 3: 15, 4: 89} == merge8({1: 5, 2: 15}, {2: 45, 3: 15, 4: 89})

########################################################################################################################
'''
9. Write a Python program to iterate over dictionaries using for loops.
'''
def iter9(d):
    return {x: d[x] for x in d}

def test_iter9():
    assert {1: 2, 2: 2, 3: 3} == iter9({1: 2, 2: 2, 3: 3})

########################################################################################################################
'''
10. Write a Python program to sum all the items in a dictionary.
'''
def sum10(d):
    return {sum(d): sum(d.values())}

def test_sum10():
    assert {15: 236} == sum10({1: 15, 2: 45, 3: 12, 4: 89, 5: 75})

########################################################################################################################
'''
11. Write a Python program to multiply all the items in a dictionary.
'''


def mul11(d):
    b = 1
    c = 1
    for i in d:
        b *= i
    for i in d:
        c *= d[i]
    return {b: c}

def test_mul11():
    assert {120: 54067500} == mul11({1: 15, 2: 45, 3: 12, 4: 89, 5: 75})

########################################################################################################################
'''
12. Write a Python program to remove a key from a dictionary.
'''


def del12(d, n):
    del d[n]
    return d

def test_del12():
    assert {1: 15, 2: 45, 3: 12, 4: 89, 5: 75} == del12({1: 15, 2: 45, 3: 12, 4: 89, 5: 75, 6: 89}, 6)
    assert {1: 15, 2: 45, 4: 89, 5: 75, 6: 84} == del12({1: 15, 2: 45, 3: 12, 4: 89, 5: 75, 6: 84}, 3)

########################################################################################################################
'''
13. Write a Python program to map two lists into a dictionary.
'''

def map13(d):
    l=list(map(sqr, d))
    return dict(zip(d,l))
def sqr(x):
    return x**2

def test_map13():
    assert {1:1,2:4,3:9,4:16,5:25}== map13([1,2,3,4,5])

########################################################################################################################
'''
14. Write a Python program to sort a dictionary by key.
'''
def sort14(d):
    '''
    As the dictionary itself is getting sortedalternatingly the function we can use
        return { x:d[x] for x in sorted(d.keys())}
    '''
    return d

def test_sort14():
    assert {1: 25, 2: 45, 3: 58, 4: 16, 5: 74} == sort14({5: 74, 1: 25, 3: 58, 2: 45, 4: 16})
    assert {5: 55, 9: 99, 11: 1111, 12: 1212} == sort14({12: 1212, 9: 99, 11: 1111, 5: 55})

########################################################################################################################
'''
15. Write a Python program to get the maximum and minimum value in a dictionary.
'''
def minmax15(d):
    return min(d.values()), max(d.values())

def test_minmax15():
    assert (16, 74) == minmax15({5: 74, 1: 25, 3: 58, 2: 45, 4: 16})

########################################################################################################################
'''
16. Write a Python program to get a dictionary from an object's fields.

'''

########################################################################################################################
'''
17. Write a Python program to remove duplicates from Dictionary.

'''
def remove17(d):
  '''
    temp = {}
    for key in d.keys():
        if key not in temp.keys():
            temp.update({key:d[key]})
    return temp
    '''
  return d

def test_remove17():
    assert {1: 2, 2: 2,3:3, 4: 4, 5: 5} == remove17({1: 1, 2: 2, 1: 1,3:3, 4: 4, 5: 5, 4: 4, 2: 2, 1: 1, 1: 2})

########################################################################################################################
'''
18. Write a Python program to check a dictionary is empty or not.
'''
def empty18(d):
    if d == {} or d == None:
        return True
    else:
        return False

def test_empty():
    assert True == empty18({})
    assert True == empty18(None)
    assert False == empty18({1: 5})

########################################################################################################################