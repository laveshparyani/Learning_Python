# Single-Line Comments:
# This is an example of a single-line comment
print("Hey, I am Lavesh!")

# Print statement with newline character
print("Hey, I am Lavesh!\nWho are you")  # This is an example of newline character "\n"

# Multi-line Comments using triple double-quotes
"""
This is an example of a multi-line comment.
Below is an if-else statement to check if a variable is greater than 5.
"""

p = 7
if p > 5:
    print("p is greater than 5.")
else:
    print("p is not greater than 5.")

# End of if-else statement.
# Multi-line Comments using triple single-quotes
''' 
This is another example of a multi-line comment.
It can be used interchangeably with triple double-quotes.
'''

# Example of Escape Sequence character
# The below line will cause a syntax error:
# print("This will not "execute"")
print("This will \"execute\", as here escape sequence character is used.")

# Additional concepts from the tutorial
# Using escape sequences for newlines and tabs
print("Hello, World!\nWelcome to Python programming.")  # Newline character
print("Hello,\tWorld!")  # Tab character

# More on the print statement
# The syntax of a print statement includes various parameters:
# print(object(s), sep=separator, end=end, file=file, flush=flush)

# Example with different parameters
print("Hello", "World", sep=", ", end="!")  # Using sep and end parameters
print(" This is the next sentence.")

# Using the 'file' parameter to write to a file instead of standard output
with open("output.txt", "w") as file:
    print("This will be written to the file.", file=file)

# Demonstrating how comments can be used to explain code
# Author: Lavesh
# Course: 100 Days Of Code
# Day: 5

# Commenting multiple lines at once using a shortcut (Ctrl + / or Command + /)
# Uncommenting the below lines will print "Hello World" multiple times
# print("Hello World")
# print("Hello World")
# print("Hello World")