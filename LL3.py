#print 123 twice
class Node:
    def __init__(self,value):
        self.data = value
        self.next = None
first = Node(1)
second = Node(2)
third = Node(3)
print(id(first), id(second), id(third))

first.next = second
second.next = third 
head = first 
def print_LL(head):
        temp = head
        while (temp!=None):
            print(temp.data)
            temp = temp.next
        temp = head
        while(temp!=None):
             print(temp.data)
             temp = temp.next
        return
print_LL(head)