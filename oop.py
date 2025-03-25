# OOP is nothing but a collection of interrelated variables and fuctions
# variable refer to properties of objects whereas function refer to as behaviors
# class is a blueprint for creating objects
# objects are instances of class


class Car:
    def __init__(self, model, color, company, speed_limit):
        self.model = model
        self.color = color
        self.company = company
        self.speed_limit = speed_limit

    def start(self):
        print("started")

    def stop(self):
        print("stopped")

    def accelarate(self):
        print("accelarating")

    def change_gear(self):
        print("gear changed")
        
# Inheritance

class ElectricCar(Car):
    # Encapusaltion
    def __init__(self, model, color, company, speed_limit, battery_capacity):
        super().__init__(model, color, company, speed_limit)
        self.battery_capacity = battery_capacity
    def start(self):
        print("started")
        print("battery capacity is ", self.battery_capacity)    

# Not a single instance of a class or object is complete without 
# all four fundamentals OOP 
# 1. Encapsulation - encapsulating data and functions into a single unit
# 2. Abstraction - hiding the complexicity of the system
# 3. Inheritance - inheriting the properties of parent class
# 4. Polymorphism - ability to take multiple forms        
    