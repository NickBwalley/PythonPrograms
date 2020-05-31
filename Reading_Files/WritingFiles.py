'''
WARNING!...
The 'w' will override the whole text and insert the newly appended text inside
The 'a' is the appropriate as it adds the file at the end of your text lines
NOTE!...
When you are using the 'w' it can also create a new file that is if it is not there
'''
employee_file = open("Scurry.html", "w")
employee_file.write("<p>This is NickBwalley the Greatest and Coolest programmer</p>")#adding an item inside the writingFiles


employee_file.close()