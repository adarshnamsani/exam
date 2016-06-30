from placeholders import *
import operator
"""
1. Write a Python script to sort (ascending and descending) a dictionary by value. """

def dict_asc_sort(dict):
    return sorted(dict.items(),key=lambda x:x[1])

def test_dict_asc_sort():
    assert [('a',1),('b',2),('c',3)] == dict_asc_sort({'c':3,'b':2,'a':1})
    assert [] == dict_asc_sort({})


def dict_dsc_sort(d):
    return sorted(d.items(), key=lambda x:x[1], reverse=True)

def test_dict_dsc_sort():
    assert [(3,'c'), (2,'b'), (1,'a') ] == dict_dsc_sort({1:'a',2:'b',3:'c'})



    """2. Write a Python script to add key to a dictionary.
    Sample Dictionary : {0: 10, 1: 20}
    Expected Result : {0: 10, 1: 20, 2: 30}"""

def add_keys(dict):
    s={0:10,1:20}
    s.update(dict)
    return s

def test_add_keys():
    assert {0:10,1:20,2:30} == add_keys({2:30})


"""3. Write a Python script to concatenate following dictionaries to create a new one.

Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}"""

def concat_dicts(dict1,dict2,dict3):
    res={}
    for item in (dict1,dict2,dict3):
        res.update(item)
    return res

def test_concat_dicts():
    assert {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60} == concat_dicts({1:10, 2:20},{3:30, 4:40},{5:50,6:60})


"""4. Write a Python script to check if a given key already exists in a dictionary."""

def key_check(dict,key):
    return dict.has_key(key)

def test_key_check():
    assert True == key_check({'a':10,'b':20,'c':30},'c')
    assert False == key_check({'a': 10, 'b': 20, 'c': 30}, 'd')

"""
5. Write a Python program to iterate over dictionaries using for loops."""

def iterate_over_dicts(dict):
    return {(key,val) for key,val in dict.items() }

def test_iterate_over_dict():
    assert {('a',10),('c',30),('b',20)} == iterate_over_dicts({'a':10,'b':20,'c':30})

"""
6. Write a Python script to generate and print a dictionary that contains number (between 1 and n) in the form (x, x*x).
Sample Dictionary ( n = 5) :
Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}"""

def dic_square(n):
    if n>=1:
        return {x:x*x for x in range(1,n+1)}

def test_dic_square():
    assert {1: 1, 2: 4, 3: 9, 4: 16, 5: 25} == dic_square(5)
    assert None == dic_square(0)


"""
7. Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included)
and the values are square of keys.
Sample Dictionary
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}"""

def ranged_squares(left,right):
    if left<right:
        return {x:x*x for x in range(left,right+1)}
    else :
        return {}


def test_ranged_squares():
    assert {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81,
            10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225} == ranged_squares(1,15)
    assert {} == ranged_squares(15,1)
"""
8. Write a Python script to merge two Python dictionaries."""

def merge_dic(dic1,dic2):
    dic=dic2.copy() #shallow copy
    dic1.update(dic)
    return dic1

def test_merge_dic():
    assert {1:10,2:20,3:30} == merge_dic({1:10,2:20},{3:30})
    assert {1: 10, 2: 20} == merge_dic({1: 10, 2: 20}, {})
    assert {1: 10, 2: 20} == merge_dic({},{1: 10, 2: 20})


"""
9. Write a Python program to iterate over dictionaries using for loops. #repeated"""

"""
10. Write a Python program to sum all the items in a dictionary."""

def sum_items(dic):
    sum=0
    for val in dic.values():
        sum+=val
    return sum

def test_sum_items():
    assert 30 == sum_items({1:10,2:20})
    assert 0 == sum_items({})


"""
11. Write a Python program to multiply all the items in a dictionary."""
def multiply_dic(dic):
    product = 1
    if dic:
        for val in dic.values():
            product*=val
        return product
    return dic
def test_multiply_dic():
    assert {} == multiply_dic({})
    assert 6000 == multiply_dic({1:10,2:20,3:30})
"""
12. Write a Python program to remove a key from a dictionary."""

def key_remove(dic,key):
    if key not in dic:
        return KeyError
    else:
        del dic[key]
    return dic

def test_key_remove():
    assert {2:20,3:30,4:40} == key_remove({1:10,2:20,3:30,4:40},1)
    assert KeyError  == key_remove({1:10,2:20,3:30,4:40},5)
    assert KeyError == key_remove({1: 10, 2: 20, 3: 30, 4: 40}, 0)


"""
13. Write a Python program to map two lists into a dictionary."""

def maps_lists(lis1,lis2):
    return dict(zip(lis1,lis2))


def test_maps_lists():
    assert {1:'a',2:'b',3:'c'} == maps_lists([1,2,3],['a','b','c'])
    assert {} == maps_lists([1, 2, 3], [])
    assert {} == maps_lists([], [])


"""14. Write a Python program to sort a dictionary by key."""
def sort_by_key(dic):
    return sorted(dic.items())

"""15. Write a Python program to get the maximum and minimum value in a dictionary."""

def minmax(dic):
    min_val=min(dic.values())
    max_val=max(dic.values())

    return [(x,y) for x,y in dic.items() if y in (min_val ,max_val) ]

def test_minmax():
    assert [(1,10),(3,30)] == minmax({1:10,2:20,3:30})

"""16. Write a Python program to get a dictionary from an object's fields."""

def obj_fields_dict():
    class sampleClass(object):

        def __init__(self,x,y):
            self.x=x
            self.y=y

    return sampleClass(1,2).__dict__

def test_obj_fields_dict():
    assert {'x':1,'y':2} == obj_fields_dict()



"""17. Write a Python program to remove duplicates from Dictionary."""

def dupl_remove(dic):
    res={}
    for key,val in dic.items() :
        if (key,val) not in res.items() :
            res[key]=val
    return res

def test_dupl_remove():
    assert {1:10,2:30} == dupl_remove({1:10,1:10,2:30,2:30})




"""18. Write a Python program to check a dictionary is empty or not."""

def check_empty(dic):
    if not dic:
        return "empty"
    else:
        return "Not empty"

def test_check_empty():
    assert "empty" == check_empty({})
    assert "Not empty" == check_empty({1:10})