# http://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json
# use this code on the above webpage

'''
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    wall_height = 0
    turn_left()
    while not right_is_clear():
        move()
        wall_height += 1
    turn_right()
    move()
    turn_right()
    while wall_height >0:
        move()
        wall_height -= 1
    turn_left()
    
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
'''