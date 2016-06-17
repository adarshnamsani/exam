arr = [int(x) for x in input("Enter the arr.ele.with.space:").split()]
n = int(input("Enter the rot.factor:"))

def rotate_right(arr,n):
    if n < len(arr) and n > 0:
        for x in range(n):
            k = arr.pop(len(arr)-1)
            arr.insert(0,k)

    print(arr)

rotate_right(arr,n)