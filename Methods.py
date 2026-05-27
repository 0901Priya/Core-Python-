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

