a=[8,0,5,15,2,13,7,10]
c=[]
i=0
j=0
k=0
temp=a[0]
n=len(a)
while i<n-1:
    if a[i]>temp:
        temp=a[i]
    i+=1
c.append(temp)

k+=1
for i in a:
    temp=a[0]
    while j<=n-1:
     
        if a[j]>temp and a[j]<c[k-1]:
            temp=a[j]
        j+=1
    if k!=3:
        c.append(temp)
        k+=1
    
    j=0
print(c)
