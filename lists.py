from placeholders import *
import itertools
import random
from string import ascii_letters
from string import digits

'''1. Write a Python program to sum all the items in a list.'''


def add(a):
    b = 0
    for i in a:
        b = b + i
    return b


def test_add():
    assert 15 == add([1, 2, 3, 4, 5])
    assert 65 == add([11, 12, 13, 14, 15])


'''2. Write a Python program to multiplies all the items in a list.'''


def product(a):
    c = 1
    for i in a:
        c = c * i
    return c


def test_product():
    assert 120 == product([1, 2, 3, 4, 5])
    assert 24 == product([1, 2, 3, 4])


'''3. Write a Python program to get the largestand smallest number from a list. '''


def lar_sma(a):
    b = a[0]
    c = []

    for i in range(0, len(a)):
        if b < a[i]:
            b = a[i]
    c.append(b)
    d = a
    b = a[0]
    for j in range(0, len(a)):
        if b > a[i]:
            b = a[i]
    c.append(b)

    return c


def test_lar_sma():
    assert [4, 1] == lar_sma([1, 2, 3, 4])
    assert [14, 11] == lar_sma([11, 12, 13, 14])


'''4. Write a Python program to find given string is a palindrome or not
   ex:madam returns True
      Hello returns False'''


def palindrome(a):
    c = len(a)
    i = 0
    while (i < (c / 2) + 1):
        if a[i] == a[c - i - 1]:
            i += 1
        else:
            return False
    return True


def test_palindrome():
    assert True == palindrome('madam')
    assert False == palindrome('hello')


'''7. Write a Python program to remove duplicates from a list.'''


def duplicates(a):
    b = []
    for i in range(len(a)):
        if a[i] not in b:
            b.append(a[i])
    return b


def test_duplicates():
    assert [1, 2, 3, 4] == duplicates([1, 2, 3, 2, 4, 3, 2, 1])


'''8. Write a Python program to check a list is empty or not.'''


def check_list(a):
    if len(a) == 0:
        return True
    return False


def test_check_():
    assert True == check_list([])
    assert False == check_list([1, 2])


'''6. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
'''


def sort_list(a):
    for i in range(0, len(a), 1):
        for j in range(0, len(a) - 1, 1):
            if a[j + 1][1] < a[j][1]:
                a[j], a[j + 1] = a[j + 1], a[j]

    return a


def test_sort_list():
    assert [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)] == sort_list([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)])


'''10. Write a Python program to find the list of words that are longer than n from a given string.
    ex:str="The quick brown fox jumps over the lazy dog"
    n=3
    output=[quick,brown,jumps,over,dog]'''


def list_words_string(a, n):
    c = []
    b = a.split()
    for i in range(0, len(b), 1):
        if len(b[i]) > n:
            c.append(b[i])

    return c


def test_list_words_string():
    assert ['quick', 'brown', 'jumps', 'over', 'lazy'] == list_words_string(
        ("The quick brown fox jumps over the lazy dog"), 3)


'''11. Write a Python function that takes two lists and returns True if they have at least one common member.
'''


def similarity(a, b):
    for i in range(0, len(a), 1):
        for j in range(0, len(b), 1):
            if a[i] == b[j]:
                return True
    return False


def test_similarity():
    assert True == similarity([2, 4, 5], [3, 6, 4])


'''9. Write a Python program to clone or copy a list. '''


def copy(a):
    b = []
    for i in range(len(a)):
        b.append(a[i])
    return b


def test_copy():
    assert [1, 2, 3] == copy([1, 2, 3])


'''5. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2'''


def count(a):
    c = 0
    for i in range(0, len(a), 1):
        if a[i][0] == a[i][len(a[i]) - 1]:
            c += 1
    return c


def test_count():
    assert 2 == count(['abc', 'xyz', 'aba', '1221'])


'''14. Write a Python program to print the numbers of a specified list after removing even numbers from it.
'''


def remove_even(a):
    for i in a:
        if i % 2 == 0:
            a.remove(i)
    return a


def test_remove_even():
    assert [1, 3, 5] == remove_even([1, 2, 3, 4, 5, 6])


'''15. Write a Python program to shuffle and print a specified list.'''


def jumble_list(a):
    if a:
        b = random.shuffle(a)
        if a == b:
            return False
        else:
            return True


def test_jumble_list():
    assert True == jumble_list([1, 2, 3])


'''18. Write a Python program to generate all permutations of a list in Python. '''


'''def list_permuta(array, index_to_swap_from, array_length, perms):
    if index_to_swap_from == array_length:
        return perms
    for i in range(index_to_swap_from, array_length):
        cloned_array = array[:]
        cloned_array[index_to_swap_from], cloned_array[i] = array[i], array[index_to_swap_from]
        perms += list_permuta(cloned_array, index_to_swap_from + 1, array_length, perms)
    return perms'''

def list_permuta(a,b,c,perms):
   list1=[]
   if b<c:
       for i in range (b,c):
           a[b],a[i]=a[i],a[b]
           perms.append(a[:])
           if b==c:
              return perms
       for i in range(0,len(perms)):
           list_permuta(perms[i],b+1,c,list1)
   return list1



def test_list_permuta():
    print list_permuta([1, 2, 3], 0, 3, [])
    '''assert [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]=='''


'''19. Write a Python program to get the difference between the two lists.
'''


def diff_lists(a, b):
    c = set(a) - (set(b))
    d = set(b) - (set(a))
    e = list(c) + list(d)
    return e


def test_diff_lists():
    assert [3, 5] == diff_lists([1, 2, 3, 4, ], [1, 2, 4, 5])


'''22. Write a Python program to find the index of an item of a specified list. '''


def index_list(a, b):
    for i in range(0, len(a), 1):
        if a[i] == b:
            return i


def test_index_list():
    assert 3 == index_list([1, 3, 5, 4, 2], 4)


'''23.given an integer array and length as input .write a function to remove all adjacent duplicate values
   ex:[1,2,2,5,2,6,6,6,3,2,6,9]
   output:[1,2,5,2,6,3,2,6,9]'''


def remove_adjacent(a):
    i = 1
    while i < len(a):
        if a[i] == a[i - 1]:
            a.pop(i)
            i -= 1
        i += 1
    return a


def test_remove_adjacent():
    assert [1, 2, 5, 2, 6, 3, 2, 6, 9] == remove_adjacent([1, 2, 2, 5, 2, 6, 6, 6, 3, 2, 6, 9])


'''21. Write a Python program to convert a list of characters into a string.
'''


def joining_list(a):
    b = ''
    for i in range(len(a)):
        b = b + a[i]
    return b


def test_joining_list():
    assert 'apple' == joining_list(['a', 'p', 'p', 'l', 'e'])


'''16. Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included).
'''


def square1(a, b):
    c = list()
    for i in range(a, a + 5):
        c.append(i ** 2)
    for i in range(b - 4, b + 1):
        c.append(i ** 2)
    return c


def test_square1():
    assert [1, 4, 9, 16, 25, 676, 729, 784, 841, 900] == square1(1, 30)


'''
17. Write a Python program to generate and print a list except the first 5 elements, where the values are square of numbers between 1 and 30 (both included). '''


def except_1st_5(a, b):
    c = list()
    for i in range(a + 5, b + 1):
        c.append(i ** 2)

    return c


def test_except_1st_5():
    assert [36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729,
            784, 841, 900] == except_1st_5(1, 30)


'''20. Write a Python program access the index of a list.
'''


def access_index(a):
    b = list()
    for i in range(0, len(a)):
        b.append((i, a[i]))
    return b


def test_access_index():
    assert [(0, 1), (1, 2), (2, 3), (3, 4)] == access_index([1, 2, 3, 4])


'''24. Write a Python program to append a list to second list. '''


def append_list_2nd(a, b):
    for i in range(len(a)):
        b.append(a[i])
    return b


def test_append_list_2nd():
    assert [5, 6, 7, 1, 2, 3, 4] == append_list_2nd([1, 2, 3, 4], [5, 6, 7])


'''25. Write a Python program to select an item randomly from a list.'''


def random_selection(a):
    b = random.choice(a)
    c = random.choice(a)
    if b == c:
        return False
    else:
        return True


def test_random_selection():
    assert True == random_selection([1, 2, 3])


'''13.given string as input.remove all non-alphabets in a string
   ex:str="ab$23#44"
   output: "ab2344"'''


def remove_special_char(a):
    b = []
    for ch in a:
        if ((ord(ch) >= 48 and ord(ch) <= 57) or (ord(ch) >= 65 and ord(ch) <= 90) or (
                ord(ch) >= 97 and ord(ch) <= 122)):
            b.append(ch)
        c = "".join(b)
    return c


def test_remove_specils_char():
    assert "ab2344" == remove_special_char("ab$23#44")


'''12. Write a Python program to print a specified list after removing the 0th, 2nd, 4th and 5th elements.
Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Expected Output : ['Green', 'White', 'Black']'''


def items_string(a, b, c, d, e):
    indices = [b, c, d, e]
    b = [x for (i, x) in enumerate(a) if i not in indices]
    return b


def test_items_string():
    assert ['Green', 'Black'] == items_string(['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow'], 0, 2, 4, 5)


'''26. Write a python program to check whether two lists are circularly identical.
list1 = [10, 10, 0, 0, 10]
list2 = [10, 10, 10, 0, 0]
Compare list1 and list2 returns True
'''


def circular_list(list1, list2):
    c = list2 * 2
    for i in range(len(list1)):
        if list1[i] in c:
            continue
    return True


def test_circular_list():
    assert True == circular_list([10, 10, 0, 0, 10], [10, 10, 10, 0, 0])
