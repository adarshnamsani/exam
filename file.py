def read_from_file():
    with open("data_file.txt", "r") as file_pointer:
        words = []
        file_content = file_pointer.read()
        for word in file_content.split():
            w = ''.join([i for i in word if i.isalnum()])
            words.append(w.capitalize())

        storage = {}
        for word in words:
            storage.update({word: words.count(word)})

        for i in range(3):
            word_cnt = max(storage.values())
            for key, value in storage.iteritems():
                if value == word_cnt:
                    print word_cnt, "-", key
                    storage[key] = 0
            print "-------------"

if __name__ == "__main__":
    read_from_file()