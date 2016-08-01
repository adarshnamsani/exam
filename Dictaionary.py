class DictionaryItem():
    def __init__(self,key = None,value = []):
        self.key = key
        self.value = value


class Dictionary():
    def __init__(self,dic = []):
        self.dic = dic

    def add_entry(self,key,value):
        dic_obj = DictionaryItem(key,value)
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

    def delete_entry(self,key):
        for obj in self.dic:
            if obj.key == key:
                self.dic.remove(obj)
    def get_all_keys(self):
        li = []
        for obj in self.dic:
            li.append(obj.key)
        return li
    def get_all_values(self):
        li = []
        for obj in self.dic:
            li.append(obj.value)
        return li
    def get_keys_by_value(self,value):
        li = []
        for obj in self.dic:
            if value in  obj.value :
                li.append(obj.key)
        return li
    def get_all_items(self):
        str = []
        for obj in self.dic:
            str.append((obj.key,obj.value))
        return str

    def update_value(self,key,value):
        for obj in self.dic:
            if obj.key == key:
                obj.value = value
                return True
        return False
    def add_value_to_existing_key(self,key,value):
        for obj in self.dic:
            li = []
            li.append(value)
            if obj.key == key:
                li.append(obj.value)
            obj.value = li


class DictionaryManager():

    def main(self):
        print "1.Add new entry !\n2.Get Key by value !\n3.Get value by key !\n4.Update a key !\n5.delete entry from Dictionary!" \
              " \n6.Get all Keys \n7. Get all values\n8.Display Dictionary\nUpdate the value\n10.Update the value\n11. Add new value to existing key\n Exit "
        di = Dictionary()
        while(True):
            choice = raw_input("Enter your Choice : ")
            if choice == '1':
                key = raw_input('Enter the key : ')
                value = raw_input('Enter the value : ')
                di.add_entry(key,value)
            elif choice == '2':
                print di.get_keys_by_value(raw_input('enter the value : '))
            elif choice == '3':
                print di.get_value_by_key(raw_input('enter the key : '))
            elif choice == '4':
                di.update_key(raw_input('enter the existing key : '),raw_input('enter new key : '))
            elif choice == '5':
                di.delete_entry(raw_input('enter the key : '))
            elif choice == '6':
                print di.get_all_keys()
            elif choice == '7':
                print di.get_all_values()
            elif choice == '8':
                print di.get_all_items()

            elif choice == '9':
                key = raw_input('Enter the key : ')
                newvalue = raw_input('Enter the New value : ')
                di.update_value(key,newvalue)
            elif choice == '10':
                key = raw_input('Enter the key : ')
                value = raw_input('Enter the new value')
                di.update_value(key,value)
            elif choice == '11':
                key = raw_input('Enter the key : ')
                value = raw_input('Enter the new value')
                di.add_value_to_existing_key(key, value)
            elif choice == '12':
                return

            else:
                print "Enter The Correct choice\n1.Add new entry !\n2.Get Key by value !\n3.Get value by key !\n4.Update a key !" \
                      "\n5.delete entry from Dictionary! \n6.Get all Keys \n7. Get all values\n8.Display Dictionary\n 9. Update the value\nExit "
               # choice = raw_input("Enter your Choice : ")


s = DictionaryManager()
s.main()



