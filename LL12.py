#insert at index recursively
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

def insert_at_tail(head,data):
     newNode = Node(data)
     if(head is None):
          return newNode
     temp = head
     while(temp.next!=None):
          temp = temp.next
     temp.next = newNode
     return head
def insert_at_index_recursively(head,data,index):
     if(index == 0):
          return insert_at_head(head,data)
     if(head == None):
          print("Index is out of bounds")
          return head
     head.next = insert_at_index_recursively(head.next,data,index-1)
     return head
head = insert_at_index_recursively(head,35,0)
print("After Inserting at Index :")
print_LL(head)