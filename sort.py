from placeholders import *

def selection_sort(a):
    for i in range(0,len(a),1):
        for j in range(i+1,len(a),1):
            if a[i] > a[j]:
                a[i],a[j] = a[j],a[i]

    return a


def bubble_sort(a):
    for i in range(len(a)- 1,0,-1):
        for j in range(0,i,1):
            if a[j] > a[i]:
                a[i],a[j] = a[j],a[i]

    return a


def insertion_sort(a):
    for i in range(1,len(a),1):
        temp=a[i]
        j=i-1
        while j >= 0:
            if a[j] > temp:
                a[j+1]=a[j]
            else:
                break
            j -=1
        a[j+1] = temp

    return a


def quick_sort(a):
    l=0
    h=len(a)-1
    quick(a,l,h)
    return a

def quick(a,l,h):
    if l < h:
        pivot= partition(a,l,h)
        quick(a,l,pivot-1)
        quick(a,pivot+1,h)

def partition(a,l,h):
    pivot_ele= a[l]
    left= l
    right= h
    while left < right:
        while a[left] <= pivot_ele and left < h:
            left +=1
        while a[right] > pivot_ele and right > l:
            right -=1
        if left < right:
            a[left],a[right] = a[right],a[left]
    a[l]=a[right]
    a[right]=pivot_ele
    return right


def merge_sort(a):
    if len(a) > 1:
        mid = int(len(a)/2)
        a_left=a[:mid]
        a_right=a[mid:]
        merge_sort(a_left)
        merge_sort(a_right)

        i=0
        j=0
        k=0

        while i < len(a_left) and j < len(a_right):
            if a_left[i] < a_right[j]:
                a[k] = a_left[i]
                i +=1
                k +=1
            else:
                a[k]=a_right[j]
                j +=1
                k +=1

        while i < len(a_left):
            a[k] = a_left[i]
            i +=1
            k +=1

        while j < len(a_right):
            a[k] = a_right[j]
            j +=1
            k +=1

    return a



def test_selection_sort():
    assert[1,2,3,4,5]==selection_sort([2,1,5,3,4])
    assert[0,1,2,3,4,5,6,7,8,9]==selection_sort([9,2,6,8,1,5,7,3,4,0])


def test_bubble_sort():
    assert[1,2,3,4,5]==bubble_sort([2,1,5,3,4])
    assert[0,1,2,3,4,5,6,7,8,9]==selection_sort([9,2,6,8,1,5,7,3,4,0])


def test_insertion_sort():
    assert[]==insertion_sort([])
    assert[0,1,2,3,4,5,6,7,8,9]==selection_sort([9,2,6,8,1,5,7,3,4,0])


def test_quick_sort():
    assert[1,2,3,4,5]==quick_sort([2,4,1,5,3])
    assert[0,1,2,3,4,5,6,7,8,9]==quick_sort([9,2,6,8,1,5,7,3,4,0])


def test_merge_sort():
    assert[1,2,3,4,5]==merge_sort([2,1,5,3,4])
    assert[0,1,2,3,4,5,6,7,8,9]==merge_sort([9,2,6,8,1,5,7,3,4,0])


