arr = [int(x) for x in input("Enter the arr ele with space:").split()]
n= int(input("enter the int.rot.factor:"))

def rotate_left(arr,n):
    if n < len(arr) and n > 0:
        for x in arr[:n]:
            arr.append(arr.pop(0))

    print(arr)

rotate_left(arr,n)