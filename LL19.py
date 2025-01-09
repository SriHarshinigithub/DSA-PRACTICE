#middle of ll using two pointer


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
print_LL(head)

def middle_of_ll_two_pointers(head):
    if head == None or head.next == None:
        return head
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = slow.next.next
    return slow
midlle_value = middle_of_ll_two_pointers(head)
print("Middle of the linked list is: ", midlle_value.data)

