#!/usr/bin/python3
class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right= None

    def insert(self,data):
        if self.data:
            if data < self.data:
                #insert left
                if self.left:
                    self.left.insert(data)
                else:
                    self.left = TreeNode(data)
            elif data > self.data:
                #insert right
                if self.right:
                    self.right.insert(data)
                else:
                    self.right=TreeNode(data)
        else:
            self.data=data
    
    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data,sep=" ")
        if self.right:
            self.right.printTree()

tree=TreeNode(45)
tree.printTree()
print('--')

tree.insert(23)
tree.printTree()
print('--')

tree.insert(65)
tree.insert(128)
tree.insert(12)
tree.insert(34)
tree.insert(92)
tree.insert(6)
tree.insert(48)
tree.insert(71)
tree.printTree()
print('--')