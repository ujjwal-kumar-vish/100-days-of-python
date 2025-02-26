print("Welcome to Pizza Deliveries!")
size = input("What sizw pizza do you want? S, M, or L ")
print(size)
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N")
cost_of_p = 0


if size == 'm':
    cost_of_p += 20
    print(cost_of_p,'m')
    if add_pepperoni == 'y':
        cost_of_p += 3
        print(cost_of_p,'m')
    if extra_cheese ==  'y':
        cost_of_p += 1
        print(cost_of_p,'m')
    #print(f"Your final bill is : {cost_of_p} ")

elif size == 'l':
    cost_of_p += 25
    print(cost_of_p,'l')
    if add_pepperoni == 'y':
        cost_of_p += 3
        print(cost_of_p,'l')
    if extra_cheese ==  'y':
        cost_of_p += 1
        print(cost_of_p,'l')
    #print(f"Your final bill is : {cost_of_p} ")

elif size == 's':
    cost_of_p += 15
    print(cost_of_p,'s')
    if add_pepperoni == 'y':
        cost_of_p += 2
        print(cost_of_p,'s')
    if extra_cheese ==  'y':
        cost_of_p += 1
        print(cost_of_p,'s')
    #print(f"Your final bill is : {cost_of_p} ")
    
print(f"Your final bill is : {cost_of_p} ")