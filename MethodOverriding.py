#Exercise
#submit your work to github for method overriding, method overloading and MRO
#MRO is Method Resolution Order.
# Two real world examples are neede for the above concepts. 

# 1.Method overriding
# Real World Example: Vehicle Movement
class Vehicle:
    def __init__(self, name):
        self.name = name

    def move(self):
        return "Generic movement"

class Car(Vehicle):
    def move(self):
        return "Driving on the road"

class Bicycle(Vehicle):
    def move(self):
        return "Pedaling along the path"

class Airplane(Vehicle):
    def move(self):
        return "Flying through the air"

# Create instances of each vehicle type
car = Car("Sedan")
bicycle = Bicycle("Mountain Bike")
airplane = Airplane("Boeing 747")

# Call the move() method on each object
print(f"{car.name} is {car.move()}")
print(f"{bicycle.name} is {bicycle.move()}")
print(f"{airplane.name} is {airplane.move()}")