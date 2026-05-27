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
