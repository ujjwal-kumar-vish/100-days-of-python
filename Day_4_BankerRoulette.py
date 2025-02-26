import random

name_string = input('Give me everybody\'s name, seperated by a comma. (ex- Ujjwal, Rahul, Atul)')
names = name_string.split(", ")

lenth = len(names)-1

randomNumber = random.randint(0, lenth)

print(f"{names[randomNumber]} will pay this time !!!! ")