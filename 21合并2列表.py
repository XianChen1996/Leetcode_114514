class Listnode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Linklist:
    def __init__(self):
       self.head=None

    def initList(self,data):
        self.head = Listnode(data[0])
        r=self.head
        p=self.head
        for i in data[1:]:
            node = Listnode(i)
            p.next = node
            p = p.next
        return r

    def printlist(self,head):
        if head == None: return
        node = head
        while node != None:
            print(node.val , end=' ')
            node = node.next

class Solution:
    def mergeTwoLists(self,l1,l2):
        head = Listnode(0)
        first =  head
        while l1!= None and l2 != None:
            if l1.val <=l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2= l2.next
            head = head.next
        if l1 != None:
            head.next = l1
        elif l2 !=None:
            head.next= l2
        return first.next

###21题的合并链表

if __name__ == '__main__':
    a=Solution()
    l=Linklist()
    data1=[1,2,3]
    data2=[2,4,6]
    l1=l.initList(data1)
    l.printlist(l1)
    print("\n")
    l2 = l.initList(data2)
    l.printlist(l2)
    m=a.mergeTwoLists(l1,l2)
    print("\n")
    l.printlist(m)
