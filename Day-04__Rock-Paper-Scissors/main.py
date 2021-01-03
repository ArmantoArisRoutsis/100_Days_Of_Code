import random
import sys

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
icons = [rock,paper,scissors]
choice = ["rock","paper","scissors"]
computerChoice = random.choice([1,2,3])
userChoice = int(input("Get ready! Choose one of the three options:\n1.rock\n2.paper\n3.scissors\n"))

if userChoice<1 or userChoice>3:
  print("You typed an invalid number")
  sys.exit()

print(f"You chose {choice[userChoice-1]} \n{icons[userChoice-1]}\n")
print(f"The computer chose {choice[computerChoice-1]}\n{icons[computerChoice-1]}\n")


if(userChoice == computerChoice):
  print("It's a draw!")
else:
  if(userChoice == 1 and computerChoice== 3):
      print("The user wins.")
  elif(userChoice== 3 and computerChoice== 1):
      print("The computer wins.")
  elif(userChoice > computerChoice):
      print("The user wins.")
  elif(userChoice < computerChoice):
      print("The computer wins.")
