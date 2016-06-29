from placeholders import*
import itertools
import random
from string import ascii_letters
from string import digits



def add(a):

    b=sum(a)
    return b
def product(a):
    c=1
    for i in a:
        c= c*i
    return c
def lar_sma(a):
    b=[]
    b.append(min(a))
    b.append(max(a))
    return b
def palindrome(a):
  c=len(a)
  i=0
  while (i<(c/2)+1):
      if a[i]==a[c-i-1]:
          return True
      break
      i+=1
  return False
def duplicates(a):
    b=set(a)
    b=''.join(b)
    return b

def check_list(a):
    if len(a)==0:
        return True
    return False
def sort_list(a):

    for i in range(0,len(a),1):
        for j in range(0,len(a)-1,1):
            if a[j+1][1]<a[j][1]:
                a[j],a[j+1]=a[j+1],a[j]

    return a
def list_words_string(a):
    c=[]
    b=a.split()
    for i in range (0,len(b),1):
        if len(b[i])>3:
            c.append(b[i])

    return c

def similarity(a,b):
    for i in range(0,len(a),1):
        for j in range(0,len(b),1):
            if a[i]==b[j]:
                return True
    return False

def copy(a):
    b=a[:]
    return b

def count(a):
    c=0
    for i in range(0,len(a),1):
        if a[i][0]==a[i][len(a[i])-1]:
            c+=1
    return c

def remove_even(a):
    for i in a:
        if i%2==0:
            a.remove(i)
    return a


def jumble_list(a):
    if a:
       b=random.shuffle(a)
       if a==b:
           return False
       else:
           return True

def list_permuta(a):
    b=itertools.permutations(a)
    return list(b)




def diff_lists(a,b):
    c=set(a).union(set(b))
    d=set(a).intersection(set(b))
    e=list(c-d)
    return e

def index_list(a,b):
    for i in range(0,len(a),1):
        if a[i]==b:
            return i

def remove_adjacent(a):
    i=1
    while i<len(a):
        if a[i]==a[i-1]:
            a.pop(i)
            i-=1
        i+=1
    return a

def joining_list(a):
    b=''.join(a)
    return b

def square1(a):
    b=list()
    for i in range (1,31,1):
        b.append(i**2)
        c=b[:5]
        d=b[-5:]
        c=c+d
    return c

def except_1st_5(a):
    b=list()
    for i in range(1,31,1):
        b.append(i**2)
        c=b[5:]
    return c
def access_index(a):
    b=list()
    for i in range(0,len(a)):
        b.append((i,a[i]))
    return b

def append_list_2nd(a,b):
    b=b+a
    return b
def random_selection(a):
    b=random.choice(a)
    c=random.choice(a)
    if a==b:
        return False
    else:
        return True

def remove_special_char(a):
    b=[]
    for ch in a:
        if ch in ascii_letters:
            b.append(ch)
        if ch in digits:
            b.append(ch)
        c="".join(b)
    return c
def items_string(a,b,c,d,e):
    indices=[b,c,d,e]
    b=[x for (i,x) in enumerate (a) if i not in indices]
    return b

def circular_list(list1,list2):
    a=map(str,list1*2)
    b=map(str,list2)
    c=''.join(a)
    d=''.join(b)
    if d in c:
        return True
    else:
        return False




def test_add():
    assert 15==add([1,2,3,4,5])
    assert 65==add([11,12,13,14,15])

def test_product():
    assert 120==product([1,2,3,4,5])
    assert 24==product([1,2,3,4])

def test_lar_sma():
    assert [1,4]==lar_sma([1,2,3,4])
    assert [11,14]==lar_sma([11,12,13,14])

def test_palindrome():
    assert True==palindrome('madam')
    assert False==palindrome('hello')

def test_duplicates():
    assert "apel" == duplicates("apple")
    assert "rzeo" == duplicates("zeroo")

def test_check_():
    assert True==check_list([])
    assert False==check_list([1,2])

def test_sort_list():
    assert [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]==sort_list([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)])

def test_list_words_string():
    assert['quick','brown','jumps','over','lazy'] ==list_words_string("The quick brown fox jumps over the lazy dog")

def test_similarity():
    assert True==similarity([2,4,5],[3,6,4])

def test_copy():
    assert [1,2,3]==copy([1,2,3])

def test_count():
    assert 2 ==count(['abc', 'xyz', 'aba', '1221'])

def test_remove_even():
    assert[1,3,5]==remove_even([1,2,3,4,5,6])

def test_diff_lists():
    assert[3,5]==diff_lists([1,2,3,4,],[1,2,4,5])

def test_index_list():
    assert 3==index_list([1,3,5,4,2],4)

def test_jumble_list():
    assert True==jumble_list([1,2,3])



def test_remove_adjacent():
    assert [1,2,5,2,6,3,2,6,9]==remove_adjacent([1,2,2,5,2,6,6,6,3,2,6,9])

def test_joining_list():
    assert 'apple'==joining_list(['a','p','p','l','e'])

def test_square1():
    assert [1, 4, 9, 16, 25, 676, 729, 784, 841, 900]==square1((0,30))

def test_except_1st_5():
    assert [36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900]==except_1st_5((0,30))

def test_access_index():
    assert [(0, 1), (1, 2), (2, 3), (3, 4)]==access_index([1,2,3,4])

def test_append_list_2nd():
    assert [5, 6, 7, 1, 2, 3, 4]==append_list_2nd([1,2,3,4],[5,6,7])

def test_list_permuta():
    assert [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]==list_permuta([1,2,3])

def test_random_selection():
    assert True==random_selection([1,2,3])

def test_remove_specils_char():
    assert "ab2344"==remove_special_char("ab$23#44")

def test_items_string():
    assert ['Green', 'Black']==items_string(['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow'],0,2,4,5)

def test_circular_list():
    assert True==circular_list([10, 10, 0, 0, 10],[10, 10, 10, 0, 0])









