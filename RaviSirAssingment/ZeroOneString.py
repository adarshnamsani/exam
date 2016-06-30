class ZeroOneString:
    def __init__(self):
        print ("")
    def zeronetring(self):
        x = input('Enter a string in like "01010"\n')
        print (x)
        y = len(x)
        w = []
        z = []
        for i in range(0,y):
            if x[i] == '0':
                w.append(x[i])
            elif x[i] == '1':
                z.append(x[i])
            else:
                print ("invalid string")
                return
        x = ''.join(w+z)

        print (x)
z = ZeroOneString()
z.zeronetring()