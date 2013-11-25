"""
Week 1: Debugging exercise 3. Debugging Dictionary Operations 

Each one of these exercises requires you to alter the code in some way. 
If the code works properly then it will run up until that point and then stop.

Each exercise should require only one kind of change/alteration.
"""

__author__ =  'Bernie Hogan'
__version__=  '1.0'

#1. Debug this line:
dict1 = {"a":"First var","b":"Second var","c":"Third var"}

#2. Comment out the wrong keys 
# print dict1["A"]
# print dict1[a]
print dict1['a']
# print dict1[1]


#3. Print the keys
for i in dict1.keys():
	print "key:",i
	print "value:",dict1[i]

#4. Debug this code:
dict1.has_key("b")

#5. Debug this code: 
print dict1["c"]

#6. Debug this code (assigning a new key-value pair):
dict1["d"] = "Yet another variable"

print "Whew. Aren't you glad that's through?"