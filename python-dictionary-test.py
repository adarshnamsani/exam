from placeholders import *

def my_func(t):
    return t[-1]


def sorting_by_value_ascending(d):    #Question1.1

    """To sort a dictionary by value in ascending order
    """

    return sorted(d.items(), key=my_func)


def sorting_by_value_descending(d):    #Question1.2

    """To sort a dictionary by value in descending order
    """

    return sorted(d.items(), key=my_func, reverse=True)


def add_key(d,key):    #Question2

    """To add key to a dictionary
    """

    if key not in d:
        d[key] = 500
    return d


def concatenate(d1,d2,d3):    #Question3

    """To concatenate given dictionaries to create a new one
    """

    d4 = {}
    for d in (d1, d2, d3):
        d4.update(d)
    return d4


def check_if_key_exists(d, given_key):    #Question4

    """To check if a given key already exists in a dictionary
    """

    for key in d :
        if key == given_key :
            return True
    return False


def iteraion(d):    #Question5

    """To iterate over dictionaries using for loops
    """

    st = ''
    for key, value in d.items():
        st += '{key} => {value} '.format(key=key, value=value)
    return st


def generate_dict_between_1_and_n(n):    #Question6

    """To generate and print a dictionary that contains number
    (between 1 and n) in the form (x, x*x)
    """

    return {x : x * x for x in range(1, n + 1)}


def generate_dict():    #Question7

    """To print a dictionary where the keys are numbers between
    1 and 15 (both included) and the values are square of keys
    """

    return {x : x ** 2 for x in range(1, 16)}


def merge_dict(d1, d2):    #Question8

    """To merge two Python dictionaries
    """

    d1.update(d2)
    return d1


def iteration_for_loops(d):    #Question9

    """To iterate over dictionaries using for loops
    """

    st = ''
    for key, value in d.items():
        st += '{key} => {value} '.format(key=key, value=value)
    return st


def sum_of_items(d):    #Question10

    """To sum all the items in a dictionary
    """

    return sum(d.values())


def product_of_items(d):    #Question11

    """To multiply all the items in a dictionary
    """

    product = 1
    for key in d:
        product *= d[key]
    return product


def remove_key(d,key):    #Question12

    """To remove a key from a dictionary
    """

    try:
        del d[key]
        return d

    except KeyError:
        return 'There is no such key in the given dictionary'


def map_two_lists(li1, li2):    #Question13

    """To map two lists into a dictionary
    """

    return dict(zip(li1,li2))


def sort_by_key(d):    #Question14

    """To sort a dictionary by key
    """

    return sorted(d.items())


def max_and_min_value(d):    #Question15

    """To get the maximum and minimum value in a dictionary
    """

    max = max(d.items(), key = (lambda k : d[k]))
    min = min(d.items(), key = (lambda k : d[k]))
    return max, min


def get_from_objet_fields():    #Question16

    """To get a dictionary from an object's fields
    """

    class dictObj(object):
        def __init__(self):
            self.a = 100
            self.b = 200
            self.c = 300

        def do_nothing(self):
            pass

    return dictObj().__dict__


def remove_duplicates(d):    #Question17

    """To remove duplicates from the given dictionary
    """

    dict = {}
    for key, value in d.items():
        if value not in dict.values():
            dict[key] = value
    return dict


def check_if_empty(d):    #Question18

    """To check a dictionary is empty or not
    """

    if d:
        return False
    else:
        return True




def test_sorting_by_value_ascending():
    assert [('e', 1), ('b', 2), ('a', 5), ('d', 8), ('c', 9)] == sorting_by_value_ascending({'a': 5, 'b': 2, 'd': 8, 'e': 1, 'c': 9})
    assert [('b', 'alpha'), ('a', 'beta'), ('f', 'delta'), ('c', 'gamma')] == sorting_by_value_ascending({'a': 'beta', 'c': 'gamma', 'b': 'alpha' ,'f': 'delta'})



def test_sorting_by_value_descending():
    assert [('c', 9), ('d', 8), ('a', 5), ('b', 2), ('e', 1)] == sorting_by_value_descending({'a': 5, 'b': 2, 'd': 8, 'e': 1, 'c': 9})
    assert [('c', 'gamma'), ('f', 'delta'), ('a', 'beta'), ('b', 'alpha')] == sorting_by_value_descending({'a': 'beta', 'c': 'gamma', 'b': 'alpha' ,'f': 'delta'})

def test_add_key():
    assert {'a': 100, 'b': 200, 'c': 500} == add_key({'a': 100, 'b': 200}, 'c')
    assert {'a': 5, 'b': 2, 'd': 8, 'e': 1, 'c': 9} == add_key({'a': 5, 'b': 2, 'd': 8, 'e': 1, 'c': 9}, 'b')
    assert {'a': 500} == add_key({}, 'a')


def test_concatenate():
    assert {1:10, 2:20, 3:30, 4:40, 5:50, 6:60} == concatenate({1:10, 2:20}, {3:30, 4:40}, {5:50,6:60})
    assert {3:30, 4:40, 5:50, 6:60} == concatenate({}, {3:30, 4:40}, {5:50,6:60})
    assert {1:10, 2:20} == concatenate({}, {1:10, 2:20}, {})


def test_check_if_key_exists():
    assert True == check_if_key_exists({'a': 5, 'b': 2, 'd': 8, 'e': 1, 'c': 9}, 'c')
    assert False == check_if_key_exists({'a': 5, 'b': 2, 'd': 8, 'e': 1, 'c': 9}, 'g')


def test_iteration():
    assert 'a => 5 c => 9 b => 2 e => 1 d => 8 ' == iteraion({'a': 5, 'b': 2, 'd': 8, 'e': 1, 'c': 9})
    assert 'a => yellow c => red b => blue e => orange d => green ' == iteraion({'a': 'yellow', 'b': 'blue', 'd': 'green', 'e': 'orange', 'c': 'red'})



def test_generate_dict_between_1_and_n():
    assert {1: 1, 2: 4, 3: 9, 4: 16, 5: 25} == generate_dict_between_1_and_n(5)
    assert {1: 1, 2: 4, 3: 9} == generate_dict_between_1_and_n(3)
    assert {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64} == generate_dict_between_1_and_n(8)


def test_generate_dict():
    assert {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225} == generate_dict()


def test_merge_dict():
    assert {'a': 5, 'b': 2, 'd': 8, 'e': 1, 'c': 9} == merge_dict({'a': 5, 'b': 2, 'd': 8}, {'e': 1, 'c': 9})
    assert {'a': 5, 'b': 2, 'd': 8} == merge_dict({'a': 5, 'b': 2, 'd': 8}, {})
    assert {'e': 1, 'c': 9} == merge_dict({}, {'e': 1, 'c': 9})


def test_iteration_for_loops():
    assert 'a => 5 c => 9 b => 2 e => 1 d => 8 ' == iteraion({'a': 5, 'b': 2, 'd': 8, 'e': 1, 'c': 9})
    assert 'a => yellow c => red b => blue e => orange d => green ' == iteraion({'a': 'yellow', 'b': 'blue', 'd': 'green', 'e': 'orange', 'c': 'red'})


def test_sum_of_items():
    assert 25 == sum_of_items({'a': 5, 'b': 2, 'd': 8, 'e': 1, 'c': 9})
    assert 1300 == sum_of_items({'a': 100, 'b': 200, 'd': 800, 'e': 200})


def test_product_of_items():
    assert 720 == product_of_items({'a': 5, 'b': 2, 'd': 8, 'e': 1, 'c': 9})
    assert 8 == product_of_items({'a': 1, 'b': 1, 'd': 8, 'e': 1})



def test_remove_key():
    assert {'a': 5, 'b': 2, 'e': 1, 'c': 9} == remove_key({'a': 5, 'b': 2, 'd': 8, 'e': 1, 'c': 9}, 'd')
    assert 'There is no such key in the given dictionary' == remove_key({'a': 5, 'b': 2, 'd': 8, 'e': 1, 'c': 9}, 'h')
    assert 'There is no such key in the given dictionary' == remove_key({'a': 5, 'b': 2, 'd': 8, 'e': 1, 'c': 9}, 8)


def test_map_two_lists():
    assert {'a' : 23, 'b' : 45, 'c': 65} == map_two_lists(['a','b','c'], [23,45,65])
    assert {23 : 'a', 45 : 'b', 65 : 'c'} == map_two_lists([23,45,65], ['a','b','c'])
    assert {'a' : 'a', 'b' : 'b', 'c': 'c'} == map_two_lists(['a','b','c'], ['a','b','c'])


def test_sort_by_key():
    assert [('a', 5), ('b', 2), ('c', 9), ('d', 8), ('e', 1)] == sort_by_key({'d': 8, 'e': 1, 'c': 9, 'a': 5, 'b': 2})
    assert [(3, 'd'), (8, 'f'), (9, 'a'), (21, 'b')] == sort_by_key({9: 'a', 3: 'd', 21: 'b', 8: 'f'})


def test_max_and_min_value():
    assert 9, 1 == max_and_min_value({'a': 5, 'b': 2, 'd': 8, 'e': 1, 'c': 9})
    assert 'gamma', 'alpha' == max_and_min_value({'a': 'beta', 'c': 'gamma', 'b': 'alpha' ,'f': 'delta'})
    assert 'beta', 'beta' == max_and_min_value({'a': 'beta'})


def test_get_from_objet_fields():
    assert {'a': 100, 'b': 200, 'c': 300} == get_from_objet_fields()


def test_remove_duplicates():
    assert {'a': 5, 'c': 2, 'e': 8} == remove_duplicates({'a': 5, 'b': 5, 'c': 2, 'e': 8, 'd': 2})
    assert {'a': 'beta', 'c': 'gamma', 'b': 'alpha'} == remove_duplicates({'a': 'beta', 'c': 'gamma', 'b': 'alpha', 'f': 'gamma', 'j': 'beta'})


def test_check_if_empty():
    assert True == check_if_empty({})
    assert False == check_if_empty({'a': 5, 'b': 2, 'd': 8})