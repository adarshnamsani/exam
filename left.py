
arr=[1,2,3,4,5,6]
l=2
temp=[]

for i in range(0,l,1):
    temp.append(arr[i])

for i in range(0,len(arr)-l,1):
    arr[i]=arr[i+l]

for i in range(0,l,1):
    arr[i+len(arr)-l]=temp[i]
