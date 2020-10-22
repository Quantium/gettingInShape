#!/usr/bin/python3
"""
LIFO
"""
class Stack:
    def __init__(self):
        self.stack=[]
    
    def add(self,data):
        if data not in self.stack:
            self.stack.append(data)
            return True
        else:
            return False
    
    def remove(self):
        if len(self.stack) <= 0:
            print('The stack is empty')
            return False
        else:
            return self.stack.pop()
    
    def peek(self):
        return self.stack[-1]
    
aStack = Stack()
aStack.add('Mon')
aStack.add('Tue')
aStack.add('Wed')
aStack.add('Thu')
aStack.add('Fri')
aStack.add('Sat')
aStack.add('Sun')
print(aStack.remove())
aStack.remove()
aStack.remove()
print(aStack.peek())