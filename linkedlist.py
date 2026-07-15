#!/usr/bin/env python3

print# 4_linkedlist.py

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def insert_head(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def insert_tail(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = node

    def delete(self, value):

        if self.head is None:
            return

        if self.head.data == value:
            self.head = self.head.next
            return

        current = self.head

        while current.next:

            if current.next.data == value:
                current.next = current.next.next
                return

            current = current.next

    def display(self):

        current = self.head

        while current:
            print(current.data, end=" -> ")
            current = current.next

        print("None")


ll = LinkedList()

ll.insert_head(20)
ll.insert_head(10)
ll.insert_tail(30)
ll.insert_tail(40)

print("Linked List:")
ll.display()

ll.delete(30)

print("After deleting 30:")
ll.display()

# Time Complexity
# Insert at Head = O(1)
# Insert at Tail = O(n)
# Delete = O(n)
# Traverse = O(n)