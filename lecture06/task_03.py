airports = {}

while True:
    print("\nChoose an option:")
    print("1. Enter a new airport")
    print("2. Fetch information of an existing airport")
    print("3. Quit the program")

    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == "1":
        icao = input("Enter the ICAO code: ").upper()
        name = input("Enter the airport name: ")

        airports[icao] = name
        print(f"Airport '{name}' with ICAO code '{icao}' added successfully!")

    elif choice == "2":
        icao = input("Enter the ICAO code: ").upper()
        if icao in airports:
            print(f"The airport name for '{icao}' is: {airports[icao]}")
        else:
            print("Airport not found!")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")