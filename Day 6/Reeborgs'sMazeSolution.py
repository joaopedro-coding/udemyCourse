# Reeborg's world! Maze code solution!

# Solution 1
def turn_right():
    turn_left()
    turn_left()
    turn_left()
counter = 0
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
        counter += 1
        if counter == 4:
            turn_left()
        
    elif front_is_clear():
        move()
    else:
        turn_left()

# Solution 2
def turn_right():
    turn_left()
    turn_left()
    turn_left()
  
while front_is_clear():
  move()
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
        
    elif front_is_clear():
        move()
    else:
        turn_left()
