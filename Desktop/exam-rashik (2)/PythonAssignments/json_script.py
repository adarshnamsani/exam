from random import shuffle
import json

def shuffling():
    l=[1,2,3,4,5]
    shuffle(l)
    ans=""
    for i in range(5):
        ans=ans+str(l[i])
    return ans

def shuffle_alpha():
    l=['a','b','c','d','e']
    shuffle(l)
    ans = ""
    for i in range(5):
        ans = ans + str(l[i])
    return ans

def generate():
    ans='{"By":[{"name":"rashik","dob":"29.7.1994"}],"status":"Good","CustomFurnish":[{"product_id":['
    for i in range(1000):
        x=shuffling()
        ans=ans+x+','
    ans=ans+str(1000)
    ans=ans+"],"
    ans=ans+'"images":['
    for i in range(1000):
        ans=ans+'['
        for x in range(4):
            p=shuffle_alpha()
            ans=ans+'"'+p+'"'+','
            #print ans
        ans=ans+'"hello"],'
    ans=ans+'["abcd","defg","hijk","lmno","pqrst"]'
    ans=ans+']}]}'
    #print ans
    ans=json.loads(ans)
    print ans
    print json.dumps(ans,indent=4)
    print "Status is: ",ans['status']
    print "Created By: ",ans['By'][0]['name']
    for i in range(1001):
        print "PRODUCT ID::",ans['CustomFurnish'][0]['product_id'][i]
        print "IMAGE URLS'S",ans['CustomFurnish'][0]['images'][i]


if __name__=="__main__":
    generate()
