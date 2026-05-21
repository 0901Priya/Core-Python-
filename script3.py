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