# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 18:30:50 2017

@author: Ethan
"""

# ADVANCED TOPICS IN PYTHON----------------------------------------------------

# Dictionaries ----------------------------------------------------------------
# In Dictionaries, there are Items, Keys, and values.  Each item contains one
# key and value.  Values belong to keys.  To add more than one value to a key
# create a list of values.

# Methods for dictionaries in python (they do not return values in any
#                                     specific order).
# .items() returns all tuples in the dictionary (key, value)
# .keys() returns a list of all the dictionary's keys
# .values() returns a list of all the dictionary's values

# Note: Tuples are immutable and are surrounded by (). They contain any data 
# type.

# For every key in a dictionary print out the key, then a space, then the value
# stored by that key:
# We can iterate over the keys of a dictionary by creating a for loop like
# for key in dictionary...
my_dict = {"a": 1, "b": 2, "c": 3}
for key in my_dict:
  print(key, my_dict[key])

# List comprehensions ----------------------------------------------------------
# Generate a list according to some logic
# for example, for every i in the range(51) if that i is even, put it into
# the list.
evens_to_50 = [i for i in range(51) if i % 2 == 0]
print(evens_to_50)

# Build a list including the squares of the even numbers between 1 to 11.
# both ways below work since the square of an even number is also even.
even_squares = [x ** 2 for x in range(1, 11) if (x ** 2) % 2 == 0]
b = [x ** 2 for x in range(1, 11) if x % 2 == 0]
print(even_squares)
print(b)

# Build a list that has every x from 1 to 10 only if x cubed is evenly
# divisible by 4.
cubes_by_four = [x ** 3 for x in range(1, 11) if (x**3) % 4 == 0]
print(cubes_by_four)

# List Slicing ----------------------------------------------------------------

# [start:end:stride] Start is inclusive, end is exclusive, stride is the space
# between items in the sliced list (the space between items!). Default stride
# is one.

# Print out every odd element of my_list from start to finish. Positive stride
# progresses through a list from left to right. Negative stride goes from right
# to left.
my_list = list(range(1, 11))
b = my_list[::2]
print(b) 
# or
c = my_list[0:11:2]
print(c) 
# or
print(my_list[:11:2])

# Reverse a list
my_list = list(range(1, 11))
backwards = my_list[::-1]

# Reverse again this time got backwards by tens.
to_one_hundred = list(range(101))

backwards_by_tens = to_one_hundred[::-10]
print(backwards_by_tens)

# Create a list, odds, that's just the odd numbers in a list
to_21 = list(range(1, 22))
odds = to_21[::2] # by every other one
print(odds)
#create a third list that has only the middle third of to_21
middle_third = to_21[7:14]
print(middle_third)

# Anonymous functions ---------------------------------------------------------
double = lambda x: x*2
print(double(5))

# Create a lambda that returns only "python" from the list below using the
# filter function
languages = ["HTML", "JavaScript", "Python", "Ruby"]
print(list(filter(lambda ls: ls == "Python", languages)))

# Create a list, squares, that consists of the squares of the numbers 1 through
# 10. Use filter() and a lambda expression to print out only the squares that
# are between 30 and 70 inclusive.
squares = [x ** 2 for x in range(11)]
print(list(filter(lambda ls: ls >= 30 and ls <= 70, squares)))

#------------------------------------------------------------------------------

# use a list commprehension to create a list that consists only of the numbers
# between 1 and 15(inclusive) that are evenly divisible by 3 and 5.

threes_and_fives = [i for i in range(1, 16) if i % 3 == 0 or i % 5 == 0]
threes_and_fives


# Use list slicing to extract messages and save it to a variable called message
# Our message is backwards and the letter we want is every other letter.
garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
garbled[::-2] #This command starts at the end(rightmost place) and goes
#backwards by every other letter.
stuff = "some random string"
stuff[::1] # by one to the end

# Create a new variable called message.  Set it to the result of calling
# filter() with the appropriate lambda that will filter out the "X's".
garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"

message = list(filter(lambda x: x != "X", garbled))
print(message) # doesn't work so well
print("".join(message))

#Use a generator expression instead
message = (x for x in garbled if x != "X")
print("".join(message))






