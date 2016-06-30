class TinarySearch:
    def __init__(self):
        print("")

    def tsearch( self,arr, first, last, data):
        if first > last:
            return
        t1 = (int (first + ( last - first)/3))
        t2 = (int (t1 + (last -first)/3))

        if(data == arr[t1]):
            print("given number is existing in the list at location :", t1)
            return
        if(data == arr[t2]):
            print("given number is existing in the list at location :", t2)
            return
        elif data < arr[t1]:
            return TinarySearch().tsearch(arr, first, t1 - 1, data)
        elif data > arr[t2]:
            print(t2 + 1, last)
            return TinarySearch().tsearch(arr, t2 + 1, last, data)
        elif (data >arr[t1]) and (data < arr[t2]):
            print (t1+1,t2)
            return TinarySearch().tsearch(arr, t1+1, t2-1 , data)





    def ternarySearch(self):
        print("Enter the size of list and element in the list " )
        n = int(input())
        arr = []
        for i in range(0, n):
                try:
                    arr.append(int(input()))

                except ValueError:
                    print("Err.. numbers only")

        first = 0
        last = n-1


        data = int (input('Enter the number '))

        TinarySearch().tsearch(arr,first,last,data)







ternarysearch = TinarySearch()
ternarysearch.ternarySearch()