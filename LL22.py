#reverse ll using Iteration

class Node:
    def __init__(self, data=None):
        self.data = data
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
#head = take_input_better()
#print_LL(head)

def reverse_LL(head):
    if head is None or head.next is None:
        return head
    prev = None
    current = head
    while current is not None:
        next_node = current.next 
        current.next = prev
        prev = current
        current = next_node
    return prev

head = take_input_better()
print("Original LL:")
print_LL(head)

head = reverse_LL(head)
print("Reversed LL:")
print_LL(head)