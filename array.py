#!/usr/bin/env python3

print# 1_arrays.py

# Store student marks in an array
marks = [70, 85, 60, 90, 75]

print("Original Array:", marks)

# Read a value at a given index
index = 2
print("Value at index", index, "is", marks[index])

# Update a value at a given index
marks[index] = 95
print("Array after updating:", marks)

# Traverse and print all values
print("\nTraversing the array:")
for mark in marks:
    print(mark)

# Find the maximum value
maximum = marks[0]
for mark in marks:
    if mark > maximum:
        maximum = mark

print("\nMaximum value:", maximum)

# Insert a value at a given index without using insert()
insert_value = 88
insert_index = 3

print("\nBefore insertion:", marks)

# Increase array size
marks.append(0)

# Shift elements to the right
for i in range(len(marks) - 1, insert_index, -1):
    marks[i] = marks[i - 1]

# Insert the new value
marks[insert_index] = insert_value

print("After insertion:", marks)

# Time Complexity
# Read = O(1)
# Update = O(1)
# Traverse = O(n)
# Find Maximum = O(n)
# Insert = O(n)