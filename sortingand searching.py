from placeholders import *


def bubblesort(a):
    for i in range(len(a) - 1, 0, -1):
        for j in range(0, i, 1):
            if a[j] > a[j+1]:
                a[j+1], a[j] = a[j], a[j+1]

    return a


def selection(a):
    for i in range(0, len(a) - 1, 1):
        for j in range(i + 1, len(a), 1):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
    return a


def insertion(a):
    for i in range(1, len(a), 1):
        temp = a[i]
        j = i - 1
        while j >= 0:
            if a[j] > temp:
                a[j + 1] = a[j]
            else:
                break
            j -= 1
        a[j + 1] = temp
    return a

def quick(a):

    quicksort(a,0,len(a)-1)
    return a
def quicksort(a,lb,hb):
    if lb<hb:
        p=par(a,lb,hb)
        quicksort(a,lb,p-1)
        quicksort(a,p+1,hb)

def par(a,lb,hb):
    pivot=a[lb]
    l=lb+1
    h=hb
    flag=False

    while flag==False:
        while l<=h and pivot>=a[l]:
            l=l+1
        while pivot<=a[h] and l<=h:
            h-=1
        if h<l:
            flag=True
        else:
             a[l],a[h]=a[h],a[l]

    a[lb],a[h]=a[h],a[lb]

    return h
def merge(a):
    if len(a)>1:
        mid=int(len(a)/2)
        left=a[0:mid]
        right=a[mid:]

        merge(left)
        merge(right)
        i=0
        j=0
        k=0

        
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                a[k]=left[i]
                i+=1
            else:
                a[k]=right[j]
                j+=1
            k+=1
        while i<len(left):
            a[k]=left[i]
            k+=1
            i+=1
        while j<len(right):
            a[k]=right[j]
            k+=1
            j+=1
    return a


def linear(a, s):
    for i in range(0, len(a) - 1, 1):
        if a[i] == s:
            return True
    return False


def binary(a, s):
    l = 0
    h = len(a) - 1
    while h > l:
        mid = (l + h) / 2
        b = a[mid]
        if b > s:
            h = mid - 1
        elif b < s:
            l = mid + 1
        else:
            return True
    return False


def test_bubble():
    assert [5, 20, 34, 55, 98] == bubblesort([55, 98, 5, 20, 34])
    assert [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] == bubblesort([5, 6, 8, 4, 1, 10, 2, 7, 3, 9])
    assert [8, 25, 42, 51, 64, 72, 98, 99] == bubblesort([98, 42, 51, 8, 25, 99, 64, 72])


def test_selection():
    assert [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] == selection([5, 6, 8, 4, 1, 10, 2, 7, 3, 9])
    assert [8, 25, 42, 51, 64, 72, 98, 99] == selection([98, 42, 51, 8, 25, 99, 64, 72])
    assert [6, 17, 25, 33, 45, 59, 61, 79, 82, 95] == selection([61, 82, 45, 33, 95, 17, 25, 6, 59, 79])


def test_insertion():
    assert [8, 25, 42, 51, 64, 72, 98, 99] == insertion([98, 42, 51, 8, 25, 99, 64, 72])
    assert [5, 20, 34, 55, 98] == insertion([55, 98, 5, 20, 34])
    assert [1, 2, 3, 4, 5] == insertion([5, 4, 1, 2, 3])


def test_quick():
    assert [1, 2, 3, 4, 5, 6] == quick([6, 4, 5, 1, 3, 2])
    assert [5, 12, 45, 68, 75, 99, 102] == quick([99, 45, 68, 12, 5, 102, 75])

def test_merge():
    assert [8, 25, 42, 51, 64, 72, 98, 99] == merge([98, 42, 51, 8, 25, 99, 64, 72])
    assert[5, 12, 45, 68, 75, 99, 102] == merge([99, 45, 68, 12, 5, 102, 75])
def test_linear():
    assert True == linear([4, 56, 75, 98, 45], 75)
    assert True == linear([22, 54, 15, 95, 35, 75], 35)
    assert False == linear([56, 45, 2, 9, 78, 4], 89)


def test_binary():
    assert True == binary([4, 13, 52, 76, 85, 89, 94, 96], 94)
    assert True == binary([5, 12, 16, 46, 66, 72, 79, 88, 99], 12)
    assert False == binary([1, 5, 9, 26, 35, 59, 69, 84, 91], 88)
