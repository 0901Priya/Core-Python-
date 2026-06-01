# 1) Add Before & After Messages

def decorator1(func):
    def wrapper():
        print("Start")
        func()
        print("End")
    return wrapper

@decorator1
def hello():
    print("Hello")

hello()


# 2) Decorator With Input (Parameters)

def decorator2(func):
    def wrapper(name):
        print("Starting...")
        func(name)
        print("Done")
    return wrapper

@decorator2
def greet(name):
    print("Hello", name)

greet("Ravi")


# 3) Result Doubler

def doubler(func):
    def wrapper():
        return func() * 2
    return wrapper

@doubler
def num():
    return 25

print(num())


# 4) Admin Access Check

user_role = "student"

def admin_check(func):
    def wrapper():
        if user_role == "admin":
            func()
        else:
            print("Access Denied")
    return wrapper

@admin_check
def dashboard():
    print("Welcome Admin")

dashboard()


# 5) Uppercase Output

def uppercase(func):
    def wrapper():
        return func().upper()
    return wrapper

@uppercase
def get_msg():
    return "hello world"

print(get_msg())


# 6) Call Counter

def counter(func):
    count = 0
    def wrapper():
        nonlocal count
        count += 1
        print("Called", count, "time(s)")
        func()
    return wrapper

@counter
def show():
    print("Function Executed")

show()
show()


# 7) Prefix ID Decorator

def prefix(func):
    def wrapper():
        return "ID: " + func()
    return wrapper

@prefix
def get_name():
    return "Ravi"

print(get_name())


# 8) Double Message Wrapper

def messages(func):
    def wrapper():
        print("Initializing...")
        func()
        print("Cleanup Complete")
    return wrapper

@messages
def task():
    print("Function Logic Runs")

task()


# 9) Negative Result Blocker

def blocker(func):
    def wrapper(a, b):
        result = func(a, b)
        if result < 0:
            return 0
        return result
    return wrapper

@blocker
def subtract(a, b):
    return a - b

print(subtract(5, 10))


# 10) Input Type Validator

def validator(func):
    def wrapper(arg):
        if type(arg) != str:
            print("Error: Invalid Input Type")
        else:
            func(arg)
    return wrapper

@validator
def display(text):
    print("Hello", text)

display("Ravi")
display(100)


