'''
Author: Samuel Ragsdale
Date: 11/08/2024
Description: This is a program that has two classes, Vehicle and Automobile. Vehicle is a super
class of Automobile. Automobile takes the arguments of Vehicle and adds its own. Finally the program
will ask the user for inputs and add those inputs to a list which will then be passed as arguments
for an Automobile class instantiation. Finally it prints out the user inputs as the various attributes
of the input.
'''

class Vehicle:
    '''Vehicle class has the type argument only'''
    def __init__(self, type):
        self.type = type


class Automobile(Vehicle):
    '''Automobile class takes arguments (type) from the Vehicle class and adds other
    arguments for year, make, model, # of doors and roof'''
    def __init__(self, type, year, make, model, doors, roof):
        super().__init__(type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

'''empty list is initialized'''
userCarList = []

'''Inputs for the userCarList that will ultimately be passed to an instance of Automobile class'''
userCarType = userCarList.append(input("What type of car do you drive? "))
userCarYear = userCarList.append(input("What year is your car? "))
userCarMake = userCarList.append(input("What is the make of your car? "))
userCarModel = userCarList.append(input("What is the model of your car? "))
userCarDoors = userCarList.append(input("How many doors does your car have? "))
userCarRoof = userCarList.append(input("What type of roof does your car have? "))

userCar = Automobile(*userCarList) #passes the list elements of userCarList as arguments for an Automobile class instance

'''Print out of the various attributes of the inputs the user just provided'''
print(f"Your car has the following attributes\n"
f"Vehicle type: {userCar.type}\n"
f"Vehicle year: {userCar.year}\n"
f"Vehicle make: {userCar.make}\n"
f"Vehicle model: {userCar.model}\n"
f"Number of doors: {userCar.doors}\n"
f"Type of roof: {userCar.roof}")
