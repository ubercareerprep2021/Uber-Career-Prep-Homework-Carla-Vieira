from Part2 import *
from Part3 import *
from Part4 import *
from Part5 import *
import unittest

class TestPart2(unittest.TestCase):

    def test_isStringPermutation(self):
        self.assertTrue(isStringPermutation('asdf', 'fsda'))
        self.assertFalse(isStringPermutation('asdf', 'fsa'))
        self.assertFalse(isStringPermutation('asdf', 'fsax'))

    def test_pairsThatEqualSum(self):
        self.assertEqual(pairsThatEqualSum([1, 2, 3, 4, 5], 5), [(2, 3), (1, 4)])
        self.assertEqual(pairsThatEqualSum([1, 2, 3, 4, 5], 1), [])
        self.assertEqual(pairsThatEqualSum([1, 2, 3, 4, 5], 7), [(3, 4), (2, 5)])

class TestPart3(unittest.TestCase):

    def test_Stack(self):
        myStack = Stack()
        myStack.push(42)
        self.assertEqual(myStack.top(), 42)
        self.assertEqual(myStack.size1(), 1)
        self.assertFalse(myStack.isEmpty())
        popped_value = myStack.pop()
        self.assertEqual(popped_value, 42)
        self.assertEqual(myStack.size1(), 0)
        self.assertTrue(myStack.isEmpty(), True)
        myStack.push(42)
        self.assertRaises(TypeError, myStack.push, "carla")
        myStack.pop()
        myStack.push("carla")
        myStack.push("maria")
        self.assertEqual(myStack.size1(), 2)
        self.assertEqual(myStack.top(), "maria")

    def test_StackMin(self):
        myStack = Stack()
        myStack.push(5)
        myStack.push(3)
        self.assertEqual(myStack.min(), 3)
        myStack.push(1)
        self.assertEqual(myStack.min(), 1)

    def test_StackRemoveMin(self):
        myStack = Stack()
        myStack.push(7)
        myStack.push(5)
        myStack.push(3)
        self.assertEqual(myStack.min(), 3)
        myStack.pop()
        self.assertEqual(myStack.min(), 5)

    def test_Queue(self):
        myQueue = Queue()
        myQueue.enqueue(1)
        myQueue.enqueue(2)
        myQueue.enqueue(3)
        self.assertEqual(myQueue.size1(), 3)
        self.assertEqual(myQueue.front(), 1)
        self.assertEqual(myQueue.rear(), 3)
        dequeuedItem = myQueue.dequeue()
        self.assertEqual(dequeuedItem, 1)
        self.assertEqual(myQueue.size1(), 2)
        myQueue.enqueue("carla")
        self.assertEqual(myQueue.rear(), "carla")

class TestPart4(unittest.TestCase):

    def testPushBackAddsOneNode(self):
        myLList = SinglyLinkedList()
        myLList.push(Node(1))
        self.assertEqual(myLList.sizeN(), 1)
        myLList.push(Node(2))
        self.assertEqual(myLList.sizeN(), 2)
        myLList.push(Node(3, myLList.head))
        self.assertEqual(myLList.sizeN(), 3)
        myLList.push(Node(4))
        self.assertEqual(myLList.sizeN(), 4)

    def testPopBackRemovesCorrectNode(self):
        myLList = SinglyLinkedList()
        node1 = Node(1)
        node2 = Node(2)
        myLList.push(node1)
        myLList.push(node2)
        self.assertEqual(myLList.pop(), node2)
        self.assertEqual(myLList.pop(), node1)
        myLList.push(node1)
        myLList.push(node2)
        node3 = Node(3, myLList.head.next)
        myLList.push(node3)
        self.assertEqual(myLList.pop(), node3)
        self.assertEqual(myLList.pop(), node2)
        self.assertEqual(myLList.pop(), node1)
        node1.next = node1
        myLList.push(node1)
        self.assertEqual(myLList.pop(), node1)
        self.assertEqual(myLList.sizeN(), 0)

    def testEraseRemovesCorrectNode(self):
        myLList = SinglyLinkedList()
        node0 = Node(0)
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        myLList.push(node0)
        myLList.push(node1)
        myLList.push(node2)
        myLList.push(node3)
        myLList.remove(2)
        self.assertEqual(myLList.elementAt(2), node3)
        node2.next = node3
        myLList.push(node2)
        self.assertEqual(myLList.elementAt(2), node3)
        myLList.remove(2)
        self.assertEqual(myLList.elementAt(2), node2)

    def testEraseDoesNothingIfNoNode(self):
        myLList = SinglyLinkedList()
        node0 = Node(0)
        node1 = Node(1)
        node2 = Node(2)
        myLList.push(node0)
        myLList.push(node1)
        myLList.push(node2)
        myLList.remove(3)
        myLList.remove(4)
        myLList.remove(-1)
        self.assertEqual(myLList.elementAt(0), node0)
        self.assertEqual(myLList.elementAt(1), node1)
        self.assertEqual(myLList.elementAt(2), node2)
        self.assertFalse(myLList.elementAt(3))

    def testElementAtReturnNode(self):
        myLList = SinglyLinkedList()
        node0 = Node(0)
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3, node1)
        myLList.push(node0)
        myLList.push(node1)
        myLList.push(node2)
        myLList.push(node3)
        self.assertEqual(myLList.elementAt(0), node0)
        self.assertEqual(myLList.elementAt(1), node1)
        self.assertEqual(myLList.elementAt(2), node2)
        self.assertEqual(myLList.elementAt(3), node3)

    def testElementAtReturnsNoNodeIfIndexDoesNotExist(self):
        myLList = SinglyLinkedList()
        node0 = Node(0)
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3, node1)
        myLList.push(node0)
        myLList.push(node1)
        myLList.push(node2)
        myLList.push(node3)
        self.assertEqual(myLList.elementAt(0), node0)
        self.assertEqual(myLList.elementAt(1), node1)
        self.assertEqual(myLList.elementAt(2), node2)
        self.assertEqual(myLList.elementAt(3), node3)
        self.assertFalse(myLList.elementAt(4))
        self.assertFalse(myLList.elementAt(-1))
        self.assertFalse(myLList.elementAt(5))

    def testSizeReturnsCorrectSize(self):
        myLList = SinglyLinkedList()
        node0 = Node(0)
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3, node1)
        self.assertEqual(myLList.size1(), 0)
        self.assertEqual(myLList.sizeN(), 0)
        myLList.push(node0)
        self.assertEqual(myLList.size1(), 1)
        self.assertEqual(myLList.sizeN(), 1)
        myLList.push(node1)
        self.assertEqual(myLList.size1(), 2)
        self.assertEqual(myLList.sizeN(), 2)
        myLList.push(node2)
        self.assertEqual(myLList.size1(), 3)
        self.assertEqual(myLList.sizeN(), 3)
        myLList.push(node3)
        self.assertEqual(myLList.size1(), 4)
        self.assertEqual(myLList.sizeN(), 4)
        myLList.remove(2)
        self.assertEqual(myLList.size1(), 3)
        self.assertEqual(myLList.sizeN(), 3)
        myLList.pop()
        self.assertEqual(myLList.size1(), 2)
        self.assertEqual(myLList.sizeN(), 2)

    def testSizeReturnsCorrectSizeNodesChained(self):
        myLList = SinglyLinkedList()
        node0 = Node(0)
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node2.next = node3
        myLList.push(node0)
        myLList.push(node1)
        myLList.push(node2)
        self.assertEqual(myLList.sizeN(), 4)


    def testIdentifyCycle(self):
        myLList = SinglyLinkedList()
        node0 = Node(0)
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3, node1)
        node4 = Node(4)
        node4.next = node4
        myLList.push(node0)
        myLList.push(node1)
        myLList.push(node2)
        self.assertFalse(myLList.hasCycle())
        myLList.push(node3)
        self.assertTrue(myLList.hasCycle())
        myLList.remove(1)
        self.assertFalse(myLList.hasCycle())
        myLList.push(node4)
        self.assertTrue(myLList.hasCycle())
        myLList.pop()
        self.assertFalse(myLList.hasCycle())

    def testIdentifySingleCycle(self):
        myLList = SinglyLinkedList()
        node0 = Node(0)
        node0.next = node0
        myLList.push(node0)
        self.assertTrue(myLList.hasCycle())

    def testIdentifyCycleEmptyList(self):
        myLList = SinglyLinkedList()
        self.assertRaises(Exception, myLList.hasCycle)

    def testIsPalindromeEven(self):
        chars = "abba"
        myLList = SinglyLinkedList()
        for char in chars:
            myLList.push(Node(char))
        self.assertTrue(myLList.isPalindrome())

    def testIsPalindromeOdd(self):
        chars = "abcba"
        myLList = SinglyLinkedList()
        for char in chars:
            myLList.push(Node(char))
        self.assertTrue(myLList.isPalindrome())

    def testIsNotPalindromeEven(self):
        chars = "abab"
        myLList = SinglyLinkedList()
        for char in chars:
            myLList.push(Node(char))
        self.assertFalse(myLList.isPalindrome())

    def testIsNotPalindromeOdd(self):
        chars = "abcab"
        myLList = SinglyLinkedList()
        for char in chars:
            myLList.push(Node(char))
        self.assertFalse(myLList.isPalindrome())

class TestPart5(unittest.TestCase):

    def testReversedLinkedList(self):
        chars = "abcdef"
        myLList = SinglyLinkedList()
        myRLList = SinglyLinkedList()

        for char in chars:
            myLList.push(Node(char))
        for char in chars[::-1]:
            myRLList.push(Node(char))

        lListStack = reverseLinkedListStack(myLList)
        lListRecursive = reverseLinkedListRecursive(myLList)
        lListIterative = reverseLinkedListIterative(myLList)

        pointerRLL = myRLList.head
        pointerLLI = lListIterative.head
        pointerLLS = lListStack.head
        pointerLLR = lListRecursive.head

        while pointerRLL:
            self.assertEqual(pointerRLL.value, pointerLLI.value)
            self.assertEqual(pointerRLL.value, pointerLLS.value)
            self.assertEqual(pointerRLL.value, pointerLLR.value)
            pointerRLL = pointerRLL.next
            pointerLLI = pointerLLI.next
            pointerLLS = pointerLLS.next
            pointerLLR = pointerLLR.next

if __name__ == '__main__':
    unittest.main()
