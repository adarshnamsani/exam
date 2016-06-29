from placeholders import *
from random import shuffle
from itertools import permutations
from itertools import groupby
import random

def sum_of_elements(my_List):    #Question1

    """To return the sum of all items
    in a list
    """

    if my_List:
        sum = 0
        for item in my_List:
            sum += item
        return sum


def product_of_elements(my_List):    #Question2

    """To multiply all items in a list
    and return the product
    """

    if my_List:
        product = 1
        for item in my_List:
            product *= item
        return product


def largest_and_smallest(my_List):      #Question3

    """To return the largest and smallest numbers
    from a given list
    """
    if my_List:
        return max(my_List), min(my_List)


def is_Palindrome(st):      #Question4

    """To find a given string is palindrome or not
    and return True if it is a palindrome
    and return False if it is not a palindrome
    """

    if st == st[::-1]:
        return True
    else:
        return False


def count_strings(my_List):    #Question5

    """To return the count of number of strings from a given list of strings
    where the string length is 2 or more
    and the first and last character are same
    """

    if my_List:
        count = 0
        for item in my_List:
            if len(item) >= 2 and item[0] == item[-1]:
                count += 1
        return count


def sort_by_last_element(my_List):    #Question6

    """To return a list, sorted in increasing order by the last element
    in each tuple from a given list of non-empty tuples
    """

    def my_fun(t):
        return t[-1]
    if my_List:
        return sorted(my_List,key = my_fun)


def remove_duplicates(my_List):    #Question7

    """To remove duplicates from a given list
     and return the list
     """
    if my_List:
        return list(set(my_List))


def is_empty(my_List):    #Question8

    """To check a list is empty or not
    and return True if it is empty
    and return False if it is non-empty
    """

    if my_List:
        return False
    else:
        return True


def copy_list(my_List):    #Question9

    """To clone or copy a given list
    and return the new list
    """

    #return my_List[:]
    return list(my_List)


def words_longer_than_n(st,n):    #Question10

    """To return the list of words
    whose length is longer than n(given value)
    from a given string
    """
    if st:
        return [item for item in st.split(' ') if len(item) > n]


def have_common_member(li_1,li_2):    #Question11

    """Take two lists and return True if they have at least one common member,
    otherwise return False
    """

    for item in li_1:
        if item in li_2:
            return True
    return False


def specified_list(my_List):    #Question12

    """To print a specified list
    after removing the 0th, 2nd, 4th and 5th elements from the given list
    """

    try:
        indices = [0, 2, 4, 5]
        indices.reverse()
        for i in indices:
            my_List.pop(i)
        return my_List
    except IndexError:
        return 'Atleast 6 elements required'


def remove_special_characters(st):    #Question13

    """To remove non-alphanumeric characters from a given string
    """

    return ''.join(s for s  in st if s.isalnum())


def remove_even_numbers(my_List):    #Question14

    """To return the numbers of a specified list
    after removing even numbers from it
    """

    return [item for item in my_List if item % 2 != 0]


def shuffle_list(my_List):    #Question15

    """To shuffle a given list and return True if shuffled,
    otherwise return False
    """

    if my_List:
        my_List_2 = my_List[:]
        shuffle(my_List)
        for i in my_List_2:
            if i not in my_List:
                return False
        return True



def first_and_last_five():    #Question16

    """To return a list of first and last 5 elements
    where the values are square of numbers between 1 and 30 (both included)
    """

    li = [i * i for i in range(1,31)]
    return li[0:5] + li[-5:]


def except_first_five():    #Question17

    """To return a list except first 5 elements,
    where the values are square of numbers between 1 and 30 (both included)
    """

    li = [i * i for i in range(1, 31)]
    return li[5:]


def generate_permutations(my_List):    #Question18

    """To generate all permutations of a list
    """

    return list(permutations(my_List))


def difference_of_lists(li1,li2):    #Question19

    """To return a list
    which is the difference between the two given lists
    """

    return [item for item in li1 if item not in li2]


def access_index_of_list(my_List):    #Question20

    """To access the indices of a list and return them
    """

    li = []
    for i,j in enumerate(my_List):
        li += [(i,j)]
    return li


def list_of_char_to_string(my_List):    #Question21

    """To convert a list of characters into a string
    and return the string
    """

    return ''.join(my_List)


def index_of_item(my_List,item):    #Question22

    """To find the index of an item of a specified list
    """

    if item in my_List:
        return my_List.index(item)
    else:
        return -1


def remove_adjacent_duplicates(my_List):    #Question23

    """To remove all adjacent duplicate values
    from a given list and return it
    """

    # return [value for key, value in enumerate(my_List) if key == 0 or value != my_List[key - 1]]
    return [key for key, grp in groupby(my_List)]



def append_list(li1,li2):    #Question24

    """To append a list to second list
    and return it
    """

    #li2.extend(li1)
    #return li2
    return li2 + li1


def random_item(my_List):    #Question25

    """To select an item randomly from a list
    and return it
    """

    if random.choice(my_List) in my_List:
        return True
    else:
        return False


def circular_identical(li1,li2):    #Question26

    """To check whether two lists are circularly identical
    and return True if they are, otherwise return False
    """

    for i in range(len(li1)):
        if li1 == li2[i:] + li2[:i] :
            return True
    return False



def test_sum_of_elements():
    assert 25 == sum_of_elements([4,6,7,3,5])
    assert 19.200000000000003 == sum_of_elements([5.3,2,7,4.9])
    assert None == sum_of_elements([])
    assert None == sum_of_elements(None)


def test_product_of_elements():
    assert 280 == product_of_elements([5,2,7,4])
    assert 46.000000000000000 == product_of_elements([2.3,2,10])
    assert None == product_of_elements([])
    assert None == product_of_elements(None)


def test_largest_and_smallest():
    assert 23 , 2 == largest_and_smallest([8,4,2,5,11,5,3,23])
    assert None == largest_and_smallest([])
    assert None == largest_and_smallest(None)


def test_is_Palindrome():
    assert True == is_Palindrome('madam')
    assert False == is_Palindrome('hello')
    assert True == is_Palindrome('')


def test_count_strings():
    assert 2 == count_strings(['abc', 'xyz', 'aba', '1221'])
    assert 2 == count_strings(['avb','1342','aa','11','d'])
    assert None == count_strings([])
    assert None == count_strings(None)


def test_sort_by_last_element():
    assert [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)] == sort_by_last_element([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)])
    assert [('r','a'),('d','c'),('b','c'),('d','f'),('e','g')] == sort_by_last_element([('d','c'),('e','g'),('b','c'),('d','f'),('r','a')])
    assert None == sort_by_last_element([])
    assert None == sort_by_last_element(None)


def test_remove_duplicates():
    assert [3,4,5,6,7] == remove_duplicates([4,5,5,7,3,6,3,5])
    assert ['a','dd','c','ddd'] == remove_duplicates(['a','dd','c','a','dd','ddd'])
    assert None == remove_duplicates([])
    assert None == remove_duplicates(None)


def test_is_empty():
    assert True == is_empty([])
    assert False == is_empty([1,2,4,5,3])


def test_copy_list():
    assert [5,3,6,5,3,2] == copy_list([5,3,6,5,3,2])
    assert ['a','bb','ccc','dddd'] == copy_list(['a','bb','ccc','dddd'])
    assert [] == copy_list([])


def test_words_longer_than_n():
    assert ['quick','brown','jumps','over','lazy'] == words_longer_than_n('The quick brown fox jumps over the lazy dog',3)
    assert [] == words_longer_than_n('All are not big',3)
    assert None == words_longer_than_n('',2)
    assert None == words_longer_than_n(None,4)


def test_have_common_member():
    assert True == have_common_member([5,32,1,5,3],[53,2,3,8])
    assert False == have_common_member([6,3,2,9,12],[4,1,7,11])
    assert False == have_common_member([3,6,1,4,8],[])
    assert False == have_common_member([],[5,3,7,1,0])
    assert False == have_common_member([],[])


def test_specified_list():
    assert [5,8,5,7] == specified_list([4,5,7,8,2,3,5,7])
    assert ['b','d'] == specified_list(['a','b','c','d','e','f'])
    assert 'Atleast 6 elements required' == specified_list([2, 4, 6, 7])
    assert 'Atleast 6 elements required' == specified_list([])


def test_remove_special_characters():
    assert 'ab2344' == remove_special_characters('ab$23#44')
    assert 'dswsa' == remove_special_characters('ds  w sa . ,')
    assert '' == remove_special_characters('')


def test_remove_even_numbers():
    assert [5,1,9,3] == remove_even_numbers([4,5,8,1,4,9,3])
    assert [] == remove_even_numbers([2,4,6,8])
    assert [] == remove_even_numbers([])


def test_shuffle_list():
    assert True == shuffle_list([1,2,3,4,5])
    assert True == shuffle_list(['a','b','c','d'])
    assert None == shuffle_list([])


def test_first_and_last_five():
    assert [1, 4, 9, 16, 25, 676, 729, 784, 841, 900] == first_and_last_five()


def test_except_first_five():
    assert [36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900] == except_first_five()


def test_generate_permutations():
    assert [(1,2),(2,1)] == generate_permutations([1,2])
    assert [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)] == generate_permutations([1,2,3])
    assert [('a', 'b'), ('b', 'a')] == generate_permutations(['a', 'b'])


def test_difference_of_lists():
    assert [1,2] == difference_of_lists([1,2,3],[3,4,5])
    assert [1,2,3,4] == difference_of_lists([1,2,3,4],[])
    assert [] == difference_of_lists([1,2,3,4],[1,2,3,4])
    assert [] == difference_of_lists([],[1,2,3,4])
    assert [] == difference_of_lists([],[])


def test_access_index_of_list():
    assert [(0,4),(1,6),(2,9),(3,3)] == access_index_of_list([4,6,9,3])
    assert [(0,'d'),(1,'e'),(2,'a'),(3,'b'),(4,'c')] == access_index_of_list(['d','e','a','b','c'])
    assert [] == access_index_of_list([])


def test_list_of_char_to_string():
    assert 'Hello' == list_of_char_to_string(['H','e','l','l','o'])
    assert 'Ravi123' == list_of_char_to_string(['R','a','v','i','1','2','3'])
    assert '' == list_of_char_to_string([])


def test_index_of_item():
    assert 2 == index_of_item([6, 2, 8, 2, 1], 8)
    assert 4 == index_of_item(['c', 'a', 't', 'd', 'b'], 'b')
    assert -1 == index_of_item([1,2,3,4,5,6],9)
    assert -1 == index_of_item([],4)


def test_remove_adjacent_duplicates():
    assert [1,2,3,2,4] == remove_adjacent_duplicates([1,2,2,3,2,2,4])
    assert [1,2,3,4] == remove_adjacent_duplicates([1,1,1,2,2,2,3,3,4])
    assert [1] == remove_adjacent_duplicates([1,1,1,1,1])


def test_append_list():
    assert [4,5,6,1,2,3] == append_list([1,2,3],[4,5,6])
    assert [6,3,7,8] == append_list([6,3,7,8],[])
    assert [5,9,3,5] == append_list([],[5,9,3,5])
    assert [] == append_list([],[])


def test_random_item():
    assert True == random_item([1,2,3,4,5])
    assert True == random_item(['a','b','c','d','e'])


def test_circular_identical():
    assert True == circular_identical([1,2,3,4,5],[3,4,5,1,2])
    assert True == circular_identical([1,2,3,4,5],[1,2,3,4,5])
    assert False == circular_identical([4,2,6,3,5],[1,2,3,4,5])
