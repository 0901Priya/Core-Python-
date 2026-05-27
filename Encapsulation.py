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

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = 0
        self.update_marks(marks)
    def update_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid Marks")
    def display(self):
        print(self.name, self.__marks)

s = Student("Priya", 85)
s.update_marks(95)
s.display()
s.__marks = 200
s.display()

class SecureFile:
    def __init__(self, content, password):
        self.__content = content
        self.__password = password
        self.__log = []
    def read(self, password):
        if password == self.__password:
            return self.__content
        else:
            self.__log.append("Unauthorized attempt")
            return "Access Denied"
f = SecureFile("Secret Data", "1234")
print(f.read("111"))
print(f.read("1234"))

