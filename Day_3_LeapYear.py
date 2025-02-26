y=int(input("enter the year you want to check :"))

if y%4==0 :
    if y%100==0 :
        if y%400==0 :
            print('its a leap year')
        else:
            print('not a year of leap')
    else:
        print("its a leap year but not 2000 ;)")
else:
    print('not a leap year')