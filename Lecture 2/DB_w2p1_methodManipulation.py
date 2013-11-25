"""
Week 2: Debugging exercise 1. Debugging Method Operations

Each one of these exercises requires you to alter the code in some way. 
If the code works properly then it will run up until that point and then stop.

Each exercise should require only one kind of change/alteration.
"""

__author__ =  'Bernie Hogan'
__version__=  '1.0'

import random
word = random.choice(["dawg","mister","dude","mate"])

# - - - - - - - - - - - #
# 1. Calling a method
# Note: Where is the printing done?

shoutOut1(word)

def shoutOut1 (str1):	
	print "Yo %s!" % str1
	

# 2. Dealing with bad input (2 errors here)
# Should print "Yo [word]!"
# Note: exceptions are called when something doesn't work right.

def shoutOut2(str1=word):
	try: 
		print "Yo %s!" % str1
	except:
		print "Exceptional %s!" % int(str1)

shoutOut2(str1)

# 3. Input / Output 
# Should print "You shall not pass, [word]"
# Note: What gets returned?
def shoutOut3(str1=word):
	try: 
		tempVar = str(str1)
	except: 
		return 
		
print "You shall not pass, " + shoutOut3("Dawg")
