from placeholders import *

def selection_sort(a_list):
    """finding min of array in each iteration and inserting at next to the least value"""
    if a_list:
        for i in range(len(a_list)):
            k = min(a_list[i:])
            a_list.remove(k)
            a_list.insert(i, k)
    return a_list


def bubble_sort(array):
    """Comparing the next value and if left>right then swapping"""
    if array:
        for i in range(len(array)):
            for j in range(len(array) - i - 1):
                if array[j] > array[j + 1]:
                    temp = array[j]
                    array[j] = array[j + 1]
                    array[j + 1] = temp
    return array


def quick_sort(array):
    """" pivotting first element , inserting it into its suitable position and performing two sorts on
    left partition and right partition """
    if array:
        quick_help(array,0,len(array)-1)
    return array

def quick_help(array,left, right):
    if left<right:
        piv_point = partition(array, left, right)

        quick_help(array,left,piv_point-1)
        quick_help(array, piv_point+1, right)

def partition(array,left,right):
    piv_element=array[left]
    i=left+1
    j=right
    flag = False
    while not flag:
        while i<=j and array[i]<=piv_element:
            i+=1
        while array[j]>=piv_element and j>=i:
            j-=1
        if j<i:
            flag= True
        else:
            temp = array[i]
            array[i] = array[j]
            array[j] = temp

    temp = array[left]
    array[left] = array[j]
    array[j] = temp
    return j


def insertion_sort(array):
    """ Traverse through 1 to len(arr)
       Move elements of arr[0..i-1], that are
       greater than key, to one position ahead of their current position"""
    if array:
        for i in range(1, len(array)):
            key = array[i]
            j = i - 1
            while j >= 0 and key < array[j]:
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = key
    return array


def merge_sort(array):
    if len(array)>1:
        mid=len(array)//2
        left_child=array[:mid]
        right_child=array[mid:]

        merge_sort(left_child)
        merge_sort(right_child)

        i = 0
        j = 0
        k = 0
        while i < len(left_child) and j < len(right_child):
            if left_child[i] < right_child[j]:
                array[k] = left_child[i]
                i = i + 1
            else:
                array[k] = right_child[j]
                j = j + 1
            k = k + 1

        while i < len(left_child):
            array[k] = left_child[i]
            i = i + 1
            k = k + 1

        while j < len(right_child):
            array[k] = right_child[j]
            j = j + 1
            k = k + 1
    return array

def test_selection_sort():
    assert [1, 2, 4, 5, 5, 15, 27] == selection_sort([2, 1, 5, 4, 5, 27, 15])
    assert [-5,-3, 1, 2, 4] == selection_sort([2, 1, 4, -5,-3])
    assert [] == selection_sort([])
    assert ['a','b','c','d'] == selection_sort(['b','a','c','d'])

def test_bubble_sort():
    assert [1, 2, 3, 4, 8, 9, 10] == bubble_sort([2, 1, 8, 3, 10, 9, 4])
    assert ['a', 'b', 'c', 'd'] == bubble_sort(['b', 'a', 'c', 'd'])
    assert [] == bubble_sort([])

def test_quick_sort():
    assert [1, 2, 4, 5, 5, 15, 27] == quick_sort([2, 1, 5, 4, 5, 27, 15])
    assert [-5, -3, 1, 2, 4] == quick_sort([2, 1, 4, -5, -3])
    assert [] == quick_sort([])
    assert ['a', 'b', 'c', 'd'] == quick_sort(['b', 'a', 'c', 'd'])


def test_insertion_sort():
    assert [1,2,4,5,5,15,27]==insertion_sort([2, 1, 5, 4, 5, 27, 15])
    assert [] == insertion_sort([])
    assert [-5, -3, 1, 2, 4] == insertion_sort([2, 1, 4, -5, -3])
    assert ['a', 'b', 'c', 'd'] == insertion_sort(['b', 'a', 'c', 'd'])

def test_merge_sort():
    assert [1, 2, 4, 5, 5, 15, 27] == merge_sort([2, 1, 5, 4, 5, 27, 15])
    assert [-5,-3, 1, 2, 4] == merge_sort([2, 1, 4, -5,-3])
    assert [1] == merge_sort([1])
    assert ['a','b','c','d'] == merge_sort(['b','a','c','d'])
    assert [] == merge_sort([])