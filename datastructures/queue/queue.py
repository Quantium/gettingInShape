#!/usr/bin/python3
"""
FIFO
"""
class Queue:
    def __init__(self):
        self.queue=list()
    
    def enqueue(self,data):
        if data not in self.queue:
            self.queue.insert(0,data)
            return True
        return False
    
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop()
        return None
    
    def size(self):
        return len(self.queue)

aQueue = Queue()
aQueue.enqueue("Andrés")
aQueue.enqueue("Andy")
aQueue.enqueue("Quantium")
aQueue.enqueue("Qython")
aQueue.enqueue("Chimi")
print(aQueue.size())
print("first element out",aQueue.dequeue())
print("first element out",aQueue.dequeue())
print("first element out",aQueue.dequeue())

