import operator




"""01 Write a Python script to sort (ascending and descending) a dictionary by value."""
def dict_asc_des_sort(dict):
    return sorted(dict.items(),key=lambda x:x[1]),sorted(dict.items(), key=lambda x:x[1], reverse=True)

def test_dict_asc_des_sort():
    assert [('a',1),('b',2),('c',3)],[('c',3),('b',2),('a',1)] == dict_asc_des_sort({'c':3,'b':2,'a':1})



"""02 Write a Python script to add key to a dictionary.
Sample Dictionary : {0: 10, 1: 20}
Expected Result : {0: 10, 1: 20, 2: 30}"""
def add_key_2(dict,key):
    dict.update(key)
    return dict
def test_add_key_2():
    assert {0:10, 1:20, 2:30} == add_key_2({0:10, 1:20}, {2:30})




"""03 Write a Python script to concatenate following dictionaries to create a new one.
Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
"""
def dict_concatination_3(dict_1,dict_2,dict_3):
    dict_4 = {}
    for d in (dict_1,dict_2,dict_3):
        dict_4.update(d)
    return dict_4
def test_dict_concatination_3():
    assert {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60} == dict_concatination_3({1:10, 2:20},{3:30, 4:40},{5:50,6:60})




"""04 Write a Python script to check if a given key already exists in a dictionary. """
def key_exist_4(dict,key):
    if key in dict:
        return "True"
    else:
        return "False"
def test_key_exist_4():
    assert "True" == key_exist_4({1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}, 3)
    assert "False" == key_exist_4({1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60},10)




"""05 Write a Python program to iterate over dictionaries using for loops."""
def iterate_dect_5(dict):
    return {(dict_key,dict_value) for dict_key,dict_value in dict.items()}
def test_iterate_dect_5():
    assert {('x', 10),('y', 20),('z', 30)} == iterate_dect_5({'x': 10, 'y': 20, 'z': 30} )




"""06 Write a Python script to generate and print a dictionary that contains number (between 1 and n) in the form (x, x*x).
Sample Dictionary ( n = 5) :
Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}"""
def square_6(num):
    return {x: x*x for x in range(1,num+1)}
def test_square_6():
    assert {1: 1, 2: 4, 3: 9, 4: 16, 5: 25} == square_6(5)




"""07 Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys.
Sample Dictionary
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}"""
def square_7(num1,num2):
    return {x: x * x for x in range(num1, num2 + 1)}
def test_square_7():
    assert {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225} == square_7(1,15)




"""08 Write a Python script to merge two Python dictionaries."""
def merge_8(dict_1,dict_2):
    dict_1.update(dict_2)
    return dict_1
def test_merge_8():
    assert {1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 8} == merge_8({1:2,3:4,5:6},{2:3,4:5,6:8})




"""09 Write a Python program to iterate over dictionaries using for loops. """
def iterate_dect_9(dict):
    return {(dict_key,dict_value) for dict_key,dict_value in dict.items()}
def test_iterate_dect_9():
    assert {('x', 10),('y', 20),('z', 30)} == iterate_dect_5({'x': 10, 'y': 20, 'z': 30} )




"""10 Write a Python program to sum all the items in a dictionary. """
def sum_dict_10(dict):
    return sum(dict.values())
def test_sum_dict_10():
    assert 60 == sum_dict_10({'x': 10, 'y': 20, 'z': 30})




"""11 Write a Python program to multiply all the items in a dictionary."""
def mul_dict_11(dict):
    return reduce(operator.mul,dict.values(), 1)
def test_mul_dict_11():
    assert 48  == mul_dict_11({1:2,3:4,5:6})




"""12 Write a Python program to remove a key from a dictionary. """
def remove_key_12(dict,key):
    if key in dict:
        del dict[key]
        return "True"
    return "False"
def test_remove_key_12():
    assert "True" == remove_key_12({'a':1,'b':2,'c':3,'d':4}, 'a')
    assert  "False" == remove_key_12({'a':1,'b':2,'c':3,'d':4},'x')




"""13 Write a Python program to map two lists into a dictionary. """
def map_13(list_1,list_2):
    return  dict(zip(list_1, list_2))
def test_map_13():
    assert {1:6,2:5,3:4,4:3,5:2,6:1} == map_13([1,2,3,4,5,6],[6,5,4,3,2,1])




""""14 Write a Python program to sort a dictionary by key."""
def sort_key(dict):
    return {k:dict[k] for k in sorted(dict.keys())}
def test_sort_key():
    return {1:6,2:5,3:4,4:3,5:2,6:1} == sort_key({4:3,5:2,1:6,5:3,6:1,3:4})



"""15 Write a Python program to get the maximum and minimum value in a dictionary."""
def max_min_15(dict):
    return min(dict.values()),max(dict.values())
def test_max_min_15():
        assert 1, 6 == max_min_15({1:6,2:5,3:4,4:3,5:2,6:1})




"""16 Write a Python program to get a dictionary from an object's fields."""

def get_from_objet_fields():
    class dictObj(object):
        def __init__(self):
            self.a = 100
            self.b = 200
            self.c = 300

        def do_nothing(self):
            pass


    return dictObj().__dict__
def test_get_from_objet_fields():
    assert {'a': 100, 'b': 200, 'c': 300} == get_from_objet_fields()

"""17  Write a Python program to remove duplicates from Dictionary."""
def remove_duplicate_17(dict):
    temp = {}
    for key, value in dict.items():
        if value not in temp.values():
            temp[key] = value
    return temp
def test_remove_duplicate_17():
    assert ({1:6,2:5,3:4,4:3,5:2,6:1}) == remove_duplicate_17({1:6,2:5,3:4,4:3,5:2,6:1,6:1,1:6,3:4})




"""18 Write a Python program to check a dictionary is empty or not. """
def empty_not_18(dict):
    if len(dict) == 0:
        return "empty"
    else:
        return "not empty"
def test_empty_not_18():
    assert "empty" == empty_not_18({})
    assert "not empty" == empty_not_18({1:2})