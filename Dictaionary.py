class DictionaryItem():
    def __init__(self,key = None,value = None):
        self.key = key
        self.value = value


class Dictionary():
    def __init__(self,dic = []):
        self.dic = dic

    def create_dic(self):
        dic_obj = DictionaryItem(raw_input('Enter the key : '), raw_input('Enter the value : '))
        self.dic.append(dic_obj)

    def get_value_by_key(self,key):
        for obj in self.dic:
            if obj.key == key:
                return obj.value
        return None

    def update_key(self,key,newkey):
        for obj in self.dic:
            if obj.key == key:
                obj.key = newkey

    def delete_key(self,key):
        for obj in self.dic:
            if obj.key == key:
                self.dic.remove(obj)
    def get_all_keys(self):
        li = []
        for obj in self.dic:
            li.append(obj.key)
        return li
    def get_all_value(self):
        li = []
        for obj in self.dic:
            li.append(obj.value)
        return li
    def get_key_by_value(self,value):
        li = []
        for obj in self.dic:
            if obj.value == value:
                li.append(obj.key)
        return li
    def display_dictionary(self):
        str = []
        for obj in self.dic:
            str.append((obj.key,obj.value))
        return str


class DictionaryManager():


    def main(self):
        print "1.Add new entry !\n2.Get Key by value !\n3.Get value by key !\n4.Update a key !\n5.delete entry from Dictionary! \n6.Get all Keys \n7. Get all values\n9.Display Dictionary\nExit "
        di = Dictionary()
        while(True):
            choice = raw_input("Enter your Choice : ")
            if choice == '1':
                di.create_dic()
            elif choice == '2':
                print di.get_key_by_value(raw_input('enter the value : '))
            elif choice == '3':
                print di.get_value_by_key(raw_input('enter the key : '))
            elif choice == '4':
                di.update_key(raw_input('enter the existing key : '),raw_input('enter new key : '))
            elif choice == '5':
                di.delete_key(raw_input('enter the key : '))
            elif choice == '6':
                print di.get_all_keys()
            elif choice == '7':
                print di.get_all_value()
            elif choice == '8':
                print di.display_dictionary()

            elif choice == '9':
                return
            else:
                print "Enter The Correct choice\n1.Add new entry !\n2.Get Key by value !\n3.Get value by key !\n4.Update a key !\n5.delete entry from Dictionary! \n6.Get all Keys \n7. Get all values\n9.Display Dictionary\nExit "
               # choice = raw_input("Enter your Choice : ")


s = DictionaryManager()
s.main()



