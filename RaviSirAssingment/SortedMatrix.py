class SortedMatrix:
    def __init__(self):
        print( "")
    def sorted_matrix(self):
        row = int(input('Enter the number of row : '))
        col = int(input('Enter the number of column : '))
        x = []
        for i in range(0, row):
            x.append([])
            for j in range(0,col):
                x[i].append(int(input()))
        print(x)
        value = int(input('Enter the value which you want to find in matrix : ' ))


        for i in range(0,row):
            if ((x[i][col-1] >= value)) and (x[i][0] <= value):

                j =col
                while j >0:
                     if x[i][j - 1] == value:
                         print("value successfully find ")
                         return
                     j -= 1

                return print("Element Doesnt Exist")

        print("Given value doesnt exist in matrix")




s = SortedMatrix()
s.sorted_matrix()
