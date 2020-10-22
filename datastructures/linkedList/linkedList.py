#!/usr/bin/python3
class Node:
    def __init__(self, dataval=None):
        self.data = dataval
        self.next = None

class SLinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (printval.data)
            printval = printval.next
    def AtBegining(self,newdata):
        NewNode = Node(newdata)
        NewNode.next = self.headval
        self.headval = NewNode

    def Inbetween(self,middle_node,newdata):
        if middle_node is None:
            print("There is no such middle node")
            return

        NewNode = Node(newdata)
        NewNode.next = middle_node.next
        middle_node.nextval = NewNode

    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        laste = self.headval
        while(laste.next):
            laste = laste.next
        laste.next=NewNode

    def RemoveNode(self, Removekey):
        HeadVal = self.headval
        if (HeadVal is not None):
            if (HeadVal.data == Removekey):
                self.headval = HeadVal.next
                HeadVal = None
                return
        prev=None
        while (HeadVal is not None):
            if HeadVal.data == Removekey:
                break
            prev = HeadVal
            HeadVal = HeadVal.next
        if (HeadVal == None):
            return
        prev.next = HeadVal.next
        HeadVal = None

list = SLinkedList()
list.headval = Node("Mon")
e2 = Node("Wed")
e3 = Node("Thu")

list.headval.next = e2
e2.next = e3

list.AtBegining("Sun")

list.AtEnd('Fri')

list.Inbetween(list.headval.next,"Tue")

list.Inbetween(list.headval.next,"Chimino")

list.RemoveNode("Chimino")

list.listprint()