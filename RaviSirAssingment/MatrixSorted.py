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

        j = col
        for i in range(0,row):

            curr = x[i][j-1]
            while x[i][j-1] >= value:
                if value == x[i][j-1]:
                    print("value exisit ")
                    return
                j -= 1
                if j < 0:
                    return


        print("Given value doesnt exist in matrix")




s = SortedMatrix()
s.sorted_matrix()