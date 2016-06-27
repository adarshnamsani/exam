

def get_linear_search(elements, key):
    found = False
    position = 0
    while position < len(elements) and not found:
        if elements[position] == key:
            found = True
        position +=1

    return found


def get_binary_search(elements , key):
    lb,ub = 0,len(elements)
    found = False
    elements = sorted(elements)
    while lb < ub and not found:
         mid = int((lb+ub)/2)

         if (elements[mid] == key):
             found = True
             return found
         elif (key < elements[mid]):
             ub = mid
         elif (key > elements[mid]):
             lb = mid+1
    return found


def bubblesort(list):
    for passedelem in range(len(list)-1,0,-1):
        for i in range(passedelem):
            if list[i] > list[i+1]:
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp
    return list


def merge_sort(list):
    if len(list) > 1:
        mid = int(len(list) / 2)
        lefthalf = list[:mid]
        righthalf = list[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                list[k] = lefthalf[i]
                i = i + 1
            else:
                list[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            list[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            list[k] = righthalf[j]
            j = j + 1
            k = k + 1

    return list


def quick_sort(list):
    quickSortHelper(list, 0, len(list) - 1)
    return list

def quickSortHelper(list, first, last):
    if first < last:
        splitpoint = partition(list, first, last)

        quickSortHelper(list, first, splitpoint - 1)
        quickSortHelper(list, splitpoint + 1, last)


def partition(list, first, last):
    pivotvalue = list[first]

    leftmark = first + 1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and list[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while list[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            list[leftmark],list[rightmark]=list[rightmark],list[leftmark]

    list[first],list[rightmark] = list[rightmark],list[first]

    return rightmark


def selection_sort(list):
    for iteration in range(len(list)):
        index_of_min = iteration
        for i in range(iteration+1, len(list)):
            if (list[index_of_min] > list[i]):
                index_of_min = i

        list[iteration],list[index_of_min] = list[index_of_min],list[iteration]

    return list

def insertion_sort(list):
    for iteration in range(1,len(list)):
        temp = list[iteration]
        j = iteration-1
        while (temp < list[j] and j >= 0):
            list[j+1] = list[j]
            j = j-1
        list[j+1] = temp
    return list

def test_get_linear_search():
     assert (True)  == get_linear_search(["adarsh", "bhanu","raghu","sanjay","kiran"] , "sanjay" )
     assert (True) == get_linear_search([1,2,3,4,5,6,7,8], 4)
     assert (False) == get_linear_search(["adarsh", "bhanu", "raghu", "sanjay", "kiran"], "srihari")
     assert (False) == get_linear_search([], "srihari")
     assert (False) == get_linear_search([], "")


def test_get_binary_search():
     assert (True)  == get_binary_search(["adarsh", "bhanu","raghu","sanjay","kiran"] , "sanjay" )
     assert (True) == get_binary_search([1,2,3,4,4,5,6,7,8], 4)
     assert (False) == get_binary_search(["adarsh", "bhanu", "raghu", "sanjay", "kiran"], "srihari")
     assert (False) == get_binary_search([], "srihari")
     assert (False) == get_binary_search([], "")


def test_bubble_sort():
    assert [1,2,3,4,5,6] == bubblesort([1,2,4,5,3,6])
    assert (["adarsh", "bhanu", "kiran", "raghu", "sanjay"]) == bubblesort(["adarsh", "bhanu","raghu","sanjay","kiran"])
    assert [""] == bubblesort([""])
    assert [] == bubblesort([])


def test_merge_sort():
    assert [1,2,3,4,5,6] == merge_sort([1,2,4,5,3,6])
    assert (["adarsh", "bhanu", "kiran", "raghu", "sanjay"]) == merge_sort(["adarsh", "bhanu","raghu","sanjay","kiran"])
    assert [""] == merge_sort([""])
    assert [] == merge_sort([])


def test_quick_sort():
    assert [1,6,8,10,11,12,19,36] == quick_sort([10,8,6,1,12,11,36,19])
    assert (["adarsh", "bhanu", "kiran", "raghu", "sanjay"]) == quick_sort(["adarsh", "bhanu","raghu","sanjay","kiran"])
    assert [""] == quick_sort([""])
    assert [] == quick_sort([])


def test_selection_sort():
    assert [1,2,2,3,4,5,6] == selection_sort([1,2,2,4,5,3,6])
    assert (["adarsh", "bhanu", "kiran", "raghu", "sanjay"]) == selection_sort(["adarsh", "bhanu","raghu","sanjay","kiran"])
    assert [""] == selection_sort([""])
    assert [] == selection_sort([])


def test_insertion_sort():
    assert [1,2,2,3,4,5,6] == insertion_sort([1,2,2,4,5,3,6])
    assert (["adarsh", "bhanu", "kiran", "raghu", "sanjay"]) == insertion_sort(["adarsh", "bhanu","raghu","sanjay","kiran"])
    assert [""] == insertion_sort([""])
    assert [] == insertion_sort([])