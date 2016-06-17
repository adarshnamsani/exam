arr =[int(x) for x in input().split()]

def sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j]<arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp

print ("Initial array: {}".format(arr))
sort(arr)
max_array=[]
for x in arr[:3]:
    max_array.append(x)

print(max_array)



