class Mathematics():
    def __init__(self):
        print("Calling Parent constructor")

    def squaree(self,d):
        return d *d
    def mod(self,d1,d2):
        try:
            z = d1 % d2
        except ZeroDivisionError as e:

            z = e  # representation: "<exceptions.ZeroDivisionError instance at 0x817426c>"

            print (z)  # output: "integer division or modulo by zero"
        else:
            print("return Successfully")
        return z


class child(Mathematics):
    def __init__(self):

        print("Calling child constructor")
    def child(self):
        print("calling child method")
        try:
            fh = open("test.txt", "r+")
            fh.write("This is my test file for exception handling!!")
        except IOError:
            print ("Error: can\'t find file or read data")
        else:
            print ("Written content in the file successfully")
            fh.close()




ma  = child()
y = ma.squaree(16)
zz = ma.mod(27,0)
ma.child()
print (y   ,  zz)


