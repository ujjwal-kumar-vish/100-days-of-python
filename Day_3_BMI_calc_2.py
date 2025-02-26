h = float(input("enter your height in m :"))
w = float(input("enter your weight in kg :"))
BMI = w/(h*h)
if BMI < 18.5 :
    print (f"your BMI is {round(BMI,2)}, you are underweight")
elif BMI < 25 :
    print (f"your BMI is {round(BMI,2)}, you are normal weight")
elif BMI < 30 :
    print (f"your BMI is {round(BMI,2)}, you are overweight")
elif BMI < 35 :
    print (f"your BMI is {round(BMI,2)}, you are obese")
else :
    print (f"your BMI is {round(BMI,2)}, you are clinically obese")