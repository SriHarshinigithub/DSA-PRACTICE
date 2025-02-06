#Insert at head
class Node:
    def __init__(self,value):
        self.data = value
        self.next = None
def print_LL(head):
        temp = head
        while (temp!=None):
            print(temp.data,end = "->")
            temp = temp.next 
        print()
        return
def take_input_better():
     value = int(input("Enter the value of node:"))
     head = None
     tail = None
     while(value!=-1):
          newNode = Node(value)
          if(head == None):
               head = newNode
               tail = newNode
          else:
               tail.next = newNode
               tail = newNode 
          value = int(input("Enter the value of node:")) 
     return head
head = take_input_better()
print_LL(head)
def insert_at_head(head,data):
    newNode = Node(data)
    newNode.next = head
    head = newNode
    return head
head = insert_at_head(head,100)
print_LL(head)