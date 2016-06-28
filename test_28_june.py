import operator
import re
from random import shuffle
import random
import itertools


def sum_list_1(list):
    return sum(list)


def multiply_list_2(list):
    return reduce(operator.mul,list, 1)

def min_max_3(list):
    return min(list),max(list)


def palindrome_4(name):
    return name == name[::-1]


def sorted_list_6(list):
    return sorted(list, key= lambda tuples: tuples[-1])


def remove_duplicates_7(list):
    temp = []
    for x in list:
        if x not in temp:
            temp.append(x)
    return temp

def empty_or_not_8(list):
    if len(list) == 0:
        return "empty"
    else:
        return "not empty"


def clone_list_9(list):
      return list[:]



def common_number_11(list1,list2):
    if (len(list(set(list1)&set(list2))))>0:
        return "True"
    else:
        return "False"


def remove_by_index_12(list1,list2):
    return  [x for (i, x) in enumerate(list1) if i not in (list2)]

def remove_non_alpha_13(string):
    pattern = re.compile('\W')
    return re.sub(pattern, '', string)


def remove_even_14(list):
    return filter(lambda list: list%2==1, list)


def shuffle_15(list):
    if list == shuffle(list):
        return "False"
    else:
        return "True"


def square_16(num1, num2):
    return [x * x for x in range(num1, num2+1) if x < 6 or x > 25]


def permutation_18(list1):
    return (itertools.permutations([list1]))


def get_diff_19(list1, list2):
    return [x for x in list1 if x not in list2]


def conver_string_21(list):
    return ''.join(list)

def index_22(list,num):
    try:
        return (list.index(num))
    except:
        return "not found"


def adjacent_duplicate_23(list):
    length_list = len(list)-1
    for i in range(0,length_list,1):
        while i < length_list and list[i] == list[i+1]:
            del list[i+1]
            length_list -= 1
    return list

def append_list_24(list1,list2):
    return list2+list1

def random_25(list):
    x= random.choice(list)
    if x in list:
        return "True"
    else:
        return "False"




def test_sum_list_1():
    assert 55 == sum_list_1([1,2,3,4,5,6,7,8,9,10])


def test_multiply_list_2():
    assert 720 == multiply_list_2([1,2,3,4,5,6])


def test_min_max_3():
    assert 3,20 == min_max_3([3,20,5,4,6,8,9,13,16,17])


def test_palindrome_4():
    assert True == palindrome_4("madam")
    assert False == palindrome_4("hello")


def test_sorted_list_6():
    assert([(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]) == sorted_list_6( [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)])
    assert ([]) ==  sorted_list_6([])


def test_remove_duplicates_7():
   assert ([1, 2, 3, 4, 5, 6, 7, 8]) == remove_duplicates_7([1, 2, 3, 4, 5, 6, 7, 8])


def test_empty_or_not_8():
    assert "empty" == empty_or_not_8([])
    assert  "not empty" == empty_or_not_8([1,2,3])


def test_clone_list_9():
    assert ([1,2,3,4,5,6]) == clone_list_9([1,2,3,4,5,6])


def test_common_number_11():
    assert "True" == common_number_11([1,2,3],[1,2])


def test_remove_by_index_12():
    assert ['Green', 'Black'] == remove_by_index_12(['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow'],[0,2,4,5])

def test_remove_non_alpha_14():
    assert "ab2344" == remove_non_alpha_13("ab$23#44")

def test_remove_even_14():
    assert [1, 3, 5, 7, 9, 11] == remove_even_14([1,2,3,4,5,6,7,8,9,10,11,12])

def test_shuffle_15():
    assert "True"  == shuffle_15(['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow'])
    assert "True" == shuffle_15([1,2,3,4,5,6])


def test_square_16():
    assert  [1, 4, 9, 16, 25, 676, 729, 784, 841, 900] == square_16(1,30)


def test_permutation_18():
    assert [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)] == permutation_18([1,2,3])

def test_get_diff_19():
    assert ([4,5])  == get_diff_19(([1,2,3,4,5]),[1,2,3])
    assert ([]) == get_diff_19([], [])
    assert (["raghu","shweta","srihari"]) == get_diff_19(["adarsh","raghu","bhanu","sanjay","shweta","srihari"],["adarsh","bhanu","sanjay"])


def test_conver_string_21():
    assert "adarsh" == conver_string_21(['a','d','a','r','s','h'])

def test_index_22():
    assert 2 == index_22([1,2,3,4,5,6,7,8,9],3)
    assert "not found" == index_22([1,2,3,4],5)

def test_adjacent_duplicate_23():
    assert [1,2,5,2,6,3,2,6,9] == adjacent_duplicate_23([1,2,2,5,2,6,6,6,3,2,6,9])


def test_append_list_24():
    assert [4,5,6,1,2,3] == append_list_24([1,2,3],[4,5,6])


def test_random_25():
    assert  "True" == random_25([1,2,3,4,5,6,7,8,9,10])