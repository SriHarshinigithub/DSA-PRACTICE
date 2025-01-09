#Middle of LL

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

def lengthofLL(head):
    temp = head
    ans = 0
    while temp is not None:
        ans += 1
        temp = temp.next
    return ans


def find_middle(head):
    if head is None and head.next is None:
        return head
    length = lengthofLL(head)
    middle = length // 2
    temp = head
    count = 0
    while count < middle:
        temp = temp.next
        count += 1
    return temp 
head = find_middle(head)

print("Middle of Linked List is : ", head.data)
