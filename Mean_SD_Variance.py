# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 17:36:23 2017

@author: Ethan
"""

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]
# Print all the grades
def print_grades(grades_input):
  for grade in grades_input:
    print (grade)
    
# Calculate the sum of scores used in calculating the mean
def grades_sum(scores):
  total = 0
  for score in scores: 
    total += score
  return total

# Calculate the mean, also used in calculating the average
def grades_average(grades_input):
  sum_of_grades = grades_sum(grades_input)
  average = sum_of_grades / float(len(grades_input))
  return average

# Calculate the variance, used in calculating the standard deviation
def grades_variance(scores):
  average = grades_average(scores)
  variance = 0
  for i in scores:
    variance += ((i - average) ** 2) # increase variance by this amount every iteration
  return(variance / len(scores))
  
# Calculate the standard deviation
def grades_std_deviation(scores):
    variance = grades_variance(scores)
    return(variance ** 0.5)


print(grades_sum(grades))
print(grades_average(grades))
print(grades_variance(grades))
print(grades_std_deviation(grades))