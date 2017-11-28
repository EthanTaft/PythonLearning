"""Some random multi-line comment that doesn't really span multiple lines. This
function will be used to calculate the area of a circle or triangle depending
on the user's input.
"""

# gain access to the non-built in python code
from math import pi
from time import sleep
from datetime import datetime

now = datetime.now()

print("Calculator Startup Time:")
print ("%s/'%s/%s %s:%s"  %(now.month, now.day, now.year, now.hour, now.minute))
sleep(1)

hint = "Don't forget to include the correct units!\nExiting..."

option = input("Enter C for Circle or T for Triangle: ")
option = option.upper()

if option == "C":
  radius = float(input("What is the radius of the circle?: "))
  area = pi * (radius**2)
  print("The pie is baking...")
  sleep(1)
  print("Area = %.2f, \n%s" % (area, hint))
elif option == "T":
  base = float(input("what is the length of the base?: "))
  height = float(input("what is the height?: "))
  area = (base*height) / 2
  print ("Uni Bi Tri...")
  sleep(1)
  print("Area = %.2f \n%s" %(area, hint))
else:
  print("You entered garbage out. Exiting program...")
