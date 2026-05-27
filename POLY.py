class Animal:
    def make_sound(self):
        print("Making sound")
class Dog:
    def make_sound(self):
        print("Bow Bow")
class Cat:
    def make_sound(self):
        print("Meow Meow")
class Cow:
    def make_sound(self):
        print("Mooo Mooo")

Animal=[Dog(),Cat(),Cow()]
for i in Animal:
    i.make_sound()


def operate(device):
    device.start()
class Car:
    def start(self):
        print("Car")
class Computer:
    def start(self):
        print("Computer")
class WashingMachine:
    def start(self):
        print("WashingMachine")
operate(Car())
operate(Computer())
operate(WashingMachine())

class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self, o2):
        return self.x+o2.x,self.y+o2.y
    def __eq__(self, o2):
        return self.x==o2.x and self.y==o2.y

V1=Vector(3,4)
V2=Vector(3,4)
print(V1+V2)
print(V1==V2)
