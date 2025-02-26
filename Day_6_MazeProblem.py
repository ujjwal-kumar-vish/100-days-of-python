# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json


'''
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def stick_to_right():
    # write the algortihem to stick to the right wall of theis maze
    while not right_is_clear():
        if front_is_clear():
            move()
        elif not front_is_clear():
            turn_left()
        else:
            print("main pagal hun")      
    
while not at_goal():
    stick_to_right()
    if at_goal():
        break
    turn_right()
    move()
'''