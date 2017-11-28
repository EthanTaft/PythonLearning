# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 16:38:41 2017

@author: Ethan
"""

# Bitwise Operators

# >> right shift
# << left shift
# & bitwise AND
# | bitwise OR
# ^ bitwise XOR
# ~ bitwise NOT


# Print binary numbers in base 10
print(0b100)
# Print base 10 numbers in binary form or print binary numbers
# in base 10 form
print(bin(7))
print(bin(0b100))
# Use int() to print ouf the base 10 equivalent of the binary
# number 11001001
print(int("11001001", 2))

# Shifts --------------------------------------------------
shift_right = 0b1100
shift_left = 0b1
print(shift_right)
print(shift_left)
# Your code here!
shift_right = shift_right >> 2
shift_left = shift_left << 2
print(shift_right)
print(shift_left)
print(bin(shift_right))
print(bin(shift_left))
print(shift_left)
print(shift_right)

# Bitwise AND operator -------------------------------
# print out the result of calling bin() on 0b1110 "&" 0b101
print(bin(0b1110 & 0b101))

# Bitwise OR operator ---------------------------------
print(bin(0b1110 | 0b101))
# Try to write a for loop to do the same thing as the | operator
string = "0b"
len1 = len(str(0b100))
len2 = len(str(0b101))
ls = []
for i in str(0b100):
    for j in str(0b101):
        if i == 1 or j == 1:
          ls.append(i)    

# Bitwise XOR operator (exclusive operator)---------------------------
# Turns on the bit if either of the numbers are 1 but not both. If both then 0
# print the result of using ^ on 0b1110 and ob101 as a binary string
# Try to do it on your own without using the ^ operator.
print(bin(0b1011))

# Bitwise NOT operator
# flips all the bits in a single number
# Mathematically this adds one to the number and then makes it
# negative
print(~1) # should = -2
print(~123)
print(~0b001)
print(~0b100)

# Bit Mask--------------------------------------------------
# A bit mask is a variable to aid with bitwise operators
num = 0b1100 # Find out if the third bit is on
mask = 0b100 # create a mask with the third bit on
desired = num & mask
if desired > 0:
    print("Bit was on")

# Define a function to check if the fourth bit of an integer is on
def check_input(input):
    mask = 0b1000
    if(mask & input) > 0:
        return("on")
    else:
        return("off")
check_input(8)
check_input(0b1010)
check_input(0b0101)

# Make sure the rightmost bit of a number is on.
a = 0b110
mask = 0b1
desired = a | mask
print(desired)

# Use a bitmask and the value a in order to make sure the third bit from the
# right of a is turned on.
a = 0b10111011
mask = 0b100
desired = a | mask
print(bin(desired))

# Flip all of the bits in a number using the XOR ^
a = 0b110
mask = 0b111
desired = a ^ mask
print(bin(desired))

a = 0b11101110
mask = 0b11111111
desired = a ^ mask
print(bin(desired))

# You can use left shifts and right shifts to slide a mask into place
# Turn on the 10th bit from the right of the integer a.
a = 0b101
mask = (0b1 << 9)
desired = a ^ mask
print(desired)

# Make a function called flip_bit that takes inputs number and n
# Flip the nth bit with the ones bit being the first bit and store it in result
# Return the result of calling bin(result)
def flip_bit(number, n):
    mask = 0b1 << n - 1
    result = number ^ mask
    return(bin(result))
flip_bit(0b111, 2)
