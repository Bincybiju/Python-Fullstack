year=int(input("Enter a year : "))
if year%100==0:
    if year%400==0:
        print("Leap year")
    else:
        print("Not leap year")
else:
    if year%4==0:
        print("Leap year")
    else:
        print("Not leap year")