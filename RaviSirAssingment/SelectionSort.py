class SelectionSort():

    def __init__(self):
        print("This is Selection Sort Constructor")

    def selectionsort(self):
        print ("Enter The Number in list ")
        n = int(input(''))
        a = []
        for i in  range(0,n):
            try:
                a.append(int(input()))

            except ValueError:
                print("Err.. numbers only")



        for i in range(0,n):
            min = i
            j = i+1
            for j in range (0,i):
                if a[j] > a[min]:
                    min = j
                temp = a[i]
                a[i] = a[min]
                a[min]  = temp
        print(a)


sel = SelectionSort()
sel.selectionsort()
print ("Thank you")

