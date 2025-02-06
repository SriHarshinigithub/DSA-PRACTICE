#length of LL using Recursion
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
#newhead = take_input_better()
#print_LL(newhead)
def LengthOFLLRecursive(head):
     if(head == None):
          return 0
     recursionAnswer = LengthOFLLRecursive(head.next)
     return 1+recursionAnswer 
headOFLL = take_input_better()
length = LengthOFLLRecursive(headOFLL)
print(length)