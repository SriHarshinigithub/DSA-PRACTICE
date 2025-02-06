#Delete at tail node recursively

class Node:
    def __init__(self, data):
        self.data = data
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

def delete_at_tail_recursively(head):
     if head is None:
          return None
     if head.next is None:
          return None
     head.next = delete_at_tail_recursively(head.next)
     return head
head = delete_at_tail_recursively(head)
print("After Deletion at tail")
print_LL(head)
