smallest = None
largest = None

while True:
    user_input = input("Enter a number (leave blank to stop): ")

    if user_input == "":
        break

    number = float(user_input)

    if smallest is None or number < smallest:
        smallest = number
    if largest is None or number > largest:
        largest = number


print("Smallest number entered:", smallest)
print("Largest number entered:", largest)