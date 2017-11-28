"""This function/program will simulate rolling a pair of dice and guessing of
the outcome of the roll. If the user's guess is greater than the total value,
they win. If it is smaller, they lose.
"""

from random import randint
from time import sleep

def get_user_guess():
  user_guess = int(input("What is your guess?:"))
  return user_guess

def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = number_of_sides * 2
  print("The maximum possible value of this two dice roll is " + str(max_val))
  sleep(1)
  user_guess = get_user_guess()
  if user_guess > max_val:
    print("Your guess must be less than or equal to the total number of sides "
          "of the two die")
    return
  else:
    print("Rolling...")
    sleep(1)
    print("First roll: %d" %(first_roll))
    sleep(1)
    print("Second roll: %d" %(second_roll))
    total_roll = first_roll + second_roll
    print("Total roll: %d" %(total_roll))
    print("Result...")
    sleep(1)
    if user_guess > total_roll:
      print("You win!")
      return
    else:
      print("You lost...")
      return
