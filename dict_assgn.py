from placeholders import *


###################################
#1
'''
1. Write a Python script to sort (ascending and descending) a dictionary by value.
'''

def sort_by_value_descend(d):
    if d:

        for i in d:
            for j in d:
                if d[i] > d[j]:
                    i,j = j,i


        return d

    return None

def test_sort_by_value1():
    assert {'3':'z','1':'y','2':'x'} == sort_by_value_descend({'1':'y','2':'x','3':'z'})


def sort_by_value_ascend(d):
    if d:
        for i in d:
            for j in d:
                if d[i] < d[j]:
                    i,j = j,i

        return d

    return None

def test_sort_by_value2():
    assert {'2':'x','1':'y','3':'z'} == sort_by_value_ascend({'1':'y','2':'x','3':'z'})



######################################
#2
'''
2. Write a Python script to add key to a dictionary.

Sample Dictionary : {0: 10, 1: 20}
Expected Result : {0: 10, 1: 20, 2: 30}
'''

def add_key(d,k):
    if d:
        d.update(k)
        return d

    return None

def test_add_key():
    assert {'0': '10', '1': '20', '2': '30'}==add_key({'0': '10', '1': '20'},{'2':'30'})


###############################################
#3
'''
3. Write a Python script to concatenate following dictionaries to create a new one.

Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
'''

def concat_dict(d1,d2,d3):

    d1.update(d2)
    d1.update(d3)

    return d1

def test_concat_dict():
    assert {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60} == concat_dict({1:10, 2:20},{3:30, 4:40},{5:50,6:60})


##########################################
#4
'''
4. Write a Python script to check if a given key already exists in a dictionary.
'''

def check_dup(d,k):
    if d:
        if k in d:
            return True

    return False


def test_check_dup():
    assert True == check_dup({'1':'a','2':'b','3':'c','4':'d'},'1')
    assert False == check_dup({'1':'a','2':'b','3':'c','4':'d'},'5')



##########################################
#5
'''
5. Write a Python program to iterate over dictionaries using for loops.
'''

def iterate(d):
    if d:
        l={}
        for k,v in d.items():
            l.update({k:v})

        return l

    return None

def test_iterate():
    assert {'1':'a','2':'b','3':'c','4':'d'} == iterate({'1':'a','2':'b','3':'c','4':'d'})



####################################
#6
'''
6. Write a Python script to generate and print a dictionary that contains number (between 1 and n) in the form (x, x*x).
Sample Dictionary ( n = 5) :
Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
'''

def square(n):
    d={}
    for i in range(1,n+1):

        d.update({i:i*i})

    return d

def test_square():
    assert {1: 1, 2: 4, 3: 9, 4: 16, 5: 25} == square(5)


########################################
#7
'''
7. Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys.
Sample Dictionary
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
'''

def square2():
    d={}
    for i in range(1,16):

        d.update({i:i*i})

    return d

def test_square2():
    assert {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225} == square2()


#############################################
#8
'''
8. Write a Python script to merge two Python dictionaries.
'''

def merge_dict(d1,d2):

    d1.update(d2)
    return d1

def test_merge():
    assert {1: 1, 2: 4, 3: 9, 4: 16} == merge_dict({1: 1, 2: 4},{3: 9, 4: 16})


####################################################
#10
'''
10. Write a Python program to sum all the items in a dictionary.
'''

def sum_dict(d):
    if d:
        sum1=0

        for i in d:
            sum1 = sum1+ d[i]

        return sum1

    return None

def test_sum():
    assert(30) == sum_dict({1: 1, 2: 4, 3: 9, 4: 16})
    assert(55) == sum_dict({1: 1, 2: 4, 3: 9, 4: 16, 5: 25})


################################################
#11
'''
11. Write a Python program to multiply all the items in a dictionary.
'''

def pro_dict(d):
    if d:
        pro =1

        for i in d:
            pro = pro * d[i]

        return pro

    return None

def test_pro():
    assert(576) == pro_dict({1: 1, 2: 4, 3: 9, 4: 16})
    assert(14400) == pro_dict({1: 1, 2: 4, 3: 9, 4: 16, 5: 25})


#####################################################
#12
'''
12. Write a Python program to remove a key from a dictionary.
'''

def remove_key(d,k):
    if d:
        if k in d:
            del d[k]

        return d

    return None

def test_remove_key():
    assert {1: 1, 2: 4, 3: 9, 4: 16} == remove_key({1: 1, 2: 4, 3: 9, 4: 16, 5: 25},5)
    assert {1: 1, 3: 9, 4: 16, 5:25} == remove_key({1: 1, 2: 4, 3: 9, 4: 16, 5: 25},2)


#####################################################
#13
'''
13. Write a Python program to map two lists into a dictionary.
'''

def map(l1,l2):

    return (dict(zip(l1,l2)))

'''
     d={}
     for i in range(0,len(l1)):
        d.update({l1[i]:l2[i]})

     return d
'''


def test_map():
    assert {1:1,2:4,3:9,4:16,5:25} == map([1,2,3,4,5],[1,4,9,16,25])


########################################################
#14
'''
14. Write a Python program to sort a dictionary by key.
'''

def sort_by_key(d):
    if d:
        return {i:d[i] for i in sorted(d.keys())}

    return None

def test_sort_by_key():
    assert {'2':'4','3':'1','5':'2','7':'0'} == sort_by_key({'7':'0','3':'1','5':'2','2':'4'})



##################################################
#15
'''
15. Write a Python program to get the maximum and minimum value in a dictionary.
'''

def max_min(d):
    if d:
        return max(d.values()),min(d.values())

    return None

def test_max_min():
    assert(16,1) == max_min({1: 1, 2: 4, 3: 9, 4: 16})




##########################################
#16
'''
16. Write a Python program to get a dictionary from an object's fields.
'''

def obj_field():
    class obj_f(object):
        def __init__(self):
            self.a=1
            self.b=2

        def do_nothing(self):
            pass

    return obj_f().__dict__


def test_odj_f():
    assert {'a':1 ,'b':2 } == obj_field()



##########################################
#17
'''
17. Write a Python program to remove duplicates from Dictionary.
'''

def remove_dup(d):
    if d:
        size=len(d)-1
        for i in range(size,1,-1):
            for j in range(1,i):
                if d[i] == d[j]:
                    del d[j]
        return d

    return None


def test_remove_dup():
    assert {1: 1, 2: 4, 3: 9, 4: 16,1:2} == remove_dup({1: 1, 2: 4, 3: 9, 4: 16, 1:1,1:2})


##########################################
#18
'''
18. Write a Python program to check a dictionary is empty or not.
'''

def empty(d):
    if d:
        return False

    else:
        return True


def test_empty():
    assert True == empty({})
    assert False == empty({1: 1, 2: 4, 3: 9, 4: 16})

###############################################