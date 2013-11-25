"""
Scrpting MT2012 Week 02

Week 2: Debugging exercise 2. Debugging file operations

Each one of these exercises requires you to alter the code in some way. 
If the code works properly then it will run up until that point and then stop.
"""

__author__ =  'Bernie Hogan'
__version__=  '1.0'

import os, glob

#1. Open a file and write to it. 
# Note, some errors happen at compile time, some happen at runtime.

fileout = open("newfile.txt", 'r') 
fileout.write("Would you be my neighbor?\n")
fileout.close()

#2. Open a file and print its contents

filein = open("newfile.txt", 'w') 

for i in filein
	print i

# #3. Open the same file as above and *append* the line below. 
# Note, sometimes you don't notice the error at first. Check the file. 

fileout = open("newfile.txt", 'w') 
fileout.write("Most certianly, good sir.\n")
fileout.close()
 

# 4. Create a new directory below the current one and place a file in there
# Note, pay attention to what file was created and where
# Note, some bugs may be os-specific.

newfolder = "tempfolder:2"
 
try: 
	os.mkdir(newfolder) #mk means "make"
except: 
	print "didn't happen"

fileout = open(newfolder + "newfile.txt",'w')

print os.getcwd()
fileout.write("am I in the right folder?\n")
fileout.close()

fileout = open(newfolder + os.sep + "newfile.txt",'r')
print fileout.read()

#5. Now delete the directory and the file
# Note, now you have to search for a command...
filestodelete = glob.glob(newfolder + os.sep + "*")
for i in filestodelete:
	os.delete(i)
os.rmdir(newfolder) #rm means remove

