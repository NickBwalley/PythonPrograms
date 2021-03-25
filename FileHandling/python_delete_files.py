
# lets create a demofile.txt and add some content inside of it
f = open("demofile4.txt", "a")
f.write("This is just a test file!\n")


"""
Python Delete File
Delete a File
To delete a file, you must import the OS module, and run its os.remove() function:
"""
# Example
# Remove the file "demofile4.txt":
import os
os.remove("demofile4.txt")


# Check if File exist:
# To avoid getting an error, you might want to check if the file exists before you try to delete it:
# Check if file exists, then delete it:
import os
if os.path.exists("demofile4.txt"):
  os.remove("demofile4.txt")
else:
  print("The file does not exist")


# Delete Folder
# To delete an entire folder, use the os.rmdir() method:
# Remove the folder "myfolder":

# import os
# os.rmdir("myfolder")

# Note: You can only remove empty folders.


