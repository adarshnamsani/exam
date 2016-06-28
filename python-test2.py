import random
myList = [1, 2, 3, 4, 5]
def sum_of_list(lis):
    if lis == None:
        return None
    sum =0
    for word in lis:
        sum = sum + word
    print(sum)
    return sum

def mul_of_list(lis):
    if lis == None:
        return None
    mul =0
    for word in lis:
        mul = mul * int(word)
    print(mul)
    return mul
def small_and_larg_inlis(lis):
    if lis == None:
        return None
    min = max = lis[0]
    for i in range(0,len(lis)):
        if(min > lis[i]):
            min = lis[i]
        if(max < lis[i]):
            max = lis[i]
    minmax = []
    minmax.append(min)
    minmax.append(max)
    return minmax


def palindrom(str):
    x = len(str) - 1;
    for i in range(0, x):
        if str[i] != str[x]:
            return False
        else:
            x = x - 1
    return True

def string_equality(lis):
    count =0

    for words in lis:
        j = words.split()
        if j[0] == j[len(j)-1]:
            count += 1


def sorted_tupple_list(lis):
    for i in range(0, len(lis)):
        for j in range(0, len(lis)):
            if (lis[i][1] < lis[j][1]):
                temp = lis[i]
                lis[i] = lis[j]
                lis[j] = temp
    print(lis)

def remove_duplicate(lis):
    l = []
    seen = set()
    for value in lis:
        if value not in seen:
            l.append(value)
            seen.add(value)
    print(l)


def check_list_empty(lis):
    if not lis:
        return True
    else:
        False


def count_word_length(lis):
    l = lis.split()
    print(l)
    nst = []
    for word in l:
        if len(word) > 2:
            nst.append(word)
    return nst




def common_word_in_list(lis1,lis2):
    if set(lis1).intersection(lis2):
        return True
    else:
        return False

def remove_alternate_from_list(lis):
    arr = []
    for i in range(0,len(lis)):
        if( i != 0 and i != 2 and i != 4 and i != 5):
            arr.append(lis[i])
    return arr


def remove_non_alpha(str):
    newstr = []
    for i in range(0,len(str)):
        if(str[i].isalpha() ):
            newstr.append(str[i])

def remove_even_number(lis):
    newlis = []
    for words in lis:
        k = int(words)
        if k%2 != 0:
            newlis.append(k)
    return newlis


def shuffle_list(lis):
    print("",lis)
'''



'''
def random_number(lis):
    import random
    while ():
        if( random.randrange(1,900)):
            print("")

def permutations(head, tail=''):
    arr = []
    if len(head) == 0:
        arr.append(tail)
    else:
        for i in range(len(head)):
            permutations(head[0:i] + head[i+1:], tail+head[i])
    return arr



def difference_list(lis1,lis2):
    lis2 = set(lis2)
    return [item for item in lis1 if item not in lis2]


def index_in_list(lis,item):
    count =0
    for i in lis:
        if i == item:
            return count
        count += 1



def remove_adjcence(lis,length):
    arr = []
    for i in range(0,length-1):
        if(lis[i] != lis[i+1]):
            arr.append(lis[i])
    k = int(len(arr))
    if(lis[length-1] != arr[k-1]):
        arr.append(lis[length-1])
    print(arr)
    return arr


def append_lis(lis1,lis2):
    for words in lis2:
        lis1.append(words)
    return lis1

def select_random(lis,item):
    import random
    k =random.randrange(0,len(lis)-1)
    return lis[k]
