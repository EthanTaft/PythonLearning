# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 14:40:54 2017

@author: Ethan
"""

# Some Practice

# -----------------------------------------------------------------------------
# define a function that takes an integer as input. If that number is even,
#return True. If that number is not even, return False.

def is_even(x):
    if x % 2 == 0:
        return(True)
    else:
        return(False)

# -----------------------------------------------------------------------------
# For this function, assume for a minute that any number with a decimal form
# like 7.0 is also an integer (like 7 is an integer) but not recognized by 
# python as an integer.
# Write a funciton that tests whether an input number is an integer based on 
# the new criterion above.
import math
def is_int(x):
  if abs(x - math.floor(x)) == 0:
    return(True)
  else:
    return(False)
# -----------------------------------------------------------------------------
# Write a function that takes a positive integer n and returns the sum
# of all that number's digits and another function that returns the product
# of each of that number's digits
def digit_sum(n):
    count = 0
    for i in str(n):
        count = count + int(i)
    return(count)
    
# or do it this way
l = []
b = 434
rightmost = b%10
l.append(rightmost)
b = b // 10

rightmost = b%10
l.append(rightmost)
b = b // 10

rightmost = b % 10
l.append(rightmost)
b = b // 10

# and this is lines 40 to 52 automated in a function
def digit_sum2(n):
    l = []
    for i in range(len(str(n))):
        rightmost = n%10
        l.append(rightmost)
        n = n//10
    return(sum(l))
    
# To multiply the digits of a number
def digit_mult(n):
    multiple = 1
    for i in str(n):
        multiple = multiple * int(i)
    return(multiple)
# -----------------------------------------------------------------------------
# Create a function to calculate the factorial of an integer.  Remember
# factorial(1) = 1 and factorial(0) = 0
# This works but not as well
def factorial(x):
  mult = 1
  for i in range(x):
    mult = mult * (i + 1)
  return(mult)

# Here is a better looking answer
def facto(x):
    ans = 1
    while (x!=0):
        ans *= x # can also be written as ans = x * ans
        x -= 1
    return(ans)
# -----------------------------------------------------------------------------  
# Define a function that will print a boolean stating if a given integer is 
# prime
def is_prime(x):
  if x < 2:
    return(False)
  if x == 2:
      return(True)
  else:
    for i in range(2, x):
      if x % i == 0:
        return(False)
      else:
        return(True)

# Buy/Sell stock to maximize profit on a given day-----------------------------
# What is the max profit we can make
time = [2, 7, 1, 8, 2, 8, 4, 5, 9, 0, 4, 5]
bestProfit = 0
for i in range(0, len(time)):
    for j in range(i + 1, len(time)):
        bestProfit = max(bestProfit, time[j] - time[i])
print(bestProfit)

#------------------------------------------------------------------------------
# Make a function called reverse that takes a string "text" as an argument and
# returns the string in reverse.
# i.e.:
range(len("stuff")) # len of range is 5
0, 1, 2, 3, 4 # do this five times for 5 letters in "stuff"
text1 = ""

# put "stuff"[4] into a new word at the first position
# put "stuff"[3] into a new word at the second position
# put "stuff"[2] into a new word at the third position
# put "stuff"[1] into a new word at the fourth position
# put "stuff"[0] into a new word at the fifth position

def reverse(text):
    text1 = ""
    for i in range(len(text)):
        text1 += text[len(text)-i-1]
    return(text1)

# -----------------------------------------------------------------------------
# Define and use a function that removes all vowels from a
# string and returns the string without the vowels.
# my way of doing it (replacing the vowels in the string with ""):
def anti_vowel(text):
    for i in text:
        if i in "ieaouIEAOU":
            text = text.replace(str(i), "")
    return(text)

# Another way of doing it(adding all non-vowels to a list and then joining)
def fn(word):
    l = []
    for i in word:
        if i not in "aeiouAEIOU":
            l.append(i)           
    return("".join(l))
    
# or
def anti_vowel2(text):
    a= ""
    for item in text:
        if item not in "aeiouAEIOU":
            a += item
    return(a)
    
# or remove items without iterating using generator expression
def anti_vowel3(text):
    return "".join(item for item in text if item not in "aeiouAEIOU")

# or
def anti_vowel4(text):
    t=""
    for c in text:
        for i in "ieaouIEAOU":
            if c==i:
                c=""
            else:
                c=c
        t=t+c
    return t

# -----------------------------------------------------------------------------

score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}

# Define a function that takes a string as input and returns the equivalent 
# scrabble score for that word based on the letter dictionary above
def scrabble_score(word):
  word = word.lower()
  total = 0
  for i in word:
    total = total + score[i]
  return(total) 

# -----------------------------------------------------------------------------
# Write a function called censor that takes two strings(text and word).
# Return the text with the word replaced with asterisks.  Input strings 
# are assumed to not contain punctuation or upper case letters.
# The number of asterisks should correspond to the number of letters in the
# censored word
def censor(text, word):
    d = text.split()
    for i in range(len(d)):
        if d[i] == word:
            d[i] = "*" * len(word)
    return(" ".join(d))

print(censor("this hack is wack hack", "hack"))

# -----------------------------------------------------------------------------

# Make a function that returns the number of times an item occurs in a list

def count(sequence, item):
    total = 0
    for i in sequence:
        if i == item:
            total = total + 1
    return(total)

# Make a function that takes a list of numbers and removes all odd numbers
# from the list and returns the result.  Do not directly modify the list;
# instead return a new list with only the even numbers
def purify(numbers):
  new = []
  for i in numbers:
    if i % 2 == 0:
      new.append(i)
  return(new)

# -----------------------------------------------------------------------------

# Make a function that takes a list and removes all elements in the list that
# are the same.  Do not modify the list you take as input; instead return a new
# list.

def remove_duplicates(some_list):
  new = []
  for i in some_list:
    if i not in new:
      new.append(i)     
  return(new)

# -----------------------------------------------------------------------------
# Find the median of a list of numbers
def median(number_list):
  sorted_list = sorted(number_list)
  if len(sorted_list) % 2 == 0: # even number of elements
    A = sorted_list[:len(sorted_list)//2]
    B = sorted_list[len(sorted_list)//2:]
    return((A[-1] + B[0]) / 2.0)
  else: # odd number of elements
    return(sorted_list[len(sorted_list)//2])
    
# or similar:
def median2(lst):
    sorted_list = sorted(lst)
    if len(sorted_list) % 2 != 0:
        #odd number of elements
        index = len(sorted_list)//2 
        return sorted_list[index]
    elif len(sorted_list) % 2 == 0:
        #even no. of elements
        index_1 = len(sorted_list)/2 - 1
        index_2 = len(sorted_list)/2
        mean = (sorted_list[index_1] + sorted_list[index_2])/2.0
        return mean









