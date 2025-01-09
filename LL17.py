#delete a node recursively
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

def delete_at_index_recursively(head,index):
    if head is None:
        print("Index is out of bounds")
        return None
    if index == 0:
        return head.next
    head.next = delete_at_index_recursively(head.next,index-1)
    return head
head = delete_at_index_recursively(head,3)
print("After Deletion")
print_LL(head)
