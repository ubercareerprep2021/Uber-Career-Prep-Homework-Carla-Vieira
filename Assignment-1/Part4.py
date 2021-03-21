from math import ceil

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, node: Node):
        if not self.head: self.head = node
        else:
            mark = self.cycleMark()
            pointer = self.head
            is_first_time = True
            while pointer.next:
                if pointer.next == mark:
                    if is_first_time:
                        is_first_time = False
                    else:
                        break
                pointer = pointer.next
            pointer.next = node
        self.size += 1

    def pop(self):
        if not self.head: raise Exception("Empty Linked List")
        mark = self.cycleMark()
        pointer = self.head
        is_first_time = True if self.hasCycle() else False
        if pointer.next == mark:
            if is_first_time:
                is_first_time = False
                previous_node = pointer
                pointer = pointer.next
            else:
                delete_node = self.head
                self.head = None
                self.size -= 1
                return delete_node
        while pointer:
            if pointer.next == mark:
                if is_first_time:
                    is_first_time = False
                else:
                    break
            previous_node = pointer
            pointer = pointer.next
        delete_node = pointer
        previous_node.next = mark if mark != delete_node else None
        if delete_node == self.head: self.head = None
        self.size -= 1
        return delete_node


    def insert(self, index: int, node: Node):
        if index >= self.sizeN() or index < 0: return
        pointer = self.head
        for x in range(index-1):
            pointer = pointer.next
        node.next = pointer.next
        pointer.next = node
        self.size += 1

    def remove(self, index: int):
        if index >= self.sizeN() or index < 0: return
        pointer = self.head
        if index == 0:
            self.head = self.head.next
        else:
            for x in range(index):
                previous_node = pointer
                pointer = pointer.next
            if self.hasCycle():
                if pointer == self.cycleMark():
                    self.removeCycle()
            previous_node.next = pointer.next
        self.size -= 1

    def elementAt(self, index: int):
        if index >= self.sizeN() or index < 0: return None
        pointer = self.head
        for x in range(index):
            pointer = pointer.next
        return pointer

    def sizeN(self):
        if not self.head: return 0
        counter = 0
        mark = self.cycleMark()
        pointer = self.head
        is_first_time = True
        while pointer:
            if pointer == mark:
                if is_first_time:
                    is_first_time = False
                else:
                    break
            counter += 1
            pointer = pointer.next
        return counter

    def size1(self):
        return self.size

    def printList(self):
        print("[ ", end="")
        if self.sizeN() == 0:
            print("]")
            return
        mark = self.cycleMark()
        pointer = self.head
        is_first_time = True
        while pointer:
            if pointer == mark:
                if is_first_time:
                    is_first_time = False
                else:
                    break
            print(pointer.value, end=" -> ")
            pointer = pointer.next
        print(pointer.value if pointer else None, end="")
        print(" ]")

    def hasCycle(self):
        if not self.head: raise Exception("Empty Linked List")
        set_nodes = set()
        pointer = self.head
        while pointer:
            if pointer in set_nodes:
                return True
            set_nodes.add(pointer)
            pointer = pointer.next
        return False

    def cycleMark(self):
        if not self.head: raise Exception("Empty Linked List")
        set_nodes = set()
        pointer = self.head
        while pointer:
            if pointer in set_nodes:
                return pointer
            set_nodes.add(pointer)
            pointer = pointer.next
        return None

    def isPalindrome(self):
        mark = self.cycleMark()
        pointer = self.head
        list_values = []
        is_first_time = True
        while pointer:
            if pointer == mark:
                if is_first_time:
                    is_first_time = False
                else:
                    break
            list_values.append(pointer.value)
            pointer = pointer.next
        return list_values[:len(list_values)//2] == list_values[len(list_values):ceil(len(list_values)/2)-1:-1]

    def removeCycle(self):
        mark = self.cycleMark()
        pointer = self.head
        is_first_time = True
        while pointer.next:
            if pointer.next == mark:
                if is_first_time:
                    is_first_time = False
                else:
                    break
            pointer = pointer.next
        pointer.next = None

'''                 
Complexity analysis:
  push(): O(n)      
  pop(): O(n)       
  insert(): O(n)       
  remove(): O(n)   
  elementAt(): O(n)     
  sizeN(): O(n)     
  size1(): O(1)   obs: size1() can be used if it will be add just Nodes without other nodes chained
  printList(): O(n)      
  hasCycle(): O(n)       
  cycleMark(): O(n)       
  isPalindrome(): O(n)   
  removeCycle(): O(n)  
'''
