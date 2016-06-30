def linearSearch():
    print("Enter the Number Of Elements")
    x = int(input())
    arr= []
    for i in range(0,x):
        arr.append(input())
    i =0
    y = input('Please Enter the Number ')
    for i in range(0,x):
        if y == arr[i]:
            return print("Element exist in the list")
linearSearch()