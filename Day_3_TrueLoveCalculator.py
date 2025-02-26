print('Welcome to the Love Calculator!')
name1 = input("What is your name?\n")
name2 = input("what is their name?\n")

name1= name1.lower()
name2= name2.lower()

l = name1.count('l') + name2.count('l')
o = name1.count('o') + name2.count('o')
v = name1.count('v') + name2.count('v')
e = name1.count('e') + name2.count('e')

onceplace = l+o+v+e

t = name1.count('t') + name2.count('t')
r = name1.count('r') + name2.count('r')
u = name1.count('u') + name2.count('u')
e = name1.count('e') + name2.count('e')

tensplace = t+u+r+e

love_score = tensplace*10+onceplace

if love_score < 10 or love_score > 90 :
    print(f"Your love scroe is {love_score}%, you go together like coke and mentos. ")
elif love_score > 40 and love_score<50 :
    print(f"your love socre is {love_score}%, you are alright together ")
else:
    print(f'your love is {tensplace*10+onceplace} %')