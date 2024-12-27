print("Welcome to the rollercoaster")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Please pay $5.")
    elif age <= 18:
        bill = 7
        print("Please pay $7.")
    elif age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        bill = 12
        print("Please pay $12.")

    wants_photo = input("Di you want to have a photo take? Type y for Yes and n for No. ")
    if wants_photo == "y":
        # Add $3 to their bill
        bill += 3
    
    print(f"Your final bill is ${bill}")


else:
    print("Sorry you have to grow taller before you can ride.")