"""
Python is a strongly-typed language under the hood, which means
that the types of values matter, especially when we're trying
to perform operations on them.

Note that if you try running the following code without making any
changes, you'll get a TypeError saying you can't perform an operation
on a string and an integer.
"""

x = 5
y = "7"

# Write a print statement that combines x + y into the integer value 12

# YOUR CODE HERE
# this is explicit type casting
print(x + int(y))

''' different way of doing it
y = int(y)
sum = x + y
print(sum)
'''
# Write a print statement that combines x + y into the string value 57

# YOUR CODE HERE
print(str(x) + y)
