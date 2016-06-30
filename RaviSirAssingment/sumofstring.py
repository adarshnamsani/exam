print ("Hello Python")
def sumOfString(x,y):
    x1 = int(x)
    y1 = int(y)
    type(x)
    type(y)
    print (x1+y1)
    return;

def multipilicationOfString(x,y):
    x1 = int(x)
    y1 = int(y)
    print (x1* y1)
    return


def divisionOfString(x,y):
    x1 = int(x)
    y1 = int(y)
    print (x1/y1)
    return
def substractionOfString(x,y):
    x1 = int(x)
    y1 = int(y)
    print (x1-y1)
    return


count =1
while(count ==1):
    x = input('Enter The First String  : ')
    y = input('Enter The Second String : ')
    print ("sum of x and y is ")
    sumOfString(x,y)
    print ("multiplaction of x and y")
    multipilicationOfString(x,y)
    print ("division of string x and y")
    divisionOfString(x,y)
    print ("substraction of two string")
    substractionOfString(x,y)
    print ("please enter 0 for exit /nFor continue enter 1")
    count =int( input(''))

print ("Thank You")
