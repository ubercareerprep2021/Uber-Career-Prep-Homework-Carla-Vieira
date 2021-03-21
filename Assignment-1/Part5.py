from Part4 import *

def reverseLinkedListIterative(linkedList: SinglyLinkedList):
    pointer = linkedList.head
    previous_node = None
    while pointer:
        posterior_node = pointer.next
        pointer.next = previous_node
        previous_node = pointer
        pointer = posterior_node
    linkedList.head = previous_node
    return linkedList

def reverseLinkedListStack(linkedList: SinglyLinkedList):
    newLinkedList =  SinglyLinkedList()
    pointer = linkedList.head
    aux_list = []
    while pointer:
        aux_list.append(pointer.value)
        pointer = pointer.next
    while aux_list:
        newLinkedList.push(Node(aux_list.pop()))
    return newLinkedList

def reverseLinkedListRecursive(linkedList: SinglyLinkedList):
    if linkedList.head == None: return SinglyLinkedList()
    if linkedList.head.next == None:
        llist = SinglyLinkedList()
        llist.push(Node(linkedList.head.value))
        return llist
    templlist = SinglyLinkedList()
    templlist.head = linkedList.head.next
    llist = reverseLinkedListRecursive(templlist)
    llist.push(Node(linkedList.head.value))
    return llist

'''                 
Complexity Analysis:

Time Complexity:
  reverseLinkedListIterative(): O(n)      
  reverseLinkedListStack(): O(n) 
  reverseLinkedListRecursive(): O(n)

Space Complexity:
  reverseLinkedListIterative(): O(1)      
  reverseLinkedListStack(): O(n) 
  reverseLinkedListRecursive(): O(n)     
      

'''
