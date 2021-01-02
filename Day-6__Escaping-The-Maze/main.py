""" 
 This code only works for the 'Reborgs World' since the functions 
used are fictional and are only ment to be used for the maze game
"""
def turn_right():
   turn_left()
   turn_left()
   turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        while front_is_clear():
             move()
    else:
        turn_left()