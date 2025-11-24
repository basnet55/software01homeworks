from car import ElectricCar
from car import  GasolineCar

e_car = ElectricCar("ABC-15", 180, 52.5)
g_car = GasolineCar("ACD-123", 165, 32.3)

e_car.accelerate(120)
g_car.accelerate(140)

e_car.drive(1)
g_car.drive(9)

print("Electric car distance:", e_car.travelled_distance, "km")
print("Gasoline car distance:", g_car.travelled_distance, "km")
