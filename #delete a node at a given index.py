#delete a node at a given index
class Node:
    def __init__(self,value):
        self.data = value
        self.next = None
def print_LL(head):
    temp = head
    while temp!= None:
        print(temp.data,end="->")
        temp = temp.next
    print()
    return
def take_input_better():
    value = int(input("Enter a node value:"))
    head = None
    tail= None
    while value!=-1:
        newNode = Node(value)
        if head == None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode
        value = int(input("Enter the value of Node:"))
    return head
head = take_input_better()
print_LL(head)


def delete_at_index(head,index):
    if(head == None):
        print("LL is Empty")
        return head
    if index == 0:
        return head.next
    temp = head
    count = 0
    while temp is not None and count < index - 1:
        temp = temp.next
        count += 1
    if temp is None and temp.next is None:
        print("Out of Bounds:")
        return head
    nodeToBeDeleted = temp.next
    nodeAfterDeletedNode = nodeToBeDeleted.next
    temp.next = nodeAfterDeletedNode
    return head
head = delete_at_index(head,3)
print("After Deletion")
print_LL(head)
