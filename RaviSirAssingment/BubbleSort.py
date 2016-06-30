class BubbleSort():

    def __init__(self):
        print("This is Bubble Sort Constructor")

    def Bubblesort(self):
        print ("Enter The Number in list ")
        n = int(input(''))
        a = []
        for i in  range(0,n):
            try:
                a.append(int(input()))

            except ValueError:
                print("Err.. numbers only")



        for i in range(0,n):
            for j in range (0,i):
                if a[i] <a[j]:
                    temp = a[i]
                    a[i] = a[j]
                    a[j]  = temp
        print(a)


Bub = BubbleSort()
Bub.Bubblesort()
print ("Thank you")



