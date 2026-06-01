class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder=account_holder
        self.balance=balance
    def deposit(self,amount):
        self.balance=self.balance+amount
    def withdraw(self,amount):
        self.balace=self.balance-amount
    def __str__(self):
        return f"{self.account_holder}:{self.balance}"
    def __add__(self,o2):
        return self.balance+o2.balance
    def __sub__(self,o2):
        return self.balance-o2.balance
    def __eq__(self,o2):
        return self.balance==o2.balance
    def __lt__(self,o2):
        return self.balance<o2.balance
    def __getattribute__(self, name):
        print(f"Accessing {name}")
        return object.__getattribute__(self,name)
    def __setattr__(self, name, value):
        if name=="balance" and  value<0 :
            print("Negative balance are not allowed")
        else:
            return object.__setattr__(self,name,value)
b1=BankAccount("Viha", 10000)
b2=BankAccount("shanti",5000)
print(b1)
print(b2)
print(b1+b2)
print(b1-b2)
print(b1==b2)
print(b1<b2)

class Product:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def total_price(self):
        return self.price * self.quantity
    def __str__(self):
        return f"{self.name} : {self.total_price()}"
    def __add__(self, o2):
        return self.total_price() + o2.total_price()
    def __mul__(self, num):
        return self.price * num
    def __gt__(self, o2):
        return self.total_price() > o2.total_price()
    def __eq__(self, o2):
        return self.price == o2.price
    def __getattr__(self, name):
        return "Attribute not found"
    def __setattr__(self, name, value):
        if name == "price" and value < 0:
            print("Invalid price")
        else:
            object.__setattr__(self, name, value)



p1=Product("Pen", 20,5)
p2=Product("Book",50,3)
print(p1)
print(p1+p2)
print(p1*9)
print(p1>p2)
print(p1==p2)

class Student:
    def __init__(self, name, marks):
        self.name=name
        self.marks=marks
    def grade(self):
        return self.marks/100
    def __str__(self):
        return f"{self.name} : {self.grade()}"
    def __add__(self, o2):
        return self.marks + o2.marks
    def __truediv__(self,num):
        return self.marks / num
    def __ge__(self, o2):
        return self.marks>=o2.marks
    def __lt__(self, o2):
        return self.marks<o2.marks
    def __getattribute__(self, name):
        print(f"Accessing {name}")
        return object.__getattribute__(self,name)
    def __setattr__(self, name, value):
        if name=="marks" and (value < 0 or value > 100):
            print("Invalid marks")
        else:
            return object.__setattr__(self,name,value)
s1=Student("yogi", 80)
s2=Student("Ammu", 100)
print(s1)
print(s2)
print(s1+s2)
print(s1/2)
print(s1>=s2)
print(s1<s2)
