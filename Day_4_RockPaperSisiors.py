import random 
def RockPaperSisiors():
    pc_input = random.randint(1, 3)
    print(pc_input)
    userInput = int(input("enter \n 1 for rock \n 2 for paper \n 3 for sisiors\n"))
    if userInput == pc_input:
        print ( "both took out same , its a draw")
    elif userInput == 1 and pc_input == 2 :
        print ("pc put out paper, ypu loose")
    elif userInput == 1 and pc_input == 3 :
        print ("pc put out sisiors, you win!")
    elif userInput == 2 and pc_input == 3 :
        print ("pc put out sisiors, you loose")
    elif userInput == 2 and pc_input == 1 :
        print ("pc put out rock, you win!")
    elif userInput == 3 and pc_input == 1 :
        print ("pc put out rock, you loose")
    elif userInput == 3 and pc_input == 2 :
        print ("pc put out paper, you win!")
    elif userInput == 0 :
        #will think about it later
        print('exit')
    else:
        print("wrong input")
    con = input('continue? y/n  ')
    if con == 'y':
        RockPaperSisiors()


RockPaperSisiors()