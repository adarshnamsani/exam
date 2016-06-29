from placeholders import *
import itertools
import random
from random import randint
import collections


################################
#1
'''
1. Write a Python program to sum all the items in a list.
'''

def list_sum(l):
    sum1=0
    for i in l:
        sum1=sum1+i

    return sum1

def test_list_sum():
    assert(15) == list_sum([1,2,3,4,5])
    assert(55) == list_sum([1,2,3,4,5,6,7,8,9,10])
    assert(0) == list_sum([])


###################################
#2
'''
2. Write a Python program to multiplies all the items in a list.
'''

def list_pro(l):
    if l:
        mul1=1
        for i in l:
            mul1=mul1*i

        return mul1

    return 0


def test_list_pro():
    assert(120) == list_pro([1,2,3,4,5])
    assert(3628800) == list_pro([1,2,3,4,5,6,7,8,9,10])
    assert(0) == list_pro([])
    assert(0) == list_pro([1,2,3,4,5,6,7,8,9,0])


##########################################
#3
'''
3. Write a Python program to get the largestand smallest number from a list.
'''

def max_min(l):
    if l:
        return max(l),min(l)

    return None


def test_max_min():
    assert(5,1) == max_min([1,2,3,4,5])
    assert(10,1) == max_min([1,2,3,4,5,6,7,8,9,10])
    assert None == max_min([])


#############################################
#4
'''
4. Write a Python program to find given string is a palindrome or not
   ex:madam returns True
      Hello returns False
'''

def palindrome(s):
    if s:
        i=0
        j=len(s)-1

        while i < j:
            if s[i] == s[j]:
                j -=1
                i +=1
                continue

            else:
                return False

        return True

    return None



def test_palindrome():
    assert True == palindrome("madam")
    assert False == palindrome("Hello")
    assert None == palindrome("")


################################################
#5
'''
5. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2
'''


def first_equals_last(l):
    if l:
        count=0
        for i in range(0,len(l),1):
            if len(l[i]) > 2:
                if l[i][0] == l[i][len(l[i])-1]:
                    count +=1

        return count

    return None


def test_first_equals_last():
    assert(2) == first_equals_last(["abc","xyz","aba","1221"])
    assert(0) == first_equals_last(["abc","xyz","abab","12213"])
    assert None == first_equals_last([])


###############################################
#6
'''
6. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
'''

def last_ele_sort(l):
    if l:
        for i in range(0,len(l),1):
            for j in range(i+1,len(l),1):
                if l[i][1] > l[j][1]:
                    l[j],l[i] = l[i],l[j]
        return l

    return None



def test_last_ele_sort():
    assert[(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)] == last_ele_sort( [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)])
    assert None == last_ele_sort([])


######################################
#7
'''
7. Write a Python program to remove duplicates from a list.
'''

def remove_dup(l):
    if l:
        a=set(l)
        l=list(a)

        return l

    return None



def test_remove_dup():
    assert[1,2,3,4,5,10] == remove_dup([10,1,2,3,1,2,4,3,4,5,4,5,3,1,5])
    assert['ant','apple','axe']==remove_dup(["apple","ant","axe","apple"])
    assert None == remove_dup([])


#################################################
#8
'''
8. Write a Python program to check a list is empty or not.
'''

def list_empty(l):
    if l:
        return False
    else:
        return True


def test_list_empty():
    assert True == list_empty([])
    assert False == list_empty([1,2,3])

###########################################
#9
'''
9. Write a Python program to clone or copy a list.
'''

def list_copy(l):
    if l:
        a=l[:]
        return  a

    return None


def test_copy():
    assert [1,2,3] == list_copy([1,2,3])
    assert[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)] == list_copy( [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)])
    assert None == list_copy([])


###################################
#10
'''
10. Write a Python program to find the list of words that are longer than n from a given string.
    ex:str="The quick brown fox jumps over the lazy dog"
    n=3
    output=[quick,brown,jumps,over,dog]
'''

def longer_n(s,n):
    if s:
        l=[]
        indices=[]
        l=s.split(" ")
        for i in range(0,len(l),1):
            if len(l[i]) <= n:
               indices.append(i)
        l=[i for j, i in enumerate(l) if j not in indices]

        return l

    return None


def test_longer_n():
    assert['quick','brown','jumps','over','lazy'] == longer_n("The quick brown fox jumps over the lazy dog",3)
    assert None == longer_n([],0)


##################################
#11
'''
11. Write a Python function that takes two lists and returns True if they have at least one common member.
'''

def common_member(first,second):
    a=set(first)
    b=set(second)
    if (a-b) != a:
        return True
    else:
        return False


def test_common_member():
    assert True == common_member([1,2,3],[1,2,3,4,5])
    assert False == common_member([1,2,3],[4,5,6])


################################
#12
'''
12. Write a Python program to print a specified list after removing the 0th, 2nd, 4th and 5th elements.
Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Expected Output : ['Green', 'White', 'Black']
'''

def remove_index(l,a,b,c,d):
    if l:
        indices=[a,b,c,d]
        l=[i for j, i in enumerate(l) if j not in indices]

        return l

    return None


def test_remove_index():
    assert ['white','black']==remove_index(['red','white','yellow','black','orange','pink'],0,2,4,5)
    assert ['def','jkl','stu']==remove_index(['abc','def','ghi','jkl','mno','qpr','stu'],0,2,4,5)
    assert ['abc','ghi','stu','vwx','yz']==remove_index(['abc','def','ghi','jkl','mno','qpr','stu','vwx','yz'],1,3,4,5)
    assert None == remove_index([],0,2,4,5)

#################################
#13
'''
13. given string as input.remove all non-alphabets in a string
   ex:str="ab$23#44"
   output: "ab2344"
'''

def remove_non_alpha(s):
    if s:
        indices=[]
        l=list(s)
        for i in range(0,len(l),1):
            if (l[i] < unichr(48)  or (l[i] > unichr(57)) and (l[i] < unichr(65)) or (l[i] > unichr(90)) and (l[i] < unichr(97)) or l[i] > unichr(122)):
                indices.append(i)
        l=[i for j, i in enumerate(l) if j not in indices]
        s="".join(l)

        return s

    return None


def test_remove_non_alpha():
    assert("apple123")==remove_non_alpha("@apple#123!")
    assert("123a")==remove_non_alpha("123!@#$%%a")
    assert("")==remove_non_alpha("!@#$%%")
    assert None==remove_non_alpha("")


##################################
#14
'''
14. Write a Python program to print the numbers of a specified list after removing even numbers from it.
'''

def remove_even(l):
    if l:
        indices=[]
        for i in range(0,len(l),1):
            if l[i]%2 == 0:
                indices.append(i)
        l=[i for j, i in enumerate(l) if j not in indices]

        return l

    return None


def test_remove_even():
    assert[1,3,5] == remove_even([1,2,3,4,5])
    assert [1,7,3,5,9] == remove_even([1,2,7,8,4,3,6,5,8,9])
    assert None == remove_even([])


####################################
#15
'''
15. Write a Python program to shuffle and print a specified list.
'''

def list_shuffle(l):
    if l:
        m=random.shuffle(l)

        if l == m:
            return False
        else:
            return True


    return None


def test_list_shuffle():
    assert True == list_shuffle([1,2,3])
    assert True == list_shuffle([1,2,3])
    assert None == list_shuffle([])


########################################
#16
'''
16. Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included).
'''

def square(first,last):

    sq=[]

#    squares=[1,4,9,16,25,36,49,64,81,100,121,144,169,196,225,256,289,324,361,400,441,484,529,576,625,676,729,784,841,900]

    while first <= last:
        sq.append(first**2)
        first +=1

    l=[]
    l.extend(sq[:5])
    l.extend(sq[-5:])

    return l



def test_square():
    assert [1,4,9,16,25,676,729,784,841,900]==square(1,30)


########################################
#17
'''
17. Write a Python program to generate and print a list except the first 5 elements, where the values are square of numbers between 1 and 30 (both included).
'''

def square2(first,last):

#    squares=[1,4,9,16,25,36,49,64,81,100,121,144,169,196,225,256,289,324,361,400,441,484,529,576,625,676,729,784,841,900]

    sq=[]
    while first <= last:
        sq.append(first**2)
        first +=1

    l=[]
    l.extend(sq[5:])

    return l


def test_square2():
    assert [36,49,64,81,100,121,144,169,196,225,256,289,324,361,400,441,484,529,576,625,676,729,784,841,900]==square2(1,30)


####################################
#18
'''
18. Write a Python program to generate all permutations of a list in Python
'''

def list_permutations(l):
    if l:
        m=[]
        m=list(itertools.permutations(l))
        return m

    return None

def test_list_permutations():
    assert[(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)] == list_permutations([1,2,3])
    assert[(1,2),(2,1)] == list_permutations([1,2])
    assert None == list_permutations([])


######################################
#19
'''
19.Write a Python program to get the difference between the two lists.
'''

def diff_lists(l1,l2):
    a=set(l1)
    b=set(l2)
    s= (a-b) | (b-a)

    return list(s)

def test_diff_lists():
    assert [2,4,5,6] == diff_lists([1,2,3,4],[1,3,5,6])
    assert [5,6] == diff_lists([1,2,3],[1,2,3,5,6])
    assert [2,4] == diff_lists([1,2,3,4,5,6,6,4],[1,3,5,6])



######################################
#20
'''
20. Write a Python program access the index of a list.
'''

def access_index(l):
    if l:
        s=[]
        for i in range(0,len(l),1):
            s.append([i,l[i]])

        return s

    return None

def test_access_index():
    assert[[0,1],[1,3],[2,4],[3,5],[4,6],[5,7],[6,9]]==access_index([1,3,4,5,6,7,9])
    assert None==access_index([])


######################################
#21
'''
21. Write a Python program to convert a list of characters into a string.
'''

def list_to_str(l):
    if l:
        return ("".join(l))

    return None


def test_list_to_str():
    assert("abcde")==list_to_str(['a','b','c','d','e'])
    assert("hello123!@#")==list_to_str(['h','e','l','l','o','1','2','3','!','@','#'])
    assert None==list_to_str([])


####################################
#22
'''
22. Write a Python program to find the index of an item of a specified list.
'''

def item_index(l,item):
    if l:
        for i in range(0,len(l),1):
            if l[i] == item:
                return i

        return -1

    return None

def test_item_index():
    assert(4)== item_index([1,3,5,7,9],9)
    assert(-1)== item_index([1,3,5,7,9],0)
    assert None==item_index([],7)


####################################
# 23
'''
23-given an integer array and length as input .write a function to remove all adjacent duplicate values
   ex:[1,2,2,5,2,6,6,6,3,2,6,9]
   output:[1,2,5,2,6,3,2,6,9]
'''

def remove_adj_dup(l):
    if l:
        indices=[]
        for i in range(0,len(l)-1,1):
            if l[i] == l[i+1]:
                indices.append(i)
        l=[i for j, i in enumerate(l) if j not in indices]
        return l

    return None


def test_remove_adj_dup():
    assert [1,2,3,4,5,2,1,3,2,4]==remove_adj_dup([1,2,2,3,4,5,2,2,2,2,2,1,3,2,4])
    assert [1]==remove_adj_dup([1,1,1,1,1,1,1])
    assert None==remove_adj_dup([])


############################################
#24
'''
24. Write a Python program to append a list to second list.
'''

def append_list(l1,l2):
    l2.extend(l1)
    return l2


def test_append_list():
    assert[1,2,3,4,5,6]==append_list([4,5,6],[1,2,3])
    assert[1,3,5,2,4,6]==append_list([2,4,6],[1,3,5])
    assert[1,2,3]==append_list([],[1,2,3])
    assert[1,2,3]==append_list([1,2,3],[])
    assert []==append_list([],[])

################################################
#25
'''
25. Write a Python program to select an item randomly from a list.
'''

def random_item(l,i1,i2):
    if l:
        item=randint(i1,i2)

        if item in l:
            return True
        return False

    return None

def test_random_item():
    assert True == random_item([1,2,3,4,5,6,7,8,9,10],1,10)


##############################################
#26
'''
26. Write a python program to check whether two lists are circularly identical.
list1 = [10, 10, 0, 0, 10]
list2 = [10, 10, 10, 0, 0]
list3 = [1, 10, 10, 0, 0]
Compare list1 and list2 returns True
Compare list1 and list3 return False
'''

def circular_identity(l1,l2):
    l1=collections.deque(l1)
    l2=collections.deque(l2)

    for i in range(0,len(l1),1):
        if l1 == l2:
            return True

        l1.rotate(i)

    return False


def test_circular():
    assert True == circular_identity([10, 10, 0, 0, 10],[10, 10, 10, 0, 0])
    assert False == circular_identity([10, 10, 0, 0, 10],[1, 10, 10, 0, 0])


##############################################################
