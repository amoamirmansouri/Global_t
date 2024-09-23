"""link list toturial """
# 2.5
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
        elif index == self.length:
            self.append(data)
        else:
            temp= self.head
            new_node = Node(data)
            for i in range(index-1):
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
            self.length += 1
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
ll.push(2)
ll.push(5)
ll.push(1)
ll.append("amir")
ll.append("kol")
ll.push(0)
print(ll)
#ll.insert(0,"number(0) test")
#ll.insert(len(ll),f"number({len(ll)}) test")
ll.insert(3,"number(3) test")
print(ll)
