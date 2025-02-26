# here we go again anathor fizzbuzz program

start = int(input("enter the starting value  "))
end = int(input("enter the ending value  "))

for i in range(start,end+1):
    if i%3==0 and i%5==0:
        print("FizzBizz")
    elif i%3==0:
        print('Fizz')
    elif i%5==0:
        print('Buzz')
    else:
        print(i)