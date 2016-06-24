arr=[10,1,9,4,10,3,2,10,9]
max_arr=[]
n=3
dup=100

while n:
    max=arr[0]
    for i in arr:
        if(i>max and i<dup):
            max=i
        
    dup=max
    max_arr.append(max)
    n-=1 

print(max_arr)
