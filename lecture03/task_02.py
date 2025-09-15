class_type = input("Enter your cabin class of the cruise: ").upper()
if class_type == "LUX":
    print("Upper-deck cabin with a balcony.")
elif class_type == "A" :
    print("Cabin above the car deck with a window.")
elif class_type == "B":
    print("Windowless cabin above the car deck.")
elif class_type == "C":
    print("Windowless cabin below the car deck.")
else:
    print("Invalid cabin class.")