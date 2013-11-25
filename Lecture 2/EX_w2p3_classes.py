"""
Week 2: Example 3: Considering classes

Classes are a form of abstraction in object oriented code. They allow us to separate different parts of the program and reuse techniques."""

__author__ =  'Bernie Hogan'
__version__=  '1.0'

# This is a class method. The main parts are the class name, 
# the __init__ method (intialization) and any helper methods. 
# "self" is an important word in classes - it refers to the value
# inside the class
class tester:
	def __init__ (self, val):
		self.value = val

	def multiplyValue (self, multiplier = 3):
		print "New value is %d, or %d (the old value) * %d (the multiplier)" % (self.value * multiplier, self.value, multiplier)
		self.value = self.value * multiplier
	
	def getValue (self):
		return self.value
		
	def setValue (self, value):
		self.value = value

lb = "\n-----------------\n"


print "We begin by creating an instance of a \"tester\" object"
t1 = tester(4)

# Each one of the objects can use the class methods, such as getValue
print t1
print t1.getValue()

# You can create several instances of a class. 
# Each one is its own object	
t2 = tester(3)
t3 = tester(10)

# Because they are objects you can put them in a list
newlist = [t1,t2,t3]

# and a list is iterable
print lb
print "We can iterate through several objects in a list:"
for i in newlist: print i.getValue()
	
# But class methods don't just return values, they can alter the contents of the object
print lb
print "In a for loop, we can act on the objects."
for i in newlist: i.multiplyValue()

# Now when we iterate through the objects, what happens
print lb
print "When we now print the value, we get the new value"
print "Iterators point to objects, not create copies"
print "but you would never know it if you didn't act on the object internally."
for i in newlist: print i.getValue()

# We can also access the objects' variables directly
print lb
print "To access an object's variables, simply type ojbectName.variable:"
print t1.value