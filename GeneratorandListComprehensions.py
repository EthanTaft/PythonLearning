# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 18:02:15 2017

@author: Ethan
"""

# Generator Comprehension Tutorial

#Original list comprehension

my_list = [1, 3, 5, 9, 2, 6]
filtered_list = [item for item in my_list if item > 3]
print(filtered_list)

#Generator expression
filtered_gen = (item for item in my_list if item > 3)
print(filtered_gen)

#Prove it's the same thing as a list comprehension 
gen_to_list = list(filtered_gen)
print(gen_to_list)
filtered_list == gen_to_list


#Anti-Vowel generator expression
text = "stuff"
b = (item for item in text if item not in "aeiouAEIOU")
b_list = list(b)
print(b_list)
b_final = "".join(b_list)
print(b_final)

# lines 28 through 32 are the same as:
"".join(item for item in text if item not in "aeiouAEIOU")