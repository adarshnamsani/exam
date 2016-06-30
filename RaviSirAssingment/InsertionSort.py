class InsertionSort():

    def __init__(self):
        print("This is Insertion Sort Constructor")

    def insertionsort(self):
        print ("Enter The Number in list ")
        n = int(input(''))
        a = []
        for i in  range(0,n):
            try:
                a.append(int(input()))

            except ValueError:
                print("Err.. numbers only")



        for i in range(0,n):
            index = a[i]
            j =i

            while j>0 and a[j-1] >index:
                a[j] = a[j-1]
                j -= 1
            a[j] = index

        print(a)


ins = InsertionSort()
ins.insertionsort()
print ("Thank you")
