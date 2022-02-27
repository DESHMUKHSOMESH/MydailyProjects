# program to know leap year or not.
year = int(input("Enter the year:"))
if year % 4 == 0:
    if year % 100 == 0:
        print("check for 400 divisibilty")
        if year % 400 == 0:
            print("leap year")
        else:
            print("not a leap year")
    else:
        print("leap year")
else:
    print("not leap year.")
