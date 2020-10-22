#!/usr/bin/python3
class Node:
    def __init__(self, dataval=None):
        self.data = dataval
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None

    def listprint(self):
        printval = self.head
        while printval is not None:
            print (printval.data)
            printval = printval.next
    def atBegining(self,newdata):
        NewNode = Node(newdata)
        NewNode.next = self.head
        self.head = NewNode

    def inBetween(self,middle_node,newdata):
        if middle_node is None:
            print("There is no such middle node")
            return

        NewNode = Node(newdata)
        NewNode.next = middle_node.next
        middle_node.next = NewNode

    def atEnd(self, newdata):
        NewNode = Node(newdata)
        if self.head is None:
            self.head = NewNode
            return
        laste = self.head
        while(laste.next):
            laste = laste.next
        laste.next=NewNode

    def removeNode(self, removekey):
        HeadVal = self.head
        if (HeadVal is not None):
            if (HeadVal.data == removekey):
                self.head = HeadVal.next
                HeadVal = None
                return
        prev=None
        while (HeadVal is not None):
            if HeadVal.data == removekey:
                break
            prev = HeadVal
            HeadVal = HeadVal.next
        if (HeadVal == None):
            return
        prev.next = HeadVal.next
        HeadVal = None

list = SLinkedList()
list.head = Node("Mon")
e2 = Node("Wed")
e3 = Node("Thu")

list.head.next = e2
e2.next = e3

list.atBegining("Sun")

list.atEnd('Fri')

list.inBetween(list.head.next,"Tue")

list.inBetween(list.head.next,"Chimino")

list.removeNode("Chimino")

list.listprint()