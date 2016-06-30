class CountWords():
    def __init__(self):
        print("")

    def wordcoun(self):
        fo = open("foo.txt", "r+")
        str = fo.read()
       # print "Read String is : ", str
        i = 0
        count =0
        #str.split()
        print (len(str))
        while i <= len(str):
            if str[i-1] ==' ':
                count +=1
                i += 1
                while str[i-1] == ' ' or str[i-1] == ',' or str[i-1] == '.' or str[i-1] == ':':
                    i += 1
            elif str[i-1] == '\n':
                count = count+1
                i = i+1
            else:
                i += 1
        print( "Number of words in file is : ",count+1)
        wordlist = []
        wordlist = str.split()
        wordfreq = []
        for w in wordlist:
            wordfreq.append(wordlist.count(w))
       # print (wordfreq)
        #print (wordlist)
        lis = []




        for j in range(0,10):

             for i in range(0,len( wordfreq )-1):

                 for j in range(0, i+1):
                     if wordfreq[j] < wordfreq[j+1]:
                         temp = wordfreq[j]
                         wordfreq[j] = wordfreq[j+1]
                         wordfreq[j+1] = temp
                         temp1 = wordlist[j]
                         wordlist[j] = wordlist[j+1]
                         wordlist[j+1] = temp1
        output = []
        seen = set()
        for value in wordlist:
            # If value has not been encountered yet,
            # ... add it to both list and set.
            if value not in seen:
                output.append(value)
                seen.add(value)
        print(output)
        i=0

        count = 0
       # print(wordfreq)
        while(i<len(wordlist) and count <10):
                print(output[count],wordfreq[i])
                i = i+wordfreq[i]
                count += 1


s = CountWords()
s.wordcoun()