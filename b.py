a=[1,2,3,4,5,6]
j=0
d=2
n=len(a)
i=n-1
temp=0
while j!=d:
    temp=a[i]
    while i>0:
        a[i]=a[i-1]
        i-=1
    a[i]=temp
    j+=1
    i=n-1
print(a)

        
