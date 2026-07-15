#!/usr/bin/env python3

print# 3_queue.py

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if len(self.items) == 0:
            return None
        return self.items.pop(0)

    def peek(self):
        if len(self.items) == 0:
            return None
        return self.items[0]

    def display(self):
        print(self.items)


q = Queue()

print("Enqueue 10")
q.enqueue(10)
q.display()

print("Enqueue 20")
q.enqueue(20)
q.display()

print("Enqueue 30")
q.enqueue(30)
q.display()

print("Front element:", q.peek())

print("Dequeue:", q.dequeue())
q.display()

print("Front element:", q.peek())

# Time Complexity
# Enqueue = O(1)
# Dequeue = O(n)
# Peek = O(1)