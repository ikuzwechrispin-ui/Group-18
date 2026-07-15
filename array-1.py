#!/usr/bin/env python3

print# Time Complexity:
# Read: O(1)
# Update: O(1)
# Traverse: O(n)
# Find Maximum: O(n)
# Insert: O(n)

marks = [75, 82, 68, 90, 77, None]
size = 5

print("Original Array:", marks[:size])

index = int(input("Enter index to read: "))
if 0 <= index < size:
    print("Value:", marks[index])
else:
    print("Invalid index")

index = int(input("Enter index to update: "))
if 0 <= index < size:
    value = int(input("Enter new value: "))
    marks[index] = value
    print("After update:", marks[:size])
else:
    print("Invalid index")

print("Array values:")
for i in range(size):
    print(marks[i])

maximum = marks[0]
for i in range(1, size):
    if marks[i] > maximum:
        maximum = marks[i]

print("Maximum value:", maximum)

print("Before insertion:", marks[:size])

index = int(input("Enter index to insert: "))
value = int(input("Enter value to insert: "))

if 0 <= index <= size:
    for i in range(size, index, -1):
        marks[i] = marks[i - 1]
    marks[index] = value
    size += 1
    print("After insertion:", marks[:size])
else:
    print("Invalid index")