
arr=[1,2,3,4,5,6]
l=2
temp=[]

for i in range(0,l,1):
    temp.append(arr[len(arr)-l+i])

for i in range(0,4,1):
    print(i,i+l)
    arr[i+l]=arr[i]

for i in range(0,l,1):
    arr[i]=temp[i]
