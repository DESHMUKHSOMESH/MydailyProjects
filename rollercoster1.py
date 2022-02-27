print("welcome to roller coaster")
height = int(input("Enter your height:"))
age = int(input("Enter your age:"))

bill = 0
if height >= 120:
    print("can ride")
    if age >= 18:
        bill += 12
    elif age < 12:
        bill += 5
    else:
        bill += 7

else:
    print("can't ride")

want_photo = input("want photo?")
if want_photo == "Y":
   no_photos = int(input("how many photos you want?"))
   if no_photos == 1:
        bill += 3
        print(bill)
   elif no_photos >= 2:
       bill += 4
       print(bill)
else:
    print(bill)
