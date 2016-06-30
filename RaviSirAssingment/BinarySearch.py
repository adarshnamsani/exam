class BinarySearch:
    def __init__(self):
        print("")

    def bsearch( self,arr, first, last, data):
        if first > last:
            return
        mid = int((first + last) / 2)
        if(data == arr[mid]):
            print("given number is existing in the list at location :", mid)
            return



        if (data < arr[mid]):
            return BinarySearch().bsearch(arr, first, mid-1, data)
        else:
            return BinarySearch().bsearch(arr, mid+1, last, data)


    def binarySearch(self):
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

        BinarySearch().bsearch(arr,first,last,data)







Binarysearch = BinarySearch()
Binarysearch.binarySearch()