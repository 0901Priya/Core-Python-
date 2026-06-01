
# Q1 Student Class

class Student:

    total_students = 0
    passing_marks = 40

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        Student.total_students += 1

    def result(self):
        return "Pass" if self.marks >= Student.passing_marks else "Fail"

    def curve_marks(self, percent):
        self.marks += self.marks * percent / 100

    @staticmethod
    def grade(mark):
        if mark >= 90:
            return "A"
        elif mark >= 75:
            return "B"
        elif mark >= 50:
            return "C"
        else:
            return "D"


s1 = Student("Ram", 70)
s2 = Student("Hari", 35)

s1.curve_marks(10)
s2.curve_marks(20)

print(s1.name, s1.marks, s1.result(), Student.grade(s1.marks))
print(s2.name, s2.marks, s2.result(), Student.grade(s2.marks))
print("Total Students:", Student.total_students)

# Q2 Product Class

class Product:

    tax_rate = 10

    def __init__(self, name, base_price):
        self.name = name
        self.base_price = base_price

    def final_price(self):
        return self.base_price + (self.base_price * Product.tax_rate / 100)

    @classmethod
    def change_tax(cls, rate):
        cls.tax_rate = rate

    @staticmethod
    def valid_price(price):
        return price >= 0 and price <= 100000


p1 = Product("Laptop", 50000)
p2 = Product("Phone", 20000)

print(p1.final_price())
print(p2.final_price())

Product.change_tax(18)

print(p1.final_price())
print(Product.valid_price(500))

# Q3 Employee Class

class Employee:

    min_experience = 5

    def __init__(self, name, experience, department):
        self.name = name
        self.experience = experience
        self.department = department

    def promotion(self):
        return self.experience >= Employee.min_experience

    @classmethod
    def update_criteria(cls, exp):
        cls.min_experience = exp

    @staticmethod
    def valid_department(dep):
        return dep in ["HR", "Tech", "Admin"]


e1 = Employee("Ram", 6, "Tech")
e2 = Employee("Hari", 3, "HR")

print(e1.promotion())
print(e2.promotion())

Employee.update_criteria(2)

print(e2.promotion())
print(Employee.valid_department("Admin"))

# Q4 Loan Class

class Loan:

    interest_rate = 8

    def __init__(self, borrower, principal):
        self.borrower = borrower
        self.principal = principal

    def total_payable(self):
        return self.principal + (self.principal * Loan.interest_rate / 100)

    @classmethod
    def update_interest(cls, rate):
        cls.interest_rate = rate

    @staticmethod
    def check_eligibility(salary):
        return salary > 25000


l1 = Loan("Ram", 100000)
l2 = Loan("Hari", 200000)

print(l1.total_payable())

Loan.update_interest(10)

print(l2.total_payable())
print(Loan.check_eligibility(30000))

# Q5 Course Class

class Course:

    total_courses = 0
    min_duration = 1

    def __init__(self, title, duration, enrolled_students):
        self.title = title
        self.duration = duration
        self.enrolled_students = enrolled_students
        Course.total_courses += 1

    def enroll(self):
        self.enrolled_students += 1

    @classmethod
    def update_duration(cls, duration):
        cls.min_duration = duration

    @staticmethod
    def valid_duration(duration):
        return duration > 0 and duration < 100


c1 = Course("Python", 3, 20)
c2 = Course("Java", 6, 15)

c1.enroll()

print(c1.enrolled_students)

Course.update_duration(2)

print(Course.min_duration)
print(Course.valid_duration(5))

# Q6 Vehicle Class

class Vehicle:

    service_rate = 5

    def __init__(self, model, kilometers_run, service_history):
        self.model = model
        self.kilometers_run = kilometers_run
        self.service_history = service_history

    def service_charge(self):
        return self.kilometers_run * Vehicle.service_rate

    @classmethod
    def update_rate(cls, rate):
        cls.service_rate = rate

    @staticmethod
    def eligible(year):
        return 2026 - year <= 15


v1 = Vehicle("Swift", 10000, ["Oil Change"])
v2 = Vehicle("BMW", 20000, ["Brake Service"])

print(v1.service_charge())

Vehicle.update_rate(7)

print(v2.service_charge())
print(Vehicle.eligible(2015))

# Q7 Inventory Class

class Inventory:

    total_items = 0
    min_threshold = 5

    def __init__(self):
        self.stock = {}

    def add_stock(self, item, qty):
        self.stock[item] = self.stock.get(item, 0) + qty
        Inventory.total_items += qty

    def remove_stock(self, item, qty):
        if item in self.stock:
            self.stock[item] -= qty
            Inventory.total_items -= qty

    @classmethod
    def update_threshold(cls, value):
        cls.min_threshold = value

    @staticmethod
    def below_threshold(stock):
        return stock < Inventory.min_threshold


i1 = Inventory()
i2 = Inventory()

i1.add_stock("Pen", 10)
i2.add_stock("Book", 3)

print(i1.stock)
print(i2.stock)

Inventory.update_threshold(4)

print(Inventory.below_threshold(3))

# Q8 HotelRoom Class

class HotelRoom:

    base_price = 2000

    def __init__(self, room_number, nights_booked, guest_name):
        self.room_number = room_number
        self.nights_booked = nights_booked
        self.guest_name = guest_name

    def total_bill(self):
        return self.nights_booked * HotelRoom.base_price

    @classmethod
    def update_price(cls, price):
        cls.base_price = price

    @staticmethod
    def valid_nights(nights):
        return isinstance(nights, int) and nights > 0


r1 = HotelRoom(101, 3, "Ram")
r2 = HotelRoom(102, 5, "Hari")

print(r1.total_bill())

HotelRoom.update_price(3000)

print(r2.total_bill())
print(HotelRoom.valid_nights(4))

# Q9 LibraryMember Class

class LibraryMember:

    total_members = 0
    borrow_limit = 3

    def __init__(self, name):
        self.name = name
        self.books_borrowed = 0
        LibraryMember.total_members += 1

    def borrow_book(self):
        if self.books_borrowed < LibraryMember.borrow_limit:
            self.books_borrowed += 1
            print("Book Borrowed")
        else:
            print("Limit Reached")

    @classmethod
    def update_limit(cls, limit):
        cls.borrow_limit = limit

    @staticmethod
    def valid_title(title):
        return isinstance(title, str) and len(title) > 0 and len(title) < 30


m1 = LibraryMember("Ram")
m2 = LibraryMember("Hari")

m1.borrow_book()
m1.borrow_book()

LibraryMember.update_limit(5)

m2.borrow_book()

print(LibraryMember.valid_title("Python"))

# Q10 Member BMI Class

class Member:

    bmi_limit = 25

    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    def bmi(self):
        return self.weight / (self.height ** 2)

    def fit_status(self):
        return "Fit" if self.bmi() <= Member.bmi_limit else "Unfit"

    @classmethod
    def update_bmi_limit(cls, limit):
        cls.bmi_limit = limit

    @staticmethod
    def valid_data(height, weight):
        return height > 0 and weight > 0


m1 = Member("Ram", 1.7, 65)
m2 = Member("Hari", 1.6, 80)

print(m1.bmi(), m1.fit_status())
print(m2.bmi(), m2.fit_status())

Member.update_bmi_limit(30)

print(m2.fit_status())
print(Member.valid_data(1.8, 70))

