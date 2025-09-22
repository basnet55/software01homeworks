cm_in_inches = 2.54

while True:
    inch = float(input("Enter length in inches (negative to stop): "))

    if inch < 0:
        print("Program stopped.")
        break

    cm = inch * cm_in_inches
    print(f"{inch} inches is {cm:.2f} centimeters")
