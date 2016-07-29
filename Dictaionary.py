class DictaionaryItem():
    def __init__(self,key = None,value = None):
        self.key = key
        self.value = value


class Dictaionary():
    def __init__(self,dic = None):
        self.dic = dic

    def get_by_value(self,value):
        for obj in self.dic:
            if obj.value == value:
                return obj.key

        return None
    def get_by_key(self,key):
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

class DictaionaryManager():
    cd = []
    def create_dic(self):
        dic_obj = DictaionaryItem(raw_input('Enter the key : '),raw_input('Enter the value : '))
        self.cd.append(dic_obj)

    def main(self):
        print "1.Add new entry !\n2.Get Key by value !\n3.Get value by key !\n4.Update a key !\n5.delete entry from dictaionary! \n6.Exit"
        while(True):
            choice = raw_input("Enter your Choice : ")
            if choice == '1':
                self.create_dic()
            elif choice == '2':
                print Dictaionary(self.cd).get_by_value(raw_input('enter the value : '))
            elif choice == '3':
                print Dictaionary(self.cd).get_by_key(raw_input('enter the key : '))
            elif choice == '4':
                Dictaionary(self.cd).update_key(raw_input('enter the existing key : '),raw_input('enter new key : '))
            elif choice == '5':
                Dictaionary(self.cd).delete_key(raw_input('enter the key : '))
            else:
                return


s = DictaionaryManager()
s.main()



