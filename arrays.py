#!/usr/bin/env python3

print# Question 1: Arrays
# Time Complexity: Traversal O(n), Maximum O(n), Insertion O(n)

marks = [75, 82, 90, 68, 88]

print("Original array:")
print(marks)

# Read value at index
index = 2
print("Value at index", index, "is:", marks[index])


# Update value at index
update_index = 3
marks[update_index] = 95

print("Array after updating index", update_index)
print(marks)


# Traverse and print all values
print("All student marks:")
for mark in marks:
    print(mark)


# Find maximum value
maximum = marks[0]

for mark in marks:
    if mark > maximum:
        maximum = mark

print("Maximum mark:", maximum)


# Insert value at given index without using insert()
insert_index = 2
new_value = 85

# Add empty space
marks.append(0)

# Shift elements to the right
for i in range(len(marks)-1, insert_index, -1):
    marks[i] = marks[i-1]

# Place new value
marks[insert_index] = new_value

print("Array after insertion:")
print(marks)