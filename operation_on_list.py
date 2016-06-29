from atk import Value
from samba import com

from placeholders import *

"""1.Sum of all items in a list"""

def sum_of_all_items(list_input):
    try:
        return sum(list_input)
    except TypeError:
        return "".join([str(x) for x in list_input ])
    except:
        return "".join(list_input)

def test_sum_of_all_items():
    assert 55 == sum_of_all_items([x for x in range(1,11)])
    assert "abc" == sum_of_all_items(['a','b','c'])
    assert 0 == sum_of_all_items([])
    assert "a2b3" == sum_of_all_items(['a',2,'b',3])
    assert 1 == sum_of_all_items([1])
    assert 'a' == sum_of_all_items(['a'])

"""2.multiply list items"""
def multiply_items_in_list(input_list):
    a = 1
    if input_list:
        for x in input_list:
            a*=x
    return a

def test_multiply_items_in_list():
    assert 6 == multiply_items_in_list([1,2,3])
    assert 120 == multiply_items_in_list([x for x in range(1,6)])
    assert 0 == multiply_items_in_list([0])
    assert 1 == multiply_items_in_list([])

"""3.Get largest and Smallest number from the given list"""
def get_largest_and_smallest(list):
    if list:
        return min(list),max(list)

def test_get_largest_and_smallest():
    assert (1,4) == get_largest_and_smallest([1,2,3,4])
    assert None == get_largest_and_smallest([])
    assert ('a','z') == get_largest_and_smallest(['a','b','z'])

"""4.Check palindrome condition"""
def is_palindrome(word):
    while word:
        if word == word[::-1]:
            return True
        else:
            return False
            break
    return word

def test_is_palindrome():
    assert True == is_palindrome('aba')
    assert False == is_palindrome('hello')
    assert '' == is_palindrome('')

"""5. Write a Python program to count the number of strings where the string length is 2 or more and the first and
        last character are same from a given list of strings.
        Sample List : ['abc', 'xyz', 'aba', '1221']
        Expected Result : 2"""
def str_with_identical_ends(list):
    count =0
    for item in list:
        if len(item)>=2 and item[0] == item[-1]:
            count+=1
    return count


def test_str_with_identical_ends():
    assert 2 == str_with_identical_ends(['abc', 'xyz', 'aba', '1221'])
    assert 1 == str_with_identical_ends(['aa'])
    assert 0 == str_with_identical_ends([])

""" 6. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]"""
def sort_by_last_item_in_tuple(tuple_list):
    if tuple_list:
        return sorted( tuple_list, key=last)
def last(n):
        return n[-1]

def test_sort_by_last_item_in_tuple():
    assert [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)] == sort_by_last_item_in_tuple([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)])

"""7. Write a Python program to remove duplicates from a list. """
def remove_duplicates_in_list(input):
    return sorted(list(set(input)))

def test_remove_duplicates_in_list():
    assert [1,2,3,4,5] == remove_duplicates_in_list([3,4,5,2,1,3,4,5])
    assert ['a','b','c','d'] == remove_duplicates_in_list(['a','a','b','c','c','d'])

"""8. Write a Python program to check a list is empty or not. """
def is_empty(input):
    if not input :
        return "Empty"
    return input
def test_is_empty():
    assert "Empty"== is_empty([])
    assert [1,2]== is_empty([1,2])

"""9. Write a Python program to clone or copy a list."""
def list_copy(list):
    if list:
        x=list[::]
        list.pop()
    return x

def test_list_copy():
    assert [1,2,3,4,5]  == list_copy([1,2,3,4,5])

"""10. Write a Python program to find the list of words that are longer than n from a given string.
    ex:str="The quick brown fox jumps over the lazy dog"
    n=3
    output=[quick,brown,jumps,over,dog]"""

def longer_than_n(str,n):
    return [item for item in str.split() if len(item)>n]

def test_longer_than_n():
    assert ['quick','brown','jumps','over','lazy'] == longer_than_n("The quick brown fox jumps over the lazy dog",3)
    assert ['quick', 'brown', 'jumps'] == longer_than_n("The quick brown fox jumps over the lazy dog",4)

"""11. Write a Python function that takes two lists and returns True if they have at least one common member."""
def compare_lists_for_common_member(list1,list2):
    if set(list1).intersection(set(list2)):
        return True
    else:
        return False
def test_compare_lists_for_common_member():
    assert True == compare_lists_for_common_member([x for x in range(10)],[x for x in range(10)])
    assert True == compare_lists_for_common_member([x for x in range(10)], [x for x in range(5)])

"""12. Write a Python program to print a specified list after removing the 0th, 2nd, 4th and 5th elements.
Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Expected Output : ['Green', 'White', 'Black']"""

def del_specific_items(list):
   return [y for x,y in enumerate(list) if x not in (0,2,4,5)]


def test_del_specific_item():
    assert ['Green', 'Black'] == del_specific_items(['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow'])
    assert ['1','3'] == del_specific_items(['0','1','2','3','4','5'])

"""13.given string as input.remove all non-alphabets in a string
   ex:str="ab$23#44"
   output: "ab2344"""
import re

def remove_non_alphabets(string):
    return re.sub(r'[\W]','',string,)

def test_remove_non_alphabets():
    assert "ab2344" == remove_non_alphabets("ab$23#44")
    assert "abcd" == remove_non_alphabets("a!b@c$d&")

"""14. Write a Python program to print the numbers of a specified list after removing even numbers from it."""

def remove_even_from_list(list):
    if list:
        return [x for x in list if x%2!=0]
    return list
def test_remove_even_from_list():
    assert [1,3,5,7] == remove_even_from_list([x for x in range(9)])
    assert [] == remove_even_from_list([])

"""15. Write a Python program to shuffle and print a specified list.
from random import shuffle"""
from random import shuffle
def list_shuffle(list):
    x=list[:]           #shallow copy
    shuffle(list)
    z=list           #call list after shuffle(list) to get shuffled list
    if x != z:
        return True

def test_list_shuffle():
    assert True == list_shuffle([1,2,3,4,5])

"""16. Write a Python program to generate and print a list of first and last 5 elements
where the values are square of numbers between 1 and 30 (both included)."""
def first_and_last_five(left,right):
    return [x*x for x in range(left,right+1) if x<6 or x>25]

def test_first_and_last_five():
    assert [1, 4, 9, 16, 25, 676, 729, 784, 841, 900] == first_and_last_five(1,30)

"""17. Write a Python program to generate and print a list except the first 5 elements,
where the values are square of numbers between 1 and 30 (both included)."""

def excpt_five(left,right):
    return [x*x for x in range(left,right)][5:]

def test_excpt_five():
    assert [36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400,
            441, 484, 529, 576, 625, 676, 729, 784, 841, 900] == excpt_five(1,31)

"""18. Write a Python program to generate all permutations of a list in Python. """
from itertools import permutations

def permutate_all(list):
    try:
        return [item for item in permutations(list)]
    except TypeError:
        return "not iterable"

def test_permutate_all():
    assert [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)] == permutate_all([1,2,3])
    assert [('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')] == permutate_all(['a','b','c'])
    assert "not iterable" == permutate_all(1)
    assert [()] == permutate_all([])

"""19. Write a Python program to get the difference between the two lists."""

def list_difference(list1,list2):
    return [item for item in list1 if item not in list2]

def test_list_difference():
    assert [1,3] == list_difference([1,2,3,4],[2,4,5,6])
    assert [1,2,3,4] == list_difference([1, 2, 3, 4], [])
    assert [] == list_difference([],[1,2,3,4,5])

"""20.Index of list"""
def list_index(list):
    return [(ind,val) for ind,val in enumerate(list)]


def test_list_index():
    assert [(0,1),(1,2),(2,3),(3,4)] == list_index([x for x in range(1,5)])


"""21. Write a Python program to convert a list of characters into a string. """
def convert_to_string(list):
    return "".join(list)

def test_convert_to_string():
    assert "abcdefghij" == convert_to_string(['a','b','c','d','e','f','g','h','i','j'])
    assert "12345" == convert_to_string([str(x) for x in range(1,6)])

"""22. Write a Python program to find the index of an item of a specified list. """
def find_index_of_value(list,val):
    try:
        return list.index(val)
    except ValueError:
        return "Value not present"
def test_find_index_of_value():
    assert 0 == find_index_of_value([1,2,3,4,5],1)
    assert "Value not present" == find_index_of_value([1,2,3,4,5],6)

"""23.Remove adjacent duplicates
 ex:[1,2,2,5,2,6,6,6,3,2,6,9]
   output:[1,2,5,2,6,3,2,6,9]"""
from itertools import groupby
def remove_adjacent_duplicates(list):
    if list:
        return [unique_list for unique_list,group in groupby(list) ]
    return list

def test_remove_adjacent_duplicates():
    assert [1,2,5,2,6,3,2,6,9] == remove_adjacent_duplicates([1,2,2,5,2,6,6,6,3,2,6,9])
    assert [0] == remove_adjacent_duplicates([0])
    assert [] == remove_adjacent_duplicates([])

"""24. Write a Python program to append a list to second list.
 By concatenating with + sign , we get expanded list but required is list last item in another list"""
def append_a_list(list1,list2):
    """list2.append(list1)
    return list2   # appending list1 at the end of list2"""
    return list2+list1

def test_append_a_list():
    assert [1,2,3,4,5,6,7] == append_a_list([5,6,7],[1,2,3,4])


"""25.select random ele from list
After few test iterations random might be equal to input list since input_list is small
"""

import random

def select_random(list):
    if random.choice(list) == random.choice(list):
        return "not working "
    else:
        return "working"

def test_select_random():
    assert "working" == select_random([x for x in range(10)])


"""26. Write a python program to check whether two lists are circularly identical.
list1 = [10, 10, 0, 0, 10]
list2 = [10, 10, 10, 0, 0]
list3 = [1, 10, 10, 0, 0]
Compare list1 and list2 returns True
Compare list1 and list3 return False """

def circular_identical(list1,list2):
    return "".join(map(str,list2)) in "".join(map(str,list1*2))

def test_circular_identical():
    assert True == circular_identical([10, 10, 0, 0, 10],[10, 10, 10, 0, 0])
    assert False == circular_identical([10, 10, 0, 0, 10],[1, 10, 10, 0, 0])