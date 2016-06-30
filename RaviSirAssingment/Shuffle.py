def shuffle(lis1,lis2):
    count1 = []
    count2 = []


    for i in range(0,26):
        count1.append(0)
        count2.append(0)
    for i in range(0,len(lis1)):
        pos = ord(lis1[i]) - ord('a')
        count1[pos] += 1
    for i in range(0, len(lis2)):
        pos = ord(lis2[i]) - ord('a')
        count2[pos] += 1
    i =0
    flag =0
    while(i<26and flag ==0):
        if count1[i] == count2[i]:
            i +=1
        else:
            flag =1
    if flag ==1:
        print("Not shuffle lisr")
    else:
        print("Shuffle List")

shuffle("bcc","cbc")