"""
Scripting MT2012 Week 02

Week 2: Example 2: File Manipulation

Files are streams of bytes that can be read, written or appended.
"""

__author__ =  'Bernie Hogan'
__version__=  '1.1'

# Files are opened as objects that we can interact with. 
# The method asks for a filename and whether its read, write or append

fileout = open("newfile.txt",'w')

outstr = "Hello, computer. I am being written to you as we speak.\n"

fileout.write(outstr)

# fileout.flush()

fileout.close()


# Now we can read the file. 
# We are going to do this in a method 
#
# When you open a file you create a file object. 
# This is not the contents of the file, but a pointer to it. 
# In order to read the file you need to use the read() method.

def printContents(pathy):
	filein = open(pathy)
	instr = filein.read()
	print instr
	filein.close()
	
printContents("newfile.txt")
	

# You can append values to the end of a file:
filein = open("newfile.txt",'a')

filein.write("Its a beautiful day in who's neighborhood?\n")

filein.close()

printContents("newfile.txt")

filein = open("newfile.txt",'r')

x = []
for i in filein:
	x.append(i)

print x