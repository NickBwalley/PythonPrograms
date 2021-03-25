"""
Python File Write
Write to an Existing File
To write to an existing file, you must add a parameter to the open() function:

"a" - Append - will append to the end of the file

"w" - Write - will overwrite any existing content
"""

# Example
# Open the file "demofile2.txt" and append content to the file:
f = open("demofile2.txt", "a")
f.write("Hello World!\nThis is Nick!\nI am a Programmer!")
f.close()
# open and read the file after appending
f = open("demofile2.txt", "r")
print(f.read())