

class hashMap(object):
    def __init__(self):
        self.size = 6
        self.map = [None] * self.size

    def _get_index(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % self.size

    def add(self,key,value):
        key_hash = self._get_index(key)
        key_value = [key, value]

        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
                self.map[key_hash].append(key_value)
                return True

    def get(self,key):
        key_hash = self._get_index(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    print pair[1]
        return None

    def delete(self,key):
        key_hash = self._get_index(key)
        if self.map[key_hash] is None:
            return False
        for i in range(0,len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True

    def display(self):
        for item in self.map:
            if item is not None:
                print (str(item))

if __name__ == "__main__":
    h = hashMap()
    while (1):
        print "1. input 2. display 3.search_key "
        choice = int(raw_input("enter choice : "))
        if choice == 1:
            key = raw_input("enter key : ")
            value = raw_input("enter value : ")
            h.add(key,value)

        elif choice == 2:
            h.display()

        elif choice == 3:
            key = raw_input("enter key to be searched : ")
            h.get(key)

        else:
            print "Incorrect choice"







