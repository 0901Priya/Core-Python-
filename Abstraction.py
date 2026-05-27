class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount
    def __str__(self):
        return f"{self.account_holder} : {self.balance}"
    def __add__(self, other):
        return self.balance + other.balance
    def __sub__(self, other):
        return self.balance - other.balance
    def __eq__(self, other):
        return self.balance == other.balance
    def __lt__(self, other):
        return self.balance < other.balance
    def __getattribute__(self, name):
        print(f"Accessing {name}")
        return object.__getattribute__(self, name)
    def __setattr__(self, name, value):
        if name == "balance" and value < 0:
            print("Negative balance not allowed")
        else:
            object.__setattr__(self, name, value)

a1 = BankAccount("Jhansi", 5000)
a2 = BankAccount("Rani", 3000)

print(a1)
print(a1 + a2)
print(a1 - a2)
print(a1 == a2)
print(a1 < a2)

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def total_price(self):
        return self.price * self.quantity
    def __str__(self):
        return f"{self.name} : {self.total_price()}"
    def __add__(self, other):
        return self.total_price() + other.total_price()
    def __mul__(self, n):
        return self.price * n
    def __gt__(self, other):
        return self.total_price() > other.total_price()
    def __eq__(self, other):
        return self.price == other.price
    def __getattr__(self, name):
        return "Attribute not found"
    def __setattr__(self, name, value):
        if name == "price" and value < 0:
            print("Invalid price")
        else:
            object.__setattr__(self, name, value)

p1 = Product("Pen", 20, 5)
p2 = Product("Book", 50, 2)

print(p1)
print(p1 + p2)
print(p1 * 3)
print(p1 > p2)
print(p1 == p2)

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def grade(self):
        if self.marks >= 90:
            return "A"
        else:
            return "B"
    def __str__(self):
        return f"{self.name} : {self.marks}"
    def __add__(self, other):
        return self.marks + other.marks
    def __truediv__(self, n):
        return self.marks / n
    def __ge__(self, other):
        return self.marks >= other.marks
    def __lt__(self, other):
        return self.marks < other.marks
    def __getattribute__(self, name):
        print(f"Accessing {name}")
        return object.__getattribute__(self, name)
    def __setattr__(self, name, value):
        if name == "marks" and (value < 0 or value > 100):
            print("Invalid marks")
        else:
            object.__setattr__(self, name, value)

s1 = Student("A", 90)
s2 = Student("B", 80)

print(s1)
print(s1 + s2)
print(s1 / 2)
print(s1 >= s2)
print(s1 < s2)

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length * self.breadth
    def __str__(self):
        return f"Area = {self.area()}"
    def __add__(self, other):
        return self.area() + other.area()
    def __sub__(self, other):
        return self.area() - other.area()
    def __eq__(self, other):
        return self.area() == other.area()
    def __gt__(self, other):
        return self.area() > other.area()
    def __getattr__(self, name):
        return "Attribute not found"
    def __setattr__(self, name, value):
        if value <= 0:
            print("Must be positive")
        else:
            object.__setattr__(self, name, value)

r1 = Rectangle(4, 5)
r2 = Rectangle(2, 6)

print(r1)
print(r1 + r2)
print(r1 - r2)
print(r1 == r2)
print(r1 > r2)

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def annual_salary(self):
        return self.salary * 12
    def __str__(self):
        return f"{self.name} : {self.salary}"
    def __add__(self, other):
        return self.salary + other.salary
    def __mul__(self, months):
        return self.salary * months
    def __ne__(self, other):
        return self.salary != other.salary
    def __le__(self, other):
        return self.salary <= other.salary
    def __getattribute__(self, name):
        print(f"Accessing {name}")
        return object.__getattribute__(self, name)
    def __setattr__(self, name, value):
        if name == "salary" and value < 10000:
            print("Salary too low")
        else:
            object.__setattr__(self, name, value)

e1 = Employee("Ram", 20000)
e2 = Employee("Sam", 25000)

print(e1)
print(e1 + e2)
print(e1 * 12)
print(e1 != e2)
print(e1 <= e2)

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def reading_time(self):
        return self.pages * 2
    def __str__(self):
        return f"{self.title} by {self.author}"
    def __add__(self, other):
        return self.pages + other.pages
    def __floordiv__(self, days):
        return self.pages // days
    def __gt__(self, other):
        return self.pages > other.pages
    def __eq__(self, other):
        return self.title == other.title
    def __getattr__(self, name):
        return "No attribute"
    def __setattr__(self, name, value):
        if name == "title" and value == "":
            print("Title empty")
        elif name == "pages" and value <= 0:
            print("Invalid pages")
        else:
            object.__setattr__(self, name, value)

b1 = Book("Python", "ABC", 200)
b2 = Book("Java", "XYZ", 150)

print(b1)
print(b1 + b2)
print(b1 // 5)
print(b1 > b2)
print(b1 == b2)

class CartItem:
    def __init__(self, item_name, price, quantity):
        self.item_name = item_name
        self.price = price
        self.quantity = quantity
    def final_amount(self):
        return self.price * self.quantity
    def __str__(self):
        return f"{self.item_name} : {self.final_amount()}"
    def __add__(self, other):
        return self.final_amount() + other.final_amount()
    def __mod__(self, discount):
        return self.final_amount() % discount
    def __lt__(self, other):
        return self.final_amount() < other.final_amount()
    def __ge__(self, other):
        return self.quantity >= other.quantity
    def __getattribute__(self, name):
        print(f"Accessing {name}")
        return object.__getattribute__(self, name)
    def __setattr__(self, name, value):
        if name == "quantity" and value < 1:
            print("Invalid quantity")
        else:
            object.__setattr__(self, name, value)

c1 = CartItem("Bag", 500, 2)
c2 = CartItem("Bottle", 200, 3)

print(c1)
print(c1 + c2)
print(c1 % 100)
print(c1 < c2)
print(c1 >= c2)

class TimeDuration:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes
    def total_minutes(self):
        return self.hours * 60 + self.minutes
    def __str__(self):
        return f"{self.hours}h {self.minutes}m"
    def __add__(self, other):
        return self.total_minutes() + other.total_minutes()
    def __sub__(self, other):
        return self.total_minutes() - other.total_minutes()
    def __eq__(self, other):
        return self.total_minutes() == other.total_minutes()
    def __gt__(self, other):
        return self.total_minutes() > other.total_minutes()
    def __getattr__(self, name):
        return "Invalid attribute"
    def __setattr__(self, name, value):
        if name == "minutes" and (value < 0 or value > 59):
            print("Invalid minutes")
        else:
            object.__setattr__(self, name, value)

t1 = TimeDuration(2, 30)
t2 = TimeDuration(1, 45)

print(t1)
print(t1 + t2)
print(t1 - t2)
print(t1 == t2)
print(t1 > t2)

class Laptop:
    def __init__(self, brand, ram, price):
        self.brand = brand
        self.ram = ram
        self.price = price
    def upgrade_ram(self, extra_ram):
        self.ram += extra_ram
    def __str__(self):
        return f"{self.brand} : {self.price}"
    def __add__(self, other):
        return self.price + other.price
    def __mul__(self, n):
        return self.price * n
    def __lt__(self, other):
        return self.price < other.price
    def __eq__(self, other):
        return self.ram == other.ram
    def __getattribute__(self, name):
        print(f"Accessing {name}")
        return object.__getattribute__(self, name)
    def __setattr__(self, name, value):
        if (name == "ram" or name == "price") and value <= 0:
            print("Invalid value")
        else:
            object.__setattr__(self, name, value)

l1 = Laptop("Dell", 8, 50000)
l2 = Laptop("HP", 16, 60000)

print(l1)
print(l1 + l2)
print(l1 * 2)
print(l1 < l2)
print(l1 == l2)

class Player:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, enemy):
        enemy.health -= self.attack_power

    def __str__(self):
        return f"{self.name} : {self.health}"

    def __add__(self, other):
        return self.attack_power + other.attack_power
    def __sub__(self, damage):
        return self.health - damage
    def __gt__(self, other):
        return self.health > other.health
    def __eq__(self, other):
        return self.attack_power == other.attack_power
    def __getattr__(self, name):
        return "Stat not found"
    def __setattr__(self, name, value):
        if name == "health" and value < 0:
            print("Health cannot be negative")
        else:
            object.__setattr__(self, name, value)

p1 = Player("Hero", 100, 20)
p2 = Player("Enemy", 80, 15)

print(p1)
print(p1 + p2)
print(p1 - 10)
print(p1 > p2)
print(p1 == p2)