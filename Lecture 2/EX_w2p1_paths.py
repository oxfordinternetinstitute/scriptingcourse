"""
DSR HT2012 Week 02

Week 2: Example 1: Navigating the path

The path is the way you find a file on a computer or in cyberspace. 
In order to manipulate files we need to know where they are! We will use the 
os and glob modules to search for files.
"""

__author__ =  'Bernie Hogan'
__version__=  '1.0'

import os
import glob

def prints(string):
	print string
	return string

def printFileExists(pathy):
	print "The path to \"%s\" exists now? \t %s" % (pathy, os.path.exists(pathy) )
	return os.path.exists(pathy)

lb = "\n-----------------\n"

# What is my current directory? 
print lb
print "\"getcwd()\", or 'get current working directory' prints the current directory:"
print os.getcwd()

PATH = "\users\effect\Documents"
PATH.replace("\"",os.sep)

# Find out if a path exists
print lb
newfolder = "tempfiles"
print "We are going to first ask if the file \"%s\" exists\n" % newfolder

printFileExists(newfolder)


# Make a new directory in the current directory
# And the remove it. Note, you can only delete empty folders with this command.
print lb

print "Making the folder \"%s\"" % newfolder

try: 
	os.mkdir(newfolder) #mk means "make"
except OSError:
	pass
	
printFileExists(newfolder)


print "Removing the folder \"%s\"" % newfolder

try:
	os.rmdir(newfolder) #rm means "remove"
except OSError: 
	pass

printFileExists(newfolder)

# List all of the files in the current folder
print lb + "Here is a list of files in this directory:"

filelist = os.listdir(os.getcwd())

[prints(i) for i in filelist]

# Find all the python files in this directory.
print lb + '''Below we use the 'glob' module
(The * means every alphanumeric character except \\ or / :)'''

print os.getcwd()
filelist = glob.glob("%s%s*.py" % (os.getcwd(),os.sep))

[prints(i) for i in filelist]

print lb + "But if we want just the names, we use \"os.path.basename()\""
[prints(os.path.basename(i)) for i in filelist]