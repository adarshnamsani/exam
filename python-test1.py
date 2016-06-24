from placeholders import *
import math
import sys
import collections
def get_odds_list(count):
    """
     This method returns a list of the first 'count' odd numbers in descending
     order. e.g count = 3 should return [5,3,1]
    """
    j=1
    a=[]
    b=[]
    k=0
    if count==0:
        return a
    elif count==1:
        a.append(1)
        return a
    else:
        for i in range(0,count):
            a.append(j)
            j=j+2
        for i in range(count-1,-1,-1):
            #b[k]=a[i]
            #k=k+1
            b.append(a[i])
    return b
    #return None


def get_odd_mountain(count):
    """
    odd mountain is a list of odd numbers going up from 1 and then back to 1.
     e.g. odd_mountain of size 5 is [1,3,5,3,1]
    odd_mountain of size 4 is [1,3,3,1]

    Hint: use the list functions and a builtin function we have already seen.
    """
    j=1
    a=[]
    if count%2==0:
        for i in range(0,(count//2)):
            a.append(j)
            j=j+2
        for i in range((count//2)-1,-1,-1):
            a.append(a[i])
        return a
    elif(count%2!=0):
        x=1
        b=[]
        c=[]
        for i in range(0,(count//2)+1):
            b.append(x)
            x=x+2
        for i in range(0,count//2):
            c.append(b[i])
        for i in range(len(c)-1,-1,-1):
            b.append(c[i])
        return b





def get_multiples_desc(number, count):
    """
    return the first count multiples of number in desc order in a list.
    e.g call with input (3,2) returns [6,3]
    call with input(5,3) returns [15,10, 5]

    Hint: one line of code, use a builtin function we have already seen in the lists lesson.
    """
    a=[]
    if count==0:
        return a
    else:
        for i in range(count,0,-1):
            x=number*i
            a.append(x)
        return a

def get_sorted_diff_string(first, second):
    """
    returns a string which contains letters in first but not in second.
    e.g.s apple and pig returns ael.
    """
    xy=""
    if(first== second):
        return xy
    elif(len(first)==0 and len(second)!=0):
        b = "".join(collections.OrderedDict.fromkeys(second))
        d=''.join(sorted(b))
        return d
    elif (len(first) != 0 and len(second) == 0):
        b = "".join(collections.OrderedDict.fromkeys(first))
        d=''.join(sorted(b))
        return d
    else:
        k=0
        c=[]
        flag=0
        for i in range(0,len(first)):
            for j in range(0,len(second)):
                if(first[i]!=second[j]):
                    flag=1
                else:
                    flag=0
                    break
            if(flag==1):
            #c[k]=first[i]
            #k=k+1
                c.append(first[i])
    d=''.join(sorted(c))
    return d
def get_sorted_without_duplicates(input):
    """
    returns a string in which characters are sorted and duplicates removed
    e.g apple returns aelp, engine returns egin
    """
    b="".join(collections.OrderedDict.fromkeys(input))
    c=''.join(sorted(b))
    return c
def create_palindrome(word):
    b=[]
    c=[]
    if(word==None):
        return None
    #pass
    else:
        a=word
        b=a[::-1]
        c=a+b
        return c
# Sort the words that are passed in by word length instead of word content.
# e.g ["apple", "dog", "elephant"] should result in ["elephant", "apple", "dog"]
# hint: use list.sort, don't write your own
def sort_by_length(words):
 if(words):
      n=len(words)
      a=[]
      if(n==0):
          return a
      elif(words==None):
          return None
      else:
        for i in range(0,n):
              for j in range(0,n):
                  if(len(words[i])>len(words[j])):
                      (words[i],words[j])=(words[j],words[i])
      #f=" ".join(sorted(words))
        return words
 return words

def test_odds_list():
    assert [1] == get_odds_list(1)
    assert [] == get_odds_list(0)
    assert [5,3,1] == get_odds_list(3)
    assert [9,7,5,3,1] == get_odds_list(5)

def test_get_odd_mountain():
    assert [1,1] == get_odd_mountain(2)
    assert [1,3,1] == get_odd_mountain(3)
    assert [1,3,5,7,5,3,1] == get_odd_mountain(7)
    assert [] == get_odd_mountain(0)

def test_get_multiples_desc():
    assert [6,3] == get_multiples_desc(3,2)
    assert [15, 10, 5] == get_multiples_desc(5,3)
    assert [] == get_multiples_desc(6, 0)
    assert [3,2,1] == get_multiples_desc(1, 3)


def test_sorted_diff_string():
    assert "" == get_sorted_diff_string("apple", "apple")
    assert "aelp" == get_sorted_diff_string("apple", "")
    assert "do" == get_sorted_diff_string("dog", "pig")
    assert "in" == get_sorted_diff_string("pineapple", "apple")


def test_sorted_without_duplicates():
    assert "aelp" == get_sorted_without_duplicates("apple")
    assert "eorz" == get_sorted_without_duplicates("zeroo")
    assert "" == get_sorted_without_duplicates("")
    assert "abcd" == get_sorted_without_duplicates("abcdabcd")

def test_create_palindrome():
        assert "battab" == create_palindrome("bat")
        assert "abba" == create_palindrome("ab")
        assert "" == create_palindrome("")
        assert None == create_palindrome(None)

def test_sort_by_length():
    assert ["apple", "bear", "dog"] == sort_by_length(["dog", "apple", "bear"])
    assert ["apple", "bear", "dog"] == sort_by_length(["apple", "dog",  "bear"])
    assert ["apple", "dog", "cat"] == sort_by_length(["dog", "apple", "cat"])
    assert ["elephant", "apple"] == sort_by_length(["apple", "elephant"])
    assert ["three", "four", "one", "two"] == sort_by_length(["one", "two", "three", "four"])
    assert [] == sort_by_length([])
    assert None == sort_by_length(None)
