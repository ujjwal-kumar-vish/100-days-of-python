import string

all_alphabets = list(string.ascii_lowercase)
cypher =[]
'''
choice = input("enter y if you want to encode ypur message \nenter n if you want to decode a message\n")

userInput = input("Type your message : \n")

shiftNum = int(input("Type the shift number :\n"))

cypher = []

for letter in userInput:
    cypher.append(letter)
    '''

def incoding(all_alphabets,shiftNum,cypher):
    for cy in range(0,len(cypher)):
        index_ = all_alphabets.index(cypher[cy])
        if (index_ + shiftNum) >= len(all_alphabets) :
            index_ = index_ + shiftNum - len(all_alphabets) - 1
        #print(index_, shiftNum,"lenght of all_alphabet",len(all_alphabets),len(cypher))
        cypher[cy] = all_alphabets[index_ + shiftNum]
    return cypher

def decode(all_alphabets,shiftNum,cypher):
    for cy in range(0,len(cypher)):
        index_ = all_alphabets.index(cypher[cy])
        if (index_ - shiftNum) < 0 :
            index_ = index_ - shiftNum + len(all_alphabets) + 1
        #print(index_, shiftNum,"lenght of all_alphabet",len(all_alphabets),len(cypher))
        cypher[cy] = all_alphabets[index_ - shiftNum]
    return cypher
x=True
while x==True:

    choice = input("want to continue \nenter y if you want to encode ypur message \nenter n if you want to decode a message \nenter x to quit\n")

    if choice == 'y':
        userInput = input("Type your message : \n")
        shiftNum = int(input("Type the shift number :\n"))
        cypher = []
        for letter in userInput:
            cypher.append(letter)
        incoding(all_alphabets,shiftNum,cypher)
        print(cypher)
    elif choice == 'n':        
        userInput = input("Type your message : \n")
        shiftNum = int(input("Type the shift number :\n"))
        cypher = []
        for letter in userInput:
            cypher.append(letter)
        decode(all_alphabets,shiftNum,cypher)
        print(cypher)
    else:
        print("we are now going to shutdown this program")
        x=False

    word =''
    for i in cypher:
        word += i
    print(word)