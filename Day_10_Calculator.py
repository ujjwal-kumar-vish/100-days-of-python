def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2


cal_dic = {
    '+' : add,
    '-' : subtract,
    '*' : multiply,
    '/' : divide,
}

should_continue = True
while should_continue:
    x1 = int(input("enter first no.   :-  "))
    x2 = int(input("enter second no.  :-  "))

    for l in cal_dic:
        print(l)

    symbol_choice = input("pick an operation from the line above : ")

    calculation_function = cal_dic[symbol_choice]
    answer = calculation_function(x1,x2)


    print(f" {x1} {symbol_choice} {x2} = {answer} ")

    choice = input('press y is want to continue n if not :-')
    if choice == 'n':
        should_continue = False