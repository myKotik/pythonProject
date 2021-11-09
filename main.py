# Python Math & Time Modules
import math
import time

# Intro
print("Welcome to the Temperature Conventer. Type C for Celsuis, F for Fahreinheit and K for Kelvin")

def again():
    try_again = print()
    user_temp = input("your temperature | C | F | K | ").upper()
    convert_temp = input("The temperature you want to convert to | C | F | K | ").upper()

    if convert_temp == "C":
        if user_temp == "C":
            print(f"Это ваша температура{user_temp}")
        if user_temp == "F":
            degree = float(input("enter the degree: "))
            result = (degree * 9 / 5) + 32
            print(f"{result}")
        if user_temp == "K":
            degree = float(input("enter the degree: "))
            result = degree + 273.15
            print(f"{result}")
            time.sleep(1)
            again()
        else:
            print("Type a temperature")
            time.sleep(1)
            again()


    elif user_temp == "F":
        if convert_temp == "C":
            degree = float(input("enter the degree: "))
            result = (degree - 32) * 5 / 9
            print(f"{result}")
        elif convert_temp == "K":
            degree = float(input("enter the degree: "))
            result = (degree - 32) * 5 / 9 + 273.15
            print(f"{result}")
        elif convert_temp == "F":
            print("This is the same type of temperature")
            time.sleep(1)
            again()
        else:
            print("Type a temperature")
            time.sleep(1)
            again()

    elif user_temp == "K":
        if convert_temp == "C":
            degree = float(input("enter the degree: "))
            result = degree - 273.15
            print(f"{result}")
        elif convert_temp == "F":
            degree = float(input("enter the degree: "))
            result = (degree - 273.15) * 9 / 5 + 32
            print(f"{result}")
        elif convert_temp == "K":
            print("This is the same type of temperature")
            time.sleep(1)
            again()
        else:
            print("Type a temperature")
            time.sleep(1)
            again()

    else:
        print("Type a temperature")
        time.sleep(1)
        again()

    # Aking if the user wants to convert again
    while try_again != "Yes" and try_again != "No":
        print("\nDo you want to try again?")
        try_again = input("Yes | No | ").lower().capitalize()
        if try_again == "Yes":
            again()
            break
        elif try_again == "No":
            print("Goodbye")
            break


again()