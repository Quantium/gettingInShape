#!/usr/bin/python3
class Node:
    def __init__(self,data):
        self.data = data;
        self.next = None
        self.prev = None

class DLinkedList:
    def __init__(self):
        self.head=None

    def listprint(self):
        printval = self.head
        while printval is not None:
            print(printval.data)
            printval=printval.next

    def atBegining(self,newdata):
        newNode = Node(newdata)
        newNode.next = self.head
        if self.head is not None:
            self.head.prev = newNode
        self.head=newNode

    def inBetween(self,middle_node,newdata):
        if middle_node is None:
            print("There is no such middle node")
            return
        newNode=Node(newdata)
        newNode.next = middle_node.next
        newNode.prev = middle_node
        middle_node.prev = newNode
        
    def atEnd(self,newdata):
        newNode=Node(newdata)
        if self.head is None:
            self.head = newNode
            return
        lastNode = self.head
        while lastNode.next:
            lastNode=lastNode.next
        lastNode.next=newNode
        newNode.prev = lastNode

    def removeNode(self,removekey):
        head=self.head
        if head.data is not None:
            if head.data == removekey:
                self.head = head.next
                self.head.prev = None
                head=None
                return
        prev=None
        while head is not None:
            if head.data == removekey:
                break
            prev = head
            head = head.next
        if head == None:
            return
        prev.next = head.next
        head.prev = prev
        head=None

list = DLinkedList()

list.head = Node('Feb')

list.atEnd('Mar')

list.atBegining('Jan')

list.atEnd('Apr')

list.listprint()
