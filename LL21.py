#reverse ll recursion optimized

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
head = take_input_better()
print("Original LL:")
print_LL(head)


def reverse_linked_list_recursive(head):
    if head is None or head.next is None:
        return head
    smallLinkedListHead = reverse_linked_list_recursive(head.next)
    tailofReversedList = head.next 
    tailofReversedList.next = head
    head.next = None
    return smallLinkedListHead
head = reverse_linked_list_recursive(head)
print("Reversed Linked List:")
print_LL(head)