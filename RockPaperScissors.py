"""This program prompts users to select rock, paper, or scissors.  The computer
 then randomly selects rock, paper, or scissors.  The winner is determined and 
 the user is then informed who the winner is.
"""

from random import randint
from time import sleep

OPTIONS = ["R", "P", "S"]
LOST = "Computer Wins"
WON = "You Win!"

def decide_winner(user_choice, computer_choice):
  print ("Users Choice: %s" %(user_choice))
  print("Computer selecting...")
  sleep(1)
  print("Computer's Choice: %s" %(computer_choice))
  user_choice_index = OPTIONS.index(user_choice)
  computer_choice_index = OPTIONS.index(computer_choice)
  if user_choice_index == computer_choice_index:
    print("Tie!")
  elif user_choice_index == 0 and computer_choice_index == 2:
    print(WON)
  elif user_choice_index == 1 and computer_choice_index == 0:
    print(WON)
  elif user_choice_index == 2 and computer_choice_index == 1:
    print(WON)
  elif user_choice_index > 2:
    print("Invalid outcome selected: Program shutting down...")
    return
  else:
    print(LOST)
    
def play_RPS():
  print("You are now playing Rock-Paper-Scissors")
  user_choice = input("Select R for Rock, P for Paper, or S for Scissors: ").upper()
  sleep(1)
  computer_choice = OPTIONS[randint(0, len(OPTIONS) - 1)]
  decide_winner(user_choice, computer_choice)
  
play_RPS()