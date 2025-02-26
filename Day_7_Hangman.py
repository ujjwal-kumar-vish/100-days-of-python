import random

'''
use this code for clearing the terminal

from replit import clear

clear()

'''

life = 6

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["ardvark","baboon","camel"]

chosen_word = (random.choice(word_list))

display = []
chosen_word2 = []
for i in range(0,len(chosen_word)):
    display.append("_")
    chosen_word2.append(chosen_word[i])

print(chosen_word)

#guess = input("Make a guess  - ")

def hangmanWordCheck(chosen_word,guess,display):
    for letter in range(0,len(chosen_word)):
        if guess == chosen_word[letter]:
            display[letter] = chosen_word[letter]
            #print("true")
        else:
            pass
            #print("false")
    return display

while life>0:
    guess = input("Make another guess  - ")
    print(display)

    if guess in chosen_word :
        hangmanWordCheck(chosen_word,guess,display)
        print(stages[life])
        if chosen_word2 == display:
            print ("you win")
            break
        else:
            continue
    else:
        life -= 1
        print(stages[life])
        print ("\nwrong guess \nlife left ",life)
        if life == 0:
            print("you loose \n game over")

#print(display)
dis = ''
 
for x in display:
    dis += x

print(dis)