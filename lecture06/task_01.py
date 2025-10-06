months_of_the_year = ("January","February","March","April", "May", "June", "July", "August", "September", "October", "November", "December")
month_number = int(input("Enter the month number (1-12):"))
month = months_of_the_year[month_number-1]
if month_number  in (2, 3, 4):
    print(f"Month {month_number}  {month} is spring.")
elif month_number in (5 , 6,7):
    print(f"Month {month_number}  {month} is summer.")
elif month_number in (8, 9, 10):
    print(f"Month {month_number}  {month} is autumn.")
else:
    print(f"Month {month_number}  {month} is winter.")