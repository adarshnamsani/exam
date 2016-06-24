from placeholders import *
def get_odds_list(count):
    lis = []

    while (count):
        lis.append(count * 2 - 1)
        count = count - 1

    return lis
    """
     This method returns a list of the first 'count' odd numbers in descending
     order. e.g count = 3 should return [5,3,1]
    """

def get_odd_mountain(count):
    count = int(count)
    lis = []
    i = 0
    if (count == 0):
        return lis
    flag = count/2
    while (count ):
        if (count > flag):
            lis.append(i * 2 + 1)

        if (count <=flag):
            lis.append(2 * (flag ) - 1)
            flag = flag - 1
        count = count - 1
        i = i + 1
    return lis
    """
    odd mountain is a list of odd numbers going up from 1 and then back to 1.
     e.g. odd_mountain of size 5 is [1,3,5,3,1]
    odd_mountain of size 4 is [1,3,3,1]
    Hint: use the list functions and a builtin function we have already seen.
    a.append(int(input()))
    """

def get_multiples_desc(number, count):
    lis = []
    for i in range(0,count):
        lis.append(number*count)
        count = count -1
    return lis

    """
    return the first count multiples of number in desc order in a list.
    e.g call with input (3,2) returns [6,3]
    call with input(5,3) returns [15,10, 5]
    Hint: one line of code, use a builtin function we have already seen in the lists lesson.
    """


def get_sorted_diff_string(first, second):
    len1 = len(first)
    len2 = len(second)
    if len1 >len2 :
        len2 = len1
    else :
        len1 = len2
    z = ""
    for i in range(0,len1):
        for j in range(0,len2):
            if first[i] == second[j]:
               break
            elif flag != 1:
                z.append(first[i])


    k = sorted(z)
    k = "".join(k)
    return k


    """
    returns a string which contains letters in first but not in second.
    e.g.s apple and pig returns ael.
    """

def get_sorted_without_duplicates(input):
    output = []
    k = ""
    seen = set()
    for value in input:
        if value not in seen:
            output.append(value)
            seen.add(value)
    k = sorted(output)
    k = "".join(k)
    return k


    """
    returns a string in which characters are sorted and duplicates removed
    e.g apple returns aelp, engine returns egin
    """
    return None
def create_palindrome(word):
    if word==None:
        return None
    else:
        s = word[::-1]
        z = word+s

    return z





# Sort the words that are passed in by word length instead of word content.
# e.g ["apple", "dog", "elephant"] should result in ["elephant", "apple", "dog"]
# hint: use list.sort, don't write your own
def sort_by_length(words):
    k = []
    if words == None:
        return None
    for word in sorted(words, key=lambda word: len(word), reverse=True):
            k.append( word)
    print (k)
    return k
    



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
