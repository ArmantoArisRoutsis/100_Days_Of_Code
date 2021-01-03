print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

first = input("\nYou are at a crossroad, where do you want to go? 'Left' or 'Right' :").lower()
if first == "left":
  second = input("\nYou've come to a lake. There is an islandin the middle of the lake.Type 'Swim' to swim across or type 'Wait' to wain for a boat?").lower()
  if second == "wait":
    third = input("\nYou arive at the Island unharmed. There is a house with 3 doors. One is Red, one is Blue and one is Yellow.Which door will you choose? :).lower()
    if third == "yellow":
      print("Congratulations. You found the treasure! You win!")
    elif third == "red":
      print("You fell into a pit Fire. Game Over")
    elif third == "blue":
      print("You fell into a pit filled with Beasts. Game over")
    else:
      ("Game Over.")
  else:
    print("You are attacked by a vicious crocodile. Game Over.")
else:
  print("Game Over.")