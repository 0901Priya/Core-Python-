class A:
    def m1(self):
        print("A class")
class B(A):
    def m1(self):
        print("B class")
        super().m1()
b1=B()
b1.m1()
a1=A()
a1.m1()


class A:
    def m1(self):
        super().m1()
        print("A class")
class B:
    def m1(self):
        super().m1()
        print("B class")
class C:
    def m1(self):
        # super().m1()
        print("C class")
class D(A,B,C):
    def m1(self):
        super().m1()
        print("D class")
d1=D()
d1.m1()
a1=A()
# a1.m1()

class A:
    x=0
    def m1(self):
        print("A class")
class B(A):
    pass
b1=B()

class A:
    x=0
    def m1(self):
        print("A class")
class B(A):
    pass
class C:
    def m1(self):
        a1=A()
        a1.m1()
c1=C()
c1.m1()

class B:
    def m1(self):
        print("B class")
    @classmethod
    def m2(cls):
        cls().m1()
    print("class Method")

# Q1 Student Pass or Fail

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        return self.marks > 40


s1 = Student("Ram", 75)
s2 = Student("Hari", 30)

print(s1.name, "Passed" if s1.is_passed() else "Failed")
print(s2.name, "Passed" if s2.is_passed() else "Failed")

# Q2 Employee Company Change

class Employee:

    company_name = "TechCorp"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_company(cls, new_name):
        cls.company_name = new_name


e1 = Employee("Ram")
e2 = Employee("Hari")

print(e1.company_name)
print(e2.company_name)

Employee.change_company("Infosys")

print(e1.company_name)
print(e2.company_name)

# Q3 MathOps Static Method

class MathOps:

    @staticmethod
    def is_even(num):
        return num % 2 == 0


print(MathOps.is_even(10))

m = MathOps()
print(m.is_even(7))

# Q4 Car Specifications

class Car:

    wheels = 4

    def __init__(self, mileage):
        self.mileage = mileage

    def display_specs(self):
        print("Mileage:", self.mileage)
        print("Wheels:", Car.wheels)

    @classmethod
    def change_wheels(cls, num):
        cls.wheels = num


c1 = Car(25)

c1.display_specs()

Car.change_wheels(6)

c1.display_specs()

# Q5 Temperature Conversion

class Temperature:

    def __init__(self, celsius):
        self.celsius = celsius

    @staticmethod
    def to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

    def show_conversion(self):
        print("Celsius:", self.celsius)
        print("Fahrenheit:", Temperature.to_fahrenheit(self.celsius))


t = Temperature(37)
t.show_conversion()

# Q6 Book Class

class Book:

    total_books = 0

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.total_books += 1

    @classmethod
    def from_string(cls, book_str):
        title, author = book_str.split("-")
        return cls(title, author)

    @staticmethod
    def is_valid_title(title):
        return len(title) >= 3


if Book.is_valid_title("Python"):
    b1 = Book("Python", "ABC")

b2 = Book.from_string("Java-XYZ")

print(b1.title, b1.author)
print(b2.title, b2.author)
print("Total Books:", Book.total_books)

# Q7 Employee Bonus System

class Employee:

    bonus_rate = 0.1

    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def final_salary(self):
        return self.base_salary + (self.base_salary * Employee.bonus_rate)

    @classmethod
    def update_bonus(cls, new_rate):
        cls.bonus_rate = new_rate

    @staticmethod
    def is_valid_salary(sal):
        return sal > 0


e1 = Employee("Ram", 30000)
e2 = Employee("Hari", 40000)

print(e1.final_salary())
print(e2.final_salary())

Employee.update_bonus(0.2)

print(e1.final_salary())
print(e2.final_salary())

# Q8 Course Enrollment

class Course:

    total_students = 0

    def __init__(self, student_name):
        self.student_name = student_name

    def enroll(self):
        Course.total_students += 1

    @classmethod
    def show_total(cls):
        print("Total Students:", cls.total_students)

    @staticmethod
    def is_eligible(age):
        return age >= 18


c1 = Course("Ram")
c2 = Course("Hari")

c1.enroll()
c2.enroll()

Course.show_total()

print(Course.is_eligible(20))

# Q9 BankAccount Transactions

class BankAccount:

    bank_name = "SBI"

    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        if BankAccount.validate_amount(amount):
            self.balance += amount

    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name

    @staticmethod
    def validate_amount(amount):
        return amount > 0


b1 = BankAccount("Ram", 5000)

b1.deposit(2000)

print(b1.holder)
print(b1.balance)
print(BankAccount.bank_name)

BankAccount.change_bank_name("HDFC")

print(BankAccount.bank_name)

# Q10 Student Result System

class Student:

    passing_marks = 40

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def result(self):
        if self.marks >= Student.passing_marks:
            print(self.name, "Passed")
        else:
            print(self.name, "Failed")

    @classmethod
    def update_passing_marks(cls, new_marks):
        cls.passing_marks = new_marks

    @staticmethod
    def grade_category(marks):
        if marks >= 90:
            return "A"
        elif marks >= 70:
            return "B"
        else:
            return "C"


s1 = Student("Ram", 80)
s2 = Student("Hari", 35)

s1.result()
s2.result()

Student.update_passing_marks(30)

s2.result()

print(Student.grade_category(95))
print(Student.grade_category(75))
print(Student.grade_category(50))
