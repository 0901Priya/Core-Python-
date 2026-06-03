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

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def get_salary(self):
        print("Salary Accessed")
        return self.__salary

    def update_salary(self, new_salary):
        if new_salary > self.__salary:
            self.__salary = new_salary
            print("Salary Updated")
        else:
            print("New salary must be higher")


e = Employee("Ram", 50000)
print(e.get_salary())
e.update_salary(60000)
print(e.get_salary())

class Product:
    def __init__(self, price, discount):
        self.__price = price
        self.__discount = discount

    def get_final_price(self):
        if self.__price < 0:
            return "Invalid Price"

        if self.__discount > 70:
            return "Discount Too High"

        final = self.__price - (self.__price * self.__discount / 100)
        return final


p = Product(1000, 20)
print("Final Price:", p.get_final_price())

class Character:
    def __init__(self, health, max_health):
        self.__health = health
        self.__max_health = max_health

    def damage(self, points):
        self.__health -= points
        if self.__health < 0:
            self.__health = 0

    def heal(self, points):
        self.__health += points
        if self.__health > self.__max_health:
            self.__health = self.__max_health

    def get_health(self):
        return self.__health


c = Character(80, 100)
c.damage(30)
print(c.get_health())
c.heal(50)
print(c.get_health())

class Engine:
    def __init__(self):
        self.__temperature = 30

    def heat(self):
        self.__temperature += 50

    def cool(self):
        self.__temperature -= 20

    def show_temp(self):
        return self.__temperature


class Car:
    def __init__(self):
        self.__engine = Engine()

    def start_car(self):
        self.__engine.heat()
        print("Car Started")

    def cool_engine(self):
        self.__engine.cool()

    def engine_status(self):
        print("Temperature:", self.__engine.show_temp())


c = Car()
c.start_car()
c.engine_status()

class ShoppingCart:
    def __init__(self):
        self.__items = []

    def add_item(self, item):
        self.__items.append(item)

    def remove_item(self, item):
        self.__items.remove(item)

    def get_items(self):
        return self.__items.copy()


cart = ShoppingCart()
cart.add_item("Laptop")
cart.add_item("Mouse")
print(cart.get_items())

# Wrong Design
class BadAttendance:
    def __init__(self):
        self.attendance = []

a = BadAttendance()
a.attendance.append("Fake Entry")
print(a.attendance)


# Correct Design
class GoodAttendance:
    def __init__(self):
        self.__attendance = []

    def mark_attendance(self, name):
        self.__attendance.append(name)

    def show(self):
        print(self.__attendance)


g = GoodAttendance()
g.mark_attendance("Priya")
g.show()

class Person:
    def __init__(self):
        self._age = 0

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value > 0:
            self._age = value
        else:
            print("Invalid Age")


p = Person()
p.age = 21
print(p.age)
p._age = -5
print(p.age)

from abc import ABC, abstractmethod
import math

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return math.pi * self.r * self.r

    def perimeter(self):
        return 2 * math.pi * self.r


class Rectangle(Shape):
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        return self.l * self.b

    def perimeter(self):
        return 2 * (self.l + self.b)


c = Circle(5)
print(c.area())

from abc import ABC, abstractmethod

class PaymentGateway(ABC):

    @abstractmethod
    def authenticate(self):
        pass

    @abstractmethod
    def pay(self, amount):
        pass

    @abstractmethod
    def refund(self, amount):
        pass


class UPIPayment(PaymentGateway):

    def authenticate(self):
        print("UPI Authenticated")

    def pay(self, amount):
        print("Paid", amount, "through UPI")

    def refund(self, amount):
        print("Refunded", amount)


u = UPIPayment()
u.authenticate()
u.pay(500)

from abc import ABC, abstractmethod

class VehicleControl(ABC):

    @abstractmethod
    def accelerate(self):
        pass

    @abstractmethod
    def brake(self):
        pass

    @abstractmethod
    def steer(self):
        pass


class CarControl(VehicleControl):

    def accelerate(self):
        print("Car Accelerating")

    def brake(self):
        print("Car Braking")

    def steer(self):
        print("Car Steering")


c = CarControl()
c.accelerate()
c.brake()

from abc import ABC, abstractmethod

class DatabaseDriver(ABC):

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def execute(self, query):
        pass

    @abstractmethod
    def close(self):
        pass


class MySQLDriver(DatabaseDriver):

    def connect(self):
        print("MySQL Connected")

    def execute(self, query):
        print("Executing:", query)

    def close(self):
        print("Connection Closed")


db = MySQLDriver()
db.connect()
db.execute("SELECT * FROM student")
db.close()

from abc import ABC, abstractmethod

class ReportGenerator(ABC):

    @abstractmethod
    def load_data(self):
        pass

    @abstractmethod
    def process(self):
        pass

    @abstractmethod
    def export(self):
        pass


class PDFReport(ReportGenerator):

    def load_data(self):
        print("Loading Data")

    def process(self):
        print("Processing Data")

    def export(self):
        print("Exporting PDF")


r = PDFReport()
r.load_data()
r.process()
r.export()

from abc import ABC, abstractmethod

class RobotCommand(ABC):

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


class MoveCommand(RobotCommand):

    def execute(self):
        print("Robot Moving")

    def undo(self):
        print("Undo Move")


m = MoveCommand()
m.execute()
m.undo()

from abc import ABC, abstractmethod

class MLModel(ABC):

    @abstractmethod
    def train(self, data):
        pass

    @abstractmethod
    def predict(self, x):
        pass

    @abstractmethod
    def evaluate(self, test):
        pass


class LinearRegressionModel(MLModel):

    def train(self, data):
        print("Training Linear Regression")

    def predict(self, x):
        return x * 2

    def evaluate(self, test):
        print("Evaluating Model")


m = LinearRegressionModel()
m.train([1,2,3])
print(m.predict(5))

from abc import ABC, abstractmethod

class Notifier(ABC):

    @abstractmethod
    def send(self, msg):
        pass


class EmailSender(Notifier):

    def send(self, msg):
        print("Email:", msg)


class SMSSender(Notifier):

    def send(self, msg):
        print("SMS:", msg)


n = EmailSender()
n.send("Hello")

from abc import ABC, abstractmethod

class MediaPlayer(ABC):

    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class MP3Player(MediaPlayer):

    def load(self):
        print("MP3 Loaded")

    def play(self):
        print("Playing MP3")

    def stop(self):
        print("Stopped")


m = MP3Player()
m.load()
m.play()
m.stop()

from abc import ABC, abstractmethod

class Sensor(ABC):

    @abstractmethod
    def read_value(self):
        pass

    @abstractmethod
    def calibrate(self):
        pass


class TemperatureSensor(Sensor):

    def __init__(self):
        self.__raw = 25
        self.__factor = 1.0

    def read_value(self):
        return self.__raw * self.__factor

    def calibrate(self):
        self.__factor = 1.2

    def get_reading(self):
        return self.read_value()


t = TemperatureSensor()
print(t.get_reading())
t.calibrate()
print(t.get_reading())