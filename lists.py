from placeholders import *
import itertools
import random
from random import shuffle
from random import choice
from collections import deque as dq



def sum1(a):


    return sum(a)

def multiplication2(a):
    b=1
    for i in a:
        b=b*i
    return b
def minmax3(a):
    b=[]
    b.append(min(a))
    b.append(max(a))
    return b
def palindrome4(a):
    n=len(a)
    if a[:n//2-1]==a[-1:n//2:-1]:
        return True
    elif a[:n // 2 - 1] == a[-1:n // 2 + 1:-1]:
        return True
    else:
        return False



def sortt6(a):
    if a==None:
        return None
    for i in range(len(a) - 1, 0, -1):
        for j in range(0, i, 1):
            if a[j][1] > a[j + 1][1]:
                a[j + 1], a[j] = a[j], a[j + 1]

    return a
def dup7(a):

    return list(set(a))
def empty8(a):
    if a == None:
        return True
    elif len(a)==0:
        return True
    else:
        return False
def copy9(a):
    b=a[:]

    return b
def addup23(a):
    b=len(a)-1
    for j in range(0, b, 1):
        while  j<b and a[j] == a[j + 1] :
            a.pop(j+1)
            b=b-1
    return a
def appending24(a,b):
    c=a+b
    return c
def noofelements5(a):
    c=0
    for i in a:
        b=len(i)-1
        if i[0]==i[b]:
            c=c+1
    return c
def permutate18(a):
    b=itertools.permutations(a)
    c=[]
    for i in b:
        c.append(i)
    return c
def common11(a,b):
    c=set(a).intersection(set(b))
    if c==set([]):
        return False
    else:
        return True
def even14(a):
    b=len(a)-1
    for j in range(0, b, 1):
        while j <= b and a[j]%2 == 0:
            a.pop(j)
            b = b - 1
    return a
def square16(a,b):
    return [x*x for x in range(a,b+1) if x<6 or x>25]

def string21(a):
    b=' '.join(a)
    return b

def square17(a,b):
    return [x*x for x in range(a,b+1) if x>5]

def list10(a):
    c=[]
    a=a.split()
    for i in a:
        if len(i)>3:
            c.append(i)
    return c

def delete12(a,b):
    for i in b:
        a.pop(i)
    return a

def diff19(a,b):
    c=set(a).union(b)
    d=set(a).intersection(b)

    return set(c)-set(d)
def alphanum13(a):
    a=list(a)
    for x in a:
        i=ord(x)
        if (i>64 and i<91) or (i>96 and i<123) or (i>47 and i<58):
            continue
        else:
            a.remove(x)
    return ''.join(a)

def index20(a):
    return [(b,a) for b,a in enumerate(a)]

def random25(a):
    x= random.choice(a)
    if x in a:
        return True
    else:
        return False
def index22(a,n):
    for i in range(0,len(a)):
        if a[i]==n:
            return i

    return 'not found'
def shuffle15(a):
    b=random.shuffle(a)
    if b!=a:
        return True
    else:
        return False
'''
def circular26(a,b):
    b=dq(b)
    for i in range(0,len(a)-1):
        if a==b:
            return True

        else:
            b.rotate(1)

    return False
'''
def circular26(a,b):
    b=dq(b)
    a=dq(a)
    for i in range(0,len(a)):

        if a == b:
            return True
        b.rotate(1)



    return False


def test_sum1():
    assert 15 == sum1([1, 2, 3, 4, 5 ])
    assert 219 == sum1([54, 23, 25, 24, 15, 78])

def test_multiplication2():
    assert 720 ==multiplication2([1,2,3,4,5,6])
    assert 1080==multiplication2([4,5,9,2,1,3])

def test_minmax3():
    assert [1,9]==minmax3([2,4,5,8,1,6,9,7])
    assert [15,78]==minmax3([54, 23, 25, 24, 15, 78])

def test_palindrome4():
    assert True==palindrome4("madam")
    assert False==palindrome4('hello')
    assert True==palindrome4('battab')

def test_sortt6():
    assert [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]==sortt6([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)])
    assert None==sortt6(None)

def test_dup7():
    assert [1,2,3,4,5,6]==dup7([2,5,4,5,2,1,3,1,6])

def test_empty8():
    assert True==empty8([])
    assert True==empty8(None)

def test_copy9():
    assert [1,2,3,4,5,6]==copy9([1,2,3,4,5,6])
    assert ['apple', 'bat', 'cat', 'apple','bat','elephant'] == copy9(['apple', 'bat', 'cat', 'apple', 'bat', 'elephant'])

def test_addup23():
    assert [1,2,5,2,6,3,2,6,9]==addup23([1,2,2,5,2,6,6,6,3,2,6,9])
    assert [5,4,9,5,4,1,6,2,8]==addup23([5,5,4,4,9,9,5,5,4,4,1,1,1,1,6,6,2,2,8,8,8,8])

def test_appending24():
    assert ['apple','ball','cat','axe','bat','egg']==appending24(['apple','ball','cat'],['axe','bat','egg'])
    assert [1,2,3,4,5,6,7,8,9,10]==appending24([1,2,3,4,5],[6,7,8,9,10])

def test_noofelements5():
    assert 2 ==noofelements5(['abc', 'xyz', 'aba', '1221'])

def test_permutate18():
    assert [(1,2,3),(1, 3, 2),(2, 1, 3),(2, 3, 1),(3, 1, 2),(3, 2, 1)]==permutate18([1,2,3])
    assert [(1,2),(2,1)]==permutate18([1,2])

def test_common11():
    assert True==common11([1,2,3],[1,4])
    assert False==common11([4,9,7],[1,2,3])

def test_even14():
    assert [1,3,7] ==even14([1,2,3,4,6,7,8,10,])
    assert [5,9,77,99,105]==even14([2,5,9,14,56,8,77,99,105])

def test_string21():
    assert 'list of elements are converted into string ' == string21(['list' ,'of' ,'elements' ,'are' ,'converted' ,'into' ,'string '])
    assert 'this is hyderabad'==string21(['this','is','hyderabad'])

def test_square16():
    assert[1,4,9,16,25,676,729,784,841,900]==square16(1,30)

def test_square17():
    assert [36,49,64,81,100,121,144,169,196,225,256,289,324,361,400,441,484,529,576,625,676,729,784,841,900]==square17(1,30)

def test_listofwords10():
    assert ['quick','brown','jumps','over','lazy']==list10("The quick brown fox jumps over the lazy dog")

def test_delete12():
    assert ['Green','Black']==delete12(['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow'],[5,4,2,0])

def test_diff19():
    assert set([1,2,3,6,7,8])==diff19([1,2,3,4,5],[4,5,6,7,8])
    assert set([5,6,8,45,68,95])==diff19([45,8,95,5,84,99],[84,99,6,68])

def test_alphanum13():
    assert "ab2344"==alphanum13("ab$23#44")

def test_index20():
    assert[(0,4),(1,5),(2,6),(3,1),(4,9),(5,8),(6,7)]==index20([4,5,6,1,9,8,7])

def test_random25():
    assert True==random25([1,2,3,4,5,6,7,8,9,10])

def test_index22():
    assert 4 ==index22([1,2,3,4,5,6,7,8],5)
    assert 7 ==index22([1,2,3,4,5,6,7,8],8)
    assert 'not found'==index22([1,2,5,6,8],9)

def test_shuffle15():
    assert True==shuffle15([1,2,3,5,6,8,8])

def test_circular26():
    assert True==circular26([10, 10, 0, 0, 10],[10, 10, 10, 0, 0])
    assert False==circular26([10, 10, 10, 0, 0],[1, 10, 10, 0, 0])
