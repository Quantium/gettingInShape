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
        
    def find(self,data):
        if data < self.data:
            #Search on the left
            if self.left is None:
                return None
            else:
                return self.left.find(data)
        elif data > self.data:
            #Search on the right
            if self.right is None:
                return None
            else:
                return self.right.find(data)
        return data
            
    
    def printTree(self,order='in'):
        res=[]
        if order=='in':
            # in-order transversal
            if self.left: self.left.printTree(order=order)
            print(self.data,sep=" ")
            res.append(self.data)
            if self.right: self.right.printTree(order=order)

        elif order=='pre':
            # pre-order transversal
            print(self.data,sep=" ")
            if self.left: self.left.printTree()
            if self.right: self.right.printTree(order=order)
            
        elif order=='post':
            # post-order transversal
            if self.left: self.left.printTree()
            if self.right: self.right.printTree(order=order)
            print(self.data,sep=" ")

tree=TreeNode(45)
tree.insert(23)
tree.insert(65)
tree.insert(128)
tree.insert(12)
tree.insert(34)
tree.insert(92)
tree.insert(6)
tree.insert(48)
tree.insert(71)
tree.printTree()
print('-')
tree.printTree(order='post')
print('-')
tree.printTree(order='pre')
print('--')

print("find 34::",tree.find(34))
print("find 50::",tree.find(50))