def sum_list(numbers):
    return sum(numbers)

user_input = input("Enter numbers separated by spaces: ")

numbers = []
for num in user_input.split():
    numbers.append(int(num))

total = sum_list(numbers)

print("Numbers in the list:", numbers)
print("Sum of the numbers:", total)
