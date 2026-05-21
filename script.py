def dec(function):
     def inner():
         print("start")
         function()
         print("end")
     return inner
@dec
def hello():
    print("Hello")
hello()


def dec(fun):
    def inner(name):
        print("starting")
        fun(name)
        print("done")
    return inner
@dec
def greet(name):
    print("Hello",name)
greet("Priya")

def double_result(fun):
    def inner():
        result=fun()
        return result*2
    return inner
@double_result
def get_value():
    return 25
print(get_value())

user_role="student"
def check(fun):
    def inner():
        if user_role=="admin":
            fun()
        else:
            print("Access denied")
    return inner
@check
def show():
    print("Welcome Admin")
show()

def upper(fun):
    def inner():
        return fun().upper()
    return inner
@upper
def get_msg():
    return "Hello world"
print(get_msg())

a=[1,2,3,4]
b=[10,20,30,40]
result=list(map(lambda x,y:x+y,a,b))
print(result)

num=[12,15,7,18,20,21,25]
result=list(filter(lambda x:(x%3==0)^(x%5==0),num))
print(result)

from functools import reduce
num=[1,2,3,4]
result=reduce(lambda x,y:x+y,num,10)
print(result)

num=[[1,2],[3,4],[5,6]]
result=list(map(lambda x:x.append(10),num))
print("Result:",result)
print("Num:",num)

def call_counter(fun):
    c=0
    def inner():
        fun()
        nonlocal c
        c=c+1
        print(f"called {c} times")
    return inner
@call_counter
def counting():
    print("counting")
counting()



class A:
    def __init__(self, x):
        self.x=x
    def __add__(self, o2):
        return self.x+o2
a1=A(10)
a2=A(20)
print(a1,a2)


class B:
    def __init__(self,x):
        self.x=x
    def __add__(self, o2):
        if isinstance(o2, int):
            return self.x+o2
        if isinstance(o2, B):
            return self.x+o2.x
        else:
            print("Wrong class")
            return 0
b1=B(30)
b2=B(35)
print(b1+b2)

class C:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def __add__(self, o2):
        if isinstance(o2, str):
            return slef.x+o2.x
        elif isinstance(o2, int):
            return self.y+o2
        else:
            return self.z+o2.z

class D:
    def __str__(self):
        return "This Dclass"
    def __repr__(self):
        return "This repr"

d1=D()
print(d1)
print([d1])


class Product:
    def __init__(self,name,price,quantity):
            name=name
            self.price=price
            self.quantity=quantity
class Cart:
    def __init__(self):
        self.l=[]
    def __add__(self,o2):
        self.l.append(o2)
    def __sub__(self, o2):
        if o2 in self.l:
            self.l.remove(o2)
    def total_price(self):
        s=0
        for i in self.l:
            s+=(i.price*i.quantity)
        return s
    def __str__(self):
        for i in self.l:
            print(i)
        print(f"total product: {self.total_price()}")



class E:
    def __init__(self,a):
        self.a=a
    def __gt__(self, o2):
        return self.a>o2.a
    def __lt__(self,o2):
        return self.a<o2.a
e1=E(25)
e2=E(35)
print(e1>e2)
print(e1<e2)

class E:
    def __init__(self,a):
        self.a=a
    def __gt__(self, o2):
        return self.a>o2.a
    def __le__(self,o2):
        return self.a<o2.a
e1=E(25)
e2=E(35)
print(e1>=e2)
print(e1<=e2)
print(e1==e2)

class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def td(self):
       return (self.x**2 + self.y**2)**(1/2)
    def __add__(self, o2):
        return Vector(self.x + o2.x, self.y + o2.y)
    def __sub__(self, o2):
        return Vector(self.x - o2.x, self.y - o2.y)
    def __gt__(self, o2):
        return self.td() > o2.td()
    def __lt__(self, o2):
        return self.td() < o2.td()
    def __ge__(self, o2):
        return self.td() >= o2.td()
    def __le__(self, o2):
        return self.td()<= o2.td()
    def __eq__(self, O2):
        return self.x == o2.x and self.y == o2.y
    def __str__(self):
        print(f"Vector({self.x}, {self.y})")
        return f"total_distance:{self.td()}"

V1=Vector(40,50)
V2=Vector(50,60)
V3=Vector(10,10)
print(V1+V2+V3)
print(V2-V1+V3)
print(V1-V2+V3)
print(V1-V2-V3)W
print(V3-V2+V1)

 class Books:
     def __init__(self, title,author,is_borrowed):
         self.title = title
         self.author = author
         self.is_borrowed = False
     def __str__(self):
         return f"{self.title}:{self.author}"
     def __rep__(self):
         return f"(self.title}:{self.author}"
class Library:
    def __init__(self):
        l={}
        def __add__(self,o2):
            if(len(02.title)>7:
                library[02.title]=o2
