print('welcome to the tip calculator')
bill = float(input("Enter the bill amount :"))
people = int(input("enter the no of people :"))
tip = int(input("enter the tip amount 10 12 14 etc percentage :"))
f_amount = (bill*tip/100 + bill)/people
formating_amount = "{:.2f}".format(f_amount)
print(f"Each person should pay {formating_amount} ")