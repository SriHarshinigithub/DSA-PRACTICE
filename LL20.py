#merge two sorted linkedlist

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

def merge_sorted_lists(head1,head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    finalhead = None
    finaltail = None
    while head1 is not None and head2 is not None:
        if head1.data < head2.data:
            if finalhead is None:
                finalhead = head1
                finaltail = head1
            else:
                finaltail.next = head1
                finaltail = head1
            head1 = head1.next
        else:
            if finalhead is None:
                finalhead = head2
                finaltail = head2
            else:
                finaltail.next = head2
                finaltail = head2
            head2 = head2.next
    if head1 is not None:
        finaltail.next = head1
    if head2 is not None:
        finaltail.next = head2
    return finalhead
print("Enter elements for the first sorted linked list:")
head1 = take_input_better()
print("Enter elements for the second sorted linked list:")
head2 = take_input_better()
print("First Linked List:")
print_LL(head1)
print("Second Linked List:")
print_LL(head2)
print("Merged Linked List:")
finalhead = merge_sorted_lists(head1,head2)
print_LL(finalhead)