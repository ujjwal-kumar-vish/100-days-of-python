import random
import string

all_alphabets = list(string.ascii_letters)

print(all_alphabets)

all_numbers = list(string.digits)

print(all_numbers)

all_Symbols = list(string.punctuation)

print(all_Symbols)

print ("welcome to PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))

nr_symbols = int(input(f"how many symbols would you like? \n"))

nr_numbers = int(input(f"How many numbers would you like? \n"))




'''rand_chose = 0
rand_alpha = 0
rand_symbols = 0
rand_num = 0

for i in range(0, nr_letters+nr_numbers+nr_symbols):

    if nr_symbols>0 and nr_letters>0 and nr_numbers>0:
        rand_chose = random.randint(1,3)
    elif nr_numbers<=0:


    if rand_chose == 1:
        #letter
        if nr_letters<=0:
            continue
        else:
            nr_letters -= 1
            rand_alpha = random.randint(0,len(all_alphabets)-1)
            password.append(all_alphabets[rand_alpha])

    elif rand_chose == 2:
        #symbol
        if nr_symbols<=0:
            continue
    

    #password.append(all_alphabets[i])'''

'''
password = []
password1 = random.sample(all_alphabets,nr_letters)
password2 = random.sample(all_numbers,nr_numbers)
password3 = random.sample(all_Symbols,nr_symbols)

password.append(password1)
password.append(password2)
password.append(password3)
print(str(password))
'''



#Eazy level Totorial
'''
password = ""

for char in range(1,nr_letters+1):
    random_char = random.choice(all_alphabets)
    password += random_char

for char in range(1,nr_symbols+1):
    password+= random.choice(all_Symbols)

for char in range(1,nr_numbers+1):
    password += random.choice(all_numbers)

print(password)
'''

# hard level

password = []

for char in range(1,nr_letters+1):
    random_char = random.choice(all_alphabets)
    password.append(random_char)

for char in range(1,nr_symbols+1):
    password+= random.choice(all_Symbols)

for char in range(1,nr_numbers+1):
    password += random.choice(all_numbers)

print(password)
random.shuffle(password)
print(password)

pas = ''
for char in password:
    pas+=char

print(pas)