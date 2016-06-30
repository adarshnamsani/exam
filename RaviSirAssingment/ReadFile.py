class ReadWords():
    def __init__(self):
        print("")

    def readfile(self):
        fo = open("foo.txt", "r+")
        str = fo.read()
        return str
       # print "Read String is : ", str
class NumberOfWords():
    def __init__(self):
        print ("")

    def countwords(self,str):
        i = 0
        count = 0
        #str.split()
        lenth = len(str)
        while i <= lenth-1:
            if str[i].isalpha()  :
                i += 1
            else:
                count += 1
                while ((str[i].isalpha()) == False) and i <lenth:
                    i += 1

        print ("Number of Words in File : ",count)

    def countwordinfile(self):
        str = ReadWords().readfile()
        self.countwords(str)
    def removenonalphabet(self,str):
        i =0
        nstr = []
        while i < len(str):
            if(str[i].isalpha()) or str[i] == ' ' or str[i] == '\n':
                nstr.append(str[i])
                i+=1
            else:
                i += 1
        nstr = ''.join(nstr)
        return nstr

class FrequencyofWords():
    def __init__(self):
        print("")
    def frequencyofwords(self,str):
        wordlist = str.split()
        wordfreq = []
        for w in wordlist:
            wordfreq.append(wordlist.count(w))
        for i in range(0, len(wordfreq)):

            for j in range(0, len(wordfreq) ):
                if wordfreq[i] > wordfreq[j]:
                    temp = wordfreq[i]
                    wordfreq[i] = wordfreq[j]
                    wordfreq[j] = temp
                    temp1 = wordlist[i]
                    wordlist[i] = wordlist[j]
                    wordlist[j] = temp1
        output = []
        seen = set()
        for value in wordlist:
            if value not in seen:
                output.append(value)
                seen.add(value)
        output1 = '\n'.join(output)
        fp = open("test.txt",'w')
        fp.write(output1)
        fp.close()
        i = 0

        count = 0
        print("wordfrw = ",wordfreq)
        # print(wordfreq)
        while (i < len(wordlist) and count < 10):
            print(output[count], wordfreq[i])
            i = i + wordfreq[i]
            count += 1




#fp = ReadWords().readfile()
num = NumberOfWords()
num.countwordinfile()
#fq = FrequencyofWords()
#num.countwords(fp)

#fq.frequencyofwords(num.removenonalphabet(fp))