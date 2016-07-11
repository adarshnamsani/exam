class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class LL:
    def __init__(self):
        self.head=None
        self.tail=None

    def add(self,data):
        node=Node(data)
        if self.head==None:
            self.head=node
            self.tail=node
        else:
            self.tail.next=node
            self.tail=node

    def __str__(self):
        s=""
        curr=self.head
        while curr.next!=None:
            s=s+" "+str(curr.data)
            curr=curr.next
        s=s+" "+str(curr.data)
        #print s NO NEED TO PRINT JUST RETURN
        return s

    # def printLL(self):
    #     curr=self.head
    #     while curr!=None:
    #         print curr.data
    #         curr=curr.next


# if __name__=="__main__":
#     head=LL()
#     head.add(5)
#     head.add(10)
#     head.add(15)
#     head.add(20)
#     head.printLL()