"""
Week 1: Debugging exercise 1. Debugging String Operations 

Each one of these exercises requires you to alter the code in some way. 
If the code works properly then it will run up until that point and then stop.
"""

__author__ =  'Bernie Hogan'
__version__=  '1.0'

#1. Import string module
import string

#2. Print a string
print 'Here is a string'

#3. Use escape quotes
print "You can put quotes in side quotes using the \" character"

#4. Print a new line
print "Here is a new line \n ^ Above here!"

#5. Print doublequotes inside a string...using escapes 
print 'You can "doublequote" in a string'
print "And 'singlequote' in a string"
print "But you can't \"doublequote\" in a double quote string."

#6. Print three list elements
print "here is a list:"
strlist = ["yes","no","maybe"]

for i in strlist: print i

#7. Join a list into a string 

print string.join(["Cheez","burger"])

#8. Print a string to upper case
print string.upper("yes, no")

#9. Print characters in a string by index
strvar = "String variable #1"

print strvar[0]
print strvar[-1]
print strvar[16]

#10. Printing values inside strings (note there are several ways to fix this one)
digit = 42
print "The number %d is the answer to life, the universe, and everything." % digit

print "Hooray, you finished. You win!"