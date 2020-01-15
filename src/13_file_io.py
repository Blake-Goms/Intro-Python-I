"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE
f = open(r"C:\Users\Blake\Desktop\Web20Git\CS\Week1\Intro-Python-I\src\foo.txt", 'r')
print(f.read())
f.close()

# or, with will automatically close the file once it's done.
with open(r"C:\Users\Blake\Desktop\Web20Git\CS\Week1\Intro-Python-I\src\foo.txt", 'r') as f:
    for line in f:
        print(line, end='')

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
bar = open(
    r"C:\Users\Blake\Desktop\Web20Git\CS\Week1\Intro-Python-I\src\bar.txt", "w")
bar.write("This is the first line")
bar.write("\n This is the second line")
bar.write("\n This is the third line")
bar.close()

h = open(r"C:\Users\Blake\Desktop\Web20Git\CS\Week1\Intro-Python-I\src\bar.txt", "r")
print(h.read())
h.close()
