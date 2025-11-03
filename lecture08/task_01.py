class Car:
    def __init__(self, registration_number, maximum_speed, current_speed =0 , travelled_distance=0):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance

NewCar= Car("ABC-123",142)

print("Car details:")
print(f"Registration Number: {NewCar.registration_number}")
print(f"Maximum Speed: {NewCar.maximum_speed} km/h")
print(f"Current Speed: {NewCar.current_speed} km/h")
print(f"Travelled Distance: {NewCar.travelled_distance} km")
