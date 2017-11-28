# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 11:46:31 2017

@author: Ethan
"""

"""Build a caldendar that the user will be able to interact with from the 
command line.  The user should be able to view the calendar, add events,
pdate events, and delete events.
"""

"""The program should behave in the following way: Print a welcome message to 
the user.  Prompt the user to view, add, update, or delete and event on the
calendar. Depending on what the user specifies they want to do, the program
should do exactly what the user wants it to do.  The program should never
terminate unless the user decides to exit.
"""

"""Build a calendar, man!
"""
from time import sleep, strftime
user_name = "Darrill"

calendar = {}

def welcome():
  print(user_name +  " welcome to your personal calendar.")
  print("Your calendar is opening...")
  sleep(1)
  print("Date: "+ strftime("%A %B %d, %Y"))
  print("Time: " + strftime("%I:%M:%S"))
  sleep(1)
  print("What would you like to do?")
  
def start_calendar():
  welcome()
  start = True
  while start == True:
    user_choice = input("Choose A to add, U to Update, V to View D to Delete, " 
                        "X to Exit: ")
    user_choice.upper()
    if user_choice in ["v", "V"]:
      if len(calendar.keys()) == 0:
        print("The calendar is empty")
      else:
        print(calendar)
    elif user_choice in ["u", "U"]:
      date = input("What date?: ")
      update = input("Enter the update: ")
      calendar[date] = update
      print("Your calendar was updated")
      print(calendar)
    elif user_choice in ["a", "A"]:
      event = input("Enter event: ")
      date = input("Enter date MM/DD/YYYY: ")
      if len(date) > 10 or int(date[6:10]) < int(strftime("%Y")):
        print("Entered date is invalid")
        try_again = input("Try Again? Y for Yes, N for N: ")
        if try_again == "Y":
            continue
        else:
            start = False
      else:
        calendar[date] = event
        print("Event Added!")
        print(calendar)
    elif user_choice in ["d", "D"]:
      if len(calendar.keys()) == 0:
        print("The calendar is already empty.")
      else:
        event = input("What event?: ")
        for i in list(calendar.keys()):
          if calendar[i] == event:
            del(calendar[i])
            print("The event was successfully deleted.")
            print(calendar)
          else:
            print("That event does not yet exist in the calendar.")
    elif user_choice in ["x", "X"]:
      start = False
    else:
      print("Your choice is not a valid choice for this program.")
      start = False



