def remove_odd_numbers(numbers):
    return [n for n in numbers if n % 2 == 0]

user_input = input("Enter numbers separated by spaces: ")

numbers = []
for num in user_input.split():
    numbers.append(int(num))

even_numbers = remove_odd_numbers(numbers)

print("Original list:", numbers)
print("Even numbers only:", even_numbers)