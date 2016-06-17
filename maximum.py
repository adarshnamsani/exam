
arr=[1,2,3,4,5,6]
max_arr=[0,0,0]

max_arr[0]=arr[0]
max_arr[1]=arr[1]
max_arr[2]=arr[2]

if (max_arr[1] > max_arr[0] | max_arr[2] > max_arr[0]):
    if (max_arr[1] > max_arr[2]):
        temp=max_arr[1]
        max_arr[1]=max_arr[0]
        max_arr[0]=temp
	  
    else:
        temp=max_arr[2]
        max_arr[2]=max_arr[1]
        max1=temp

    if max_arr[2] > max_arr[1] :
        temp=max_arr[1]
        max_arr[1]=max_arr[2]
        max_arr[2]=temp
	   

    for i in range(3,len(arr)-1,1):
        if arr[i] > max_arr[0] :
            max_arr[2]=max_arr[1]
            max_arr[1]=max_arr[0] 
            max_arr[0]=arr[i]

        elif(arr[i]>max_arr[1] & arr[i]<max_arr[0]):
            max_arr[2]=max_arr[1]
            max_arr[1]=arr[i]

        elif(arr[i]>max_arr[2] & arr[i]<max_arr[1]):
            max_arr[2]=arr[i]


#print(max_arr[0],max_arr[1],max_arr[2])
