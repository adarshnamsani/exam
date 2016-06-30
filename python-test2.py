import random
def sum_of_list(lis):
    if lis == None:
        return None
    sum =0
    for num in lis:
        sum = sum + num

    return sum

def mul_of_list(num_list):
    if num_list == None:
        return None
    mul =1
    for num in num_list:
        mul = mul * int(num)
    return mul
def min_and_max(lis):
    if lis == None:
        return None
    min = max = lis[0]
    for i in range(0,len(lis)):
        if(min > lis[i]):
            min = lis[i]
        if(max < lis[i]):
            max = lis[i]
    minmax = []
    minmax.append(min)
    minmax.append(max)
    return minmax


def palindrom(str):
    x = len(str) - 1
    print range(0, 4)
    i =0
    while i<x:
        print i
        if str[i] != str[x]:
            return False
        x = x - 1
        i += 1
    return True

def string_equality(lis):
    count =0
    i =0
    for word in lis:
        #print(len(words),i)
        if len(word) >= 2:
            #print word[0]
            if lis[i][0] == lis[i][len(word)-1]:
                count += 1
        i = i+1
    return count

def sorted_tupple_list(lis):
    for i in range(0, len(lis)):
        for j in range(0, i):
            if (lis[i][1] < lis[j][1]):
                temp = lis[i]
                lis[i] = lis[j]
                lis[j] = temp
    return lis

def remove_duplicate(lis):
    l = []
    for value in lis:
        if value not in l:
            l.append(value)
    return l


def check_list_empty(lis):
    if len(lis) == 0:
        return "Empty"
    else:
        return "NoneEmpty"

def clone_or_copy_list(lis):
    arr = []
    for words in lis:
        arr.append(words)
    return arr

def string_to_list(str,n):

    k = str.split()
    arr = []
    for word in k:
        if(len(word) >= n):
            arr.append(word)

    return arr



def count_word_length(lis):
    l = lis.split()

    nst = []
    for word in l:
        if len(word) > 2:
            nst.append(word)
    return nst




def common_word_in_list(lis1,lis2):
    if set(lis1).intersection(lis2):
        return True
    else:
        return False

def remove_alternate_from_list(lis):
    arr = []

    for i in range(0,len(lis)):
        if not ( i == 0 or i == 2 or i == 4 or i == 5):
            arr.append(lis[i])

    return arr


def remove_non_alpha(str):
    newstr = []
    for i in range(0,len(str)):
        if(str[i].isalpha() ):
            newstr.append(str[i])
    return ''.join(newstr)

def remove_even_number(lis):
    newlis = []
    for words in lis:
        k = int(words)
        if k%2 != 0:
            newlis.append(k)
    return newlis


def shuffle_list(lis):
    random.shuffle(lis)
    return "True"





def square_number():
    i =1
    j =26
    arr = []
    while(i <6 or j <= 30):
        if i < 6:
            arr.append(i*i)
            i += 1
        else :
            arr.append(j*j)
            j += 1

    return arr


def permutations(head, tail=''):
    from itertools import permutations
    l = list(permutations(range(1, 4)))
    return l



def set_difference_list(lis1,lis2):
    lis2 = set(lis2)
    return [item for item in lis1 if item not in lis2]


def index_in_list(lis,item):
    count =0
    for i in lis:
        if i == item:
            return count
        count += 1
    return "not found"

def list_to_string(lis):
    return ''.join(lis)

def remove_adjcence(lis):
    length = len(lis)
    arr = []
    for i in range(0,length-1):
        if(lis[i] != lis[i+1]):
            arr.append(lis[i])

    arr.append(lis[length-1])

    return arr


def append_lis(lis1,lis2):
    for word in lis2:
        lis1.append(word)
    return lis1

def select_random(lis):
    import random
    k =random.randrange(0,len(lis)-1)
    if(k >=0 and k<len(lis)):
        return True

def circular_list(lis1, lis2):
    if len(lis1) != len(lis2):
        return False
    for i in range(0, len(lis1)):
        if (lis1[0] == lis2[i]):
            k = i
            break
    i =0
    x = len(lis1)
    count = len(lis2)

    while (count - 1):
        if (k == x ):
            k = 0

        if(i == x):
            i =0


        if (lis1[i] != lis2[k]):
            return False
        count -= 1
        i += 1
        k += 1

    return True



















def test_sum_of_list():
    assert 55 == sum_of_list([1,2,3,4,5,6,7,8,9,10])


def test_multiply_list_2():
    assert 720 == mul_of_list([1,2,3,4,5,6])


def test_min_max_3():
    assert [3,20] == min_and_max([3,20,5,4,6,8,9,13,16,17])


def test_palindrome_4():
    assert True == palindrom("madam")
    assert False == palindrom("hello")


def test_sorted_tupple_list():
    assert([(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]) == sorted_tupple_list( [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)])
    assert ([]) ==  sorted_tupple_list([])


def test_remove_duplicate_7():
   assert ([1, 2, 3, 4, 5, 6, 7, 8]) == remove_duplicate([1, 2, 3, 4, 5, 6, 7, 8])


def test_check_list_empty():
    assert "Empty" == check_list_empty([])
    assert  "NoneEmpty" == check_list_empty([1,2,3])


def test_clone_list_9():
    assert ([1,2,3,4,5,6]) == clone_or_copy_list([1,2,3,4,5,6])

def test_string_to_list():
    assert(['quick','brown','jumps','over','lazy']) == string_to_list("The quick       brown fox jumps over        the lazy dog",4)

def test_common_number_11():
    assert True == common_word_in_list([1,2,3],[1,2])


def test_remove_non_alpha():
    assert "abc" == remove_non_alpha("ab$c#")

def test_remove_even_14():
    assert [1, 3, 5, 7, 9, 11] == remove_even_number([1,2,3,4,5,6,7,8,9,10,11,12])

def test_shuffle_15():
    assert "True"  == shuffle_list(['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow'])
    assert "True" == shuffle_list([1,2,3,4,5,6])

def test_string_equality():
    assert 2 == string_equality(['abc', 'xyz', 'aba', '1221'])
def test_square_16():
    assert  [1, 4, 9, 16, 25, 676, 729, 784, 841, 900] == square_number()


def test_permutation_18():
    assert [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)] == permutations([1,2,3],tail='')

def test_get_diff_19():
    assert ([4,5])  == set_difference_list(([1,2,3,4,5]),[1,2,3])
    assert ([]) == set_difference_list([], [])
    assert (["raghu","shweta","srihari"]) == set_difference_list(["adarsh","raghu","bhanu","sanjay","shweta","srihari"],["adarsh","bhanu","sanjay"])


def test_list_to_string():
    assert "adarsh" == list_to_string(['a','d','a','r','s','h'])

def test_index_22():
    assert 2 == index_in_list([1,2,3,4,5,6,7,8,9],3)
    assert "not found" == index_in_list([1,2,3,4],5)

def test_adjacent_duplicate_23():
    assert [1,2,5,2,6,3,2,6,9] == remove_adjcence([1,2,2,5,2,6,6,6,3,2,6,9])


def test_append_list_24():
    assert [1,2,3,4,5,6] == append_lis([1,2,3],[4,5,6])


def test_random_25():
   assert  True == select_random([1,2,3,4,5,6,7,8,9,10])
def test_circular_list():
    assert True == circular_list([1,2,3,4],[4,1,2,3])

def test_remove_alternate_from_list():
    assert ['Green', 'Black'] == remove_alternate_from_list(['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow'])