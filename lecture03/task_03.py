gender = input("Enter your gender: ").lower()
hemoglobin_level = float(input("Enter your hemoglobin level (g/L): "))
if gender == "female":
    if hemoglobin_level <117:
        print("Your hemoglobin level is low.")
    elif hemoglobin_level <= 155:
        print("Your hemoglobin level is normal.")
    else:
        print("Your hemoglobin level is high")
if gender == "male":
    if hemoglobin_level < 134:
        print("Your hemoglobin level is low.")
    elif hemoglobin_level <= 167:
        print("Your hemoglobin level is normal.")
    else:
        print("Your hemoglobin level is high")