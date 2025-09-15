requiredlength = 42
length = float(input("The length of a zanderin: "))
shorterthan= requiredlength - length
if length < requiredlength:
    print(f"Please release it back into the lake. It is {shorterthan:.2f} cm shorter than the required length.")
else:
    print("You can keep the fish.")