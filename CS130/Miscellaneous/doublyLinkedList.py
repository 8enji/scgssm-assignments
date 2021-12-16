
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class LinkedList:

    def __init__(self):
        self.head = None
    # def printList(self):
    #     temp = self.head
    #     while (temp):
    #         print(temp.data)
    #         temp = temp.next



doubleLinkedList = LinkedList()

doubleLinkedList.head = Node(1)
second = Node(2)
third = Node(3)

doubleLinkedList.head.next = second

second.previous = doubleLinkedList.head
second.next = third

third.previous = second

word = doubleLinkedList.head

newNode = Node('New')
newNode.previous = doubleLinkedList.head
newNode.next = doubleLinkedList.head.next
doubleLinkedList.head.next = newNode
newNode.next.previous = newNode

while(word):
    print(word.data)
    word = word.next