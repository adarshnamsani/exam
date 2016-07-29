class Dictaionary():
    def __init__(self,key = None,value = None):
        self.key = key
        self.value = value

    def get_by_value(self,dic,value):
        for obj in dic:
            if obj.value == value:
                return obj.key

        return "Value not exist "
    def get_by_key(self,dic,key):
        for obj in dic:
            if obj.key == key:
                return obj.value

        return "Key not exist "

    def update_key(self,dic,key,newkey):
        for obj in dic:
            if obj.key == key:
                obj.key = newkey

    def delete_key(self,dic,key):
        for obj in dic:
            if obj.key == key:
                dic.remove(obj)

class DictaionaryManager():
    cd = []
    def create_dic(self):
        dic_obj = Dictaionary(raw_input('Enter the key'),raw_input('Enter the value'))
        self.cd.append(dic_obj)

    def main(self):
        print "1.Add new entry !\n2.Get Key by value !\n3.Get value by key !\n4.Update a key !\n5.delete entry from dictaionary! \n6.Exit"
        while(True):
            choice = raw_input("Enter your Choice")
            if choice == '1':
                self.create_dic()
            elif choice == '2':
                print Dictaionary().get_by_value(self.cd,raw_input('enter the value'))
            elif choice == '3':
                print Dictaionary().get_by_key(self.cd,raw_input('enter the key'))
            elif choice == '4':
                Dictaionary().update_key(self.cd,raw_input('enter the existing key'),raw_input('enter new key'))
            elif choice == '5':
                Dictaionary().delete_key(self.cd,raw_input('enter the key'))
            else:
                return


s = DictaionaryManager()
s.main()



