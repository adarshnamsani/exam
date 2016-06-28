from placeholders import *

def bubble_sort(a):
    for i in range (len(a)-1,0,-1):
       for j in range(0,i,1):
            if a[j]>a[j+1]:
                a[j+1],a[j]=a[j],a[j+1]

    return a


def selection_sort(a):
    for i in range(0,len(a),1):
        for j in range(i+1,len(a),1):
            if a[i]>a[j]:
                a[j],a[i]=a[i],a[j]

    return a

def insertion_sort(a):
    for i in range(1,len(a),1):
        temp=a[i]
        j=i-1
        while(j>=0):
            if a[j]>temp:
                a[j+1]=a[j]
            else:
                break
            j-=1
            a[j+1]=temp
    return a



def merge_sort(a):
    if len(a) > 1:
        mid = len(a) / 2
        left = a[:mid]
        right = a[mid:]

        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                a[k] = left[i]
                i+=1
            else:
                a[k] = right[j]
                j+=1
            k += 1

        while i < len(left):
            a[k] = left[i]
            k+=1
            i += 1
        while j < len(right):
            a[k] = right[j]
            k+=1
            j+=1
    return a
def quick_sort(a):
    quicksort(a,0,len(a)-1)
    return a
def quicksort(a,l,h):
    if l<h:
        p=partition(a,l,h)
        quicksort(a,l,p-1)
        quicksort(a,p+1,h)
def partition(a,l,h):
    pivot=a[l]
    lb=l+1
    hb=h
    flag=False
    while flag==False:
        while lb<=hb and a[lb]<= pivot:
            lb+=1
        while a[hb]>=pivot and lb<=hb:
            hb-=1
        if hb<lb:
            flag=True
        else:
            a[lb],a[hb]=a[hb],a[lb]
    a[l],a[hb]=a[hb],a[l]
    return hb


def test_bubble_sort():
    assert[2,3,4,5,6,7]==bubble_sort([4,3,5,2,7,6])
    assert[32,43,56,67,78,87]==bubble_sort([56,67,32,87,43,78])

def test_selection_sort():
    assert[11,34,65,72,91]==selection_sort([91,65,11,72,34])
    assert[12,13,14,15,16]==selection_sort([15,13,16,14,12])

def test_insertion_sort():
    assert[2,3,4,5,6,7]==insertion_sort([4,3,5,2,7,6])
    assert[32,43,56,67,78,87]==insertion_sort([56,67,32,87,43,78])
def test_merge_sort():
    assert [11, 34, 65, 72, 91] == merge_sort([91, 65, 11, 72, 34])
    assert [12, 13, 14, 15, 16] == merge_sort([15, 13, 16, 14, 12])
def test_quick_sort():
    assert [27,36,45,54,63]==quick_sort([45,54,63,27,36])
    assert [2,3,4,5,6]==quick_sort([3,5,2,4,6])

