def gallons_to_liters(gallons):
    return gallons * 3.78541  # Convert gallons to liters

while True:
    gallons = float(input("Enter gallons (negative number to quit): "))
    if gallons < 0:
        print("Goodbye!")
        break
    liters = gallons_to_liters(gallons)
    print(f"{gallons} gallons = {liters:.2f} liters\n")