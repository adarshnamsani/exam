from placeholders import *
di = {2: 9, 1: 7,3:12}
def dicationary_sorting(di):
    value = di.items()
    for i in range(0,len(value)):
        for j in range(0,i):
            if(value[i][1] > value[j][1]):
                temp = value[i]
                value[i] = value[j]
                value[j] = temp
    return di
def test_1():
    assert {1:7,2:9,3:12} ==dicationary_sorting(di)



def update_key_in_dic(di,key,val):
    di.update({key : val})
    return di
def test_2():
    assert {2: 9, 1: 7,3:12,5:19} == update_key_in_dic(di,5,19)

def concatinate_dic(di1,di2):
    val =  (di1.items() + di2.items())
    di = {}
    i =0
    while i< len(val):
        di.update({val[i][0]:val[i][1]})
        i = i+1
    print "in update", di
    return di

def test_3():
    assert {2: 9, 1: 7, 3: 12, 5: 19} == concatinate_dic({2:9,1:7},{3:12,5:19})

def check_key(di,key):
    if key in di:
        return True
    else:
        return False
def test_4():
    assert True == check_key(di,2)


def itterate_over_dic(di):
    i =0
    arr = di.keys()
    while i< len(di):
        print ("key and value ",arr[i],di[arr[i]])


def square_num_dic(n):
    di = {}
    i =0
    while i< n:
        di.update({(i,i*i)})
        i +=1
    print di
    return di

def test_5():
    assert {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81} == square_num_dic(10)

def merge_dic(di1,di2):
    return (di1.items()+di2.items())

def sum_of_all_items_in_dic(di):
    return sum(di.values())
def test_6():
    assert 28 == sum_of_all_items_in_dic({1:7,2:9,3:12})



def mul_of_all_items_in_dic(di):
    k =1
    i =0
    p = di.values()
    while i< len(p):
        k = k *p[i]
        i = i+1
    return k


def test_7():
    assert 0 == mul_of_all_items_in_dic({1: 7, 2: 9, 3: 0})


def delete_key_dic(di,ke):
    if ke in di:
        del di[ke]
    return di

def test_8():
    assert {1: 7, 2: 9} == delete_key_dic({1: 7, 2: 9, 3: 0},3)

def map_list_to_dict(lis1,lis2):
    if len(lis1) != len(lis2):
        return "Invalid  list"
    i = 0
    di = {}
    while i <len(lis1):
        di.update({(lis1[i],lis2[i])})
        i += 1
    print di
    return di

def test_9():
    assert {1: 7, 2: 9, 3: 0} == map_list_to_dict([1,2,3],[7,9,0])

map_list_to_dict([1,2,3],[6,7,8])


def dicationary_sorting_by_key(di):
    value = di.items()
    for i in range(0,len(value)):
        for j in range(0,i):
            if(value[i][0] > value[j][0]):
                temp = value[i]
                value[i] = value[j]
                value[j] = temp
    print "value =",value
    i =0
    di1 = {}
    while i< len(value):
        #print value[i]
        di1.update({value[i][0]:value[i][1]})
        i += 1
        print di1

dicationary_sorting_by_key({9:3,10:4,6:7})

def max_min_value_in_key(di):
    value = di.items()
    min = max = value[0][0]
    i = 0
    while i< len(value):
        if value[i][0] < min:
            min = value[i][0]
        if value[i][0] > max:
            max = value[i][0]
        i += 1
    min_max = []
    min_max.append(min)
    min_max.append(max)
    print "min and max from dict",min_max
    return min_max
def test10():
    assert [1,3] == max_min_value_in_key({1:2, 3 :4, 1:6})


def object_to_dict(obj):
    return obj.__dict__


class A():
    def __init__(self):
        print ''
        self.s =1
        self.z =2

a = A()

def test_11():
    assert {'s': 1, 'z': 2} == object_to_dict(a)


def remove_duplicate_dict(di):
    result = {}
    for key, value in di.items():
        if value not in result.values():
            result[key] = value

    return result
#remove_duplicate_dict(di1)
def test_12():
    assert {1: 6, 2: 7} == remove_duplicate_dict({1: 6, 2: 7, 1: 6})


def check_dict_isempty(di):
    if len(di) == 0:
        return True
    return False
def test13():
    assert True == check_dict_isempty({})




