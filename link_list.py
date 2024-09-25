"""link list toturial """
# 0.5
class Node:
    """data container and next node address"""
    def __init__(self,data=None):
        self.data = data
        self.next = None

class Linked_list:
    def __init__(self)-> None:
        self.head = None
        self.length = 0


    def push(self, data)->None:
        new_node = Node(data)
        new_node.next= self.head
        self.head = new_node
        self.length+=1

    def append(self, data)->None:
        temp = self.head
        while temp.next:
            temp = temp.next
        else:
            temp.next = Node(data)
        self.length+=1
    def insert(self, index:int, data)->None:
        if index <= 0:
            self.push(data)
        elif index >= self.length:
            self.append(data)
        else:
            temp= self.head
            new_node = Node(data)
            for i in range(index-1):
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
            self.length += 1
    
    def rev1(self):
        prv = self.head
        mid = self.head.next
        nex = self.head.next.next
        prv.next = None
        while nex.next:
            mid.next = prv
            prv = mid
            mid = nex
            nex = nex.next
        else:
            mid.next = prv
            nex.next = mid
            self.head = nex
    
    def rev2(self):
        pre = None
        cur = self.head
        while cur:
            _next = cur.next
            cur.next = pre
            pre = cur
            cur = _next
        self.head = pre
            
    def seter(self, lst:list)-> None:
        for item in lst:
            self.append(item)
    def pop(self,index=None):
        if index is None or index>=self.length: 
            temp = self.head
            while temp.next.next:
                temp = temp.next
            else:
                self.length-=1
                val = temp.next.data
                temp.next = None
                return val
        elif index<=0:
            self.length-=1
            val = self.head.data
            self.head = self.head.next
            return val
        else:
            temp = pre = self.head
            while index:
                pre = temp
                temp = temp.next
                index-=1
            else:
                pre.next = temp.next
                temp.next=None
                self.length-=1
                return temp.data
    def isempty(self):
        return self.length == 0
    
    def __repr__(self)->str:
        text = str()
        temp = self.head
        while temp.next:
            text += str(temp.data) + " >> "
            temp = temp.next
        else:
            text += str(temp.data)
        return f"[ {text} ]"

    def __len__(self)->int:
        return self.length



ll = Linked_list()
ll.push(0)
ll.push(2)
ll.push(5)
ll.push(1)
ll.append("amir")
ll.append("kol")
print(ll)
ll.rev2()
print(ll)
print(ll.pop(0))
print(ll)
