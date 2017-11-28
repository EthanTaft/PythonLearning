# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 22:18:30 2017

@author: Ethan
"""
from random import randint

count = 0

if count < 5:
    print("Hello, I am an if statement and count is", count)
    
while count < 5:
    print("Hello, I am a while and count is", count)
    count += 1

# Print the square of numbers incremented from 1 to 10 and 
# including 10 while number is less than or equal to 10
num = 1

while num <= 10:  # Fill in the condition
  # Print num squared
  print(num ** 2)
  # Increment num (make sure to do this!)
  num += 1

# While a user response is not in the expected response list, prompt again
# for a different input
choice = input('Enjoying the course? (y/n)')

while choice not in ["y", "n"]:  # Fill in the condition (before the colon)
  choice = input("Sorry, I didn't catch that. Enter again: ")
  
# An example of an infinite loop: Do not run. There is no counter that would
# trigger an exit condition
"""
number = 0

while number < 10:
    print(number)
"""

# while/else
# similar to if/else but not completely.  The else block in 
# a while/else will execute anytime the loop condition is evaluated
# to False (Even if the loop is never entered of if the loop exits normally)

print("Lucky Numbers! 3 numbers will be generated.\
      \nIf one of them is a '5' you lose!")

count = 0
while count < 3:
    num = randint(1, 6)
    print(num)
    if num == 5:
        print("Sorry, you lose!")
        break
    count += 1
else:
    print("You Win!")

# Use a while loop to let the user keep guessing so long as the
# guesses_left is greater than zero

# Define a random number that the user is going to try to guess
random_number = randint(1, 10)
guesses_left = 3

while guesses_left > 0:
    guess = int(input("What is your number guess?: "))
    if guess == random_number:
        print("You Win!")
        break
    guesses_left -= 1
else:
    print("\nYou lose.")
    
# A for loop that promts the user for a hobbie. It will create a list
# of hobbies.
hobbies = []

# Add your code below!
for i in range(3):
  hobby = input("What is one of your hobbies?: ")
  hobbies.append(hobby)
print(hobbies)

# For each character in phrase, print it out.  If the character
# is an "A" or "a" print "X" instead. Use end = "" after each print statement
# to keep the printed statements on the same line.

phrase = "A bird in the hand..."

for char in phrase:
    if char in ["A", "a"]:
        print("X", end = "")
    else:
        print(char, end = "")

print() # used to escape printing on the same line.
print("Stuff")

# you can also use "sys" to pring stuff on the same line

import sys

for char in phrase:
    if char in ["A", "a"]:
        sys.stdout.write("X")
    else:
        sys.stdout.write(char)


# For each key in the dictionary, print key and it's value on the same line
d = {'a': 'apple', 'b': 'berry', 'c': 'cherry'}

for key in d:
  # Your code here!
  print(key, d[key])


# For each item in a list, print the item and it's index value
choices = ['pizza', 'pasta', 'salad', 'nachos']

print('Your choices are:')

for index, item in enumerate(choices):
  print(index, item)
  
# For each item in a list, print the item and its index value but
# print starting at index value appearing as 1.
choices = ['pizza', 'pasta', 'salad', 'nachos']

print('Your choices are:')

for index, item in enumerate(choices):
    print(index + 1, item)


# Iterate over two lists at one time. Compare each number and print
# The larger of the two numbers. Notice how these two for loops act differently

list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

# this will print only max(list_a[1], list_b[1]) etc.
for a, b in zip(list_a, list_b):
    print(max(a, b))
    
# this will print all pairwise comparisons
for index, a in enumerate(list_a):
    for b in list_b:
        print(index + 1, max(a, b))

# Or do it a better way with the index number
for index, (a, b) in enumerate(zip(list_a, list_b)):
    print(index, max(a, b))



































