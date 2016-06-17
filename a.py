a=[1,2,3,4,5,6]
i=0
j=0
d=2
n=len(a)
temp=0
while j!=d:
    temp=a[i]
    while i<n-1:
        a[i]=a[i+1]
        i+=1
    a[i]=temp
        
    j+=1
    i=0
print(a)
