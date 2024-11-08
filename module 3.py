#Bella Carman
#Module 3
# Accepts user input on vehicle information and prints out input information
# Super class
class Vehicle:
    def __init__(self):
        self.vehicle_type = "car"
# Sub class 
class Automobile(Vehicle):
    def __init__(self):
        super().__init__()
        self.year = ""
        self.make = ""
        self.model = ""
        self.doors = ""
        self.roof = ""
       
A = Automobile()

A.year = input("What year is your car? ")
A.make = input("What is the make of your car? ")
A.model = input("What is the model is your car? ")
A.doors = input("How many doors do your car have (2 or 4)? ")
A.roof = input("Does your car have a solid or sunroof? ")

print("Vehicle type: " + A.vehicle_type)
print("Vehicle year: " + A.year)
print("Vehicle make: " + A.make)
print("Vehicle model: " + A.model)
print("Vehicle doors: " + A.doors)
print("Vehicle roof: " + A.roof)