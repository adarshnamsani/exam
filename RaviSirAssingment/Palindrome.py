class Palindrome:
    def __init__(self):
        print("This class for check , The given Number is valid Palindrome or not")

    def palindrom(self):
        print ("Please Enter a String")
        str = input()
        x = len(str) -1;
        for i in range(0,x):
            if str[i] != str[x]:
                print("Not a Valid Palindrome String")
                return
            else:
                x =  x- 1
        print ("Given String is a valid Palindrome")




palindrom = Palindrome()
palindrom.palindrom()
print("Thank You")
