import math


def unit_price(diameter, price):
    radius = (diameter / 100) / 2
    area = math.pi * radius ** 2
    return price / area


print("Pizza 1:")
d1 = float(input("Enter diameter (cm): "))
p1 = float(input("Enter price (€): "))


print("\nPizza 2:")
d2 = float(input("Enter diameter (cm): "))
p2 = float(input("Enter price (€): "))


u1 = unit_price(d1, p1)
u2 = unit_price(d2, p2)


print(f"\nPizza 1 unit price: {u1:.2f} €/m²")
print(f"Pizza 2 unit price: {u2:.2f} €/m²")


if u1 < u2:
    print("Pizza 1 is cheaper per square meter.")
elif u2 < u1:
    print("Pizza 2 is cheaper per square meter")
else:
    print("Both pizzas cost the same per square meter.")
