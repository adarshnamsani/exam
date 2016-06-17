arr = [int(x) for x in input("enter nmbrs with space:").split()]
print("given array {}".format(arr))

def max_3(arr):
    max_arr = []
    for x in range(3):
        k = max(arr)
        max_arr.append(k)
        arr.remove(k)

    print(max_arr)

max_3(arr)

