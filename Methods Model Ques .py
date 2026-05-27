
class CartItem:
    def __init__(self, item_name, price, quantity):
        self.item_name = item_name
        self.price = price
        self.quantity = quantity
    def final_amount(self):
        return self.price * self.quantity
    def __str__(self):
        return f"Item: {self.item_name}, Price: {self.price}, Quantity: {self.quantity}"
    def __add__(self, other):
        return self.final_amount() + other.final_amount()
    def __mod__(self, discount):
        return self.final_amount() % discount
    def __lt__(self, other):
        return self.final_amount() < other.final_amount()
    def __ge__(self, other):
        return self.quantity >= other.quantity
    def __getattribute__(self, name):
        print(f"Accessing attribute: {name}")
        return object.__getattribute__(self, name)
    def __setattr__(self, name, value):
        if name == "quantity" and value < 1:
            print("Quantity cannot be less than 1")
        else:
            object.__setattr__(self, name, value)

c1 = CartItem("Mouse", 500, 2)
c2 = CartItem("Keyboard", 1000, 1)
print(c1)
print(c1.final_amount())
print(c1 + c2)
print(c1 % 300)
print(c1 < c2)
print(c1 >= c2)

class Laptop:
    def __init__(self, brand, ram, price):
        self.brand = brand
        self.ram = ram
        self.price = price
    def upgrade_ram(self, extra_ram):
        self.ram += extra_ram
    def __str__(self):
        return f"Brand: {self.brand}, RAM: {self.ram}GB, Price: {self.price}"
    def __add__(self, other):
        return self.price + other.price
    def __mul__(self, quantity):
        return self.price * quantity
    def __lt__(self, other):
        return self.price < other.price
    def __eq__(self, other):
        return self.ram == other.ram
    def __getattribute__(self, name):
        print(f"Accessing attribute: {name}")
        return object.__getattribute__(self, name)
    def __setattr__(self, name, value):
        if name in ["ram", "price"] and value <= 0:
            print(f"{name} must be positive")
        else:
            object.__setattr__(self, name, value)

l1 = Laptop("Dell", 8, 50000)
l2 = Laptop("HP", 8, 60000)
print(l1)
l1.upgrade_ram(4)
print(l1)
print(l1 + l2)
print(l1 * 2)
print(l1 < l2)
print(l1 == l2)


class Book:
    def __init__(self, book_name, isbn_number, is_borrowed=False):
        self.book_name = book_name
        self.isbn_number = isbn_number
        self.is_borrowed = is_borrowed
    def __str__(self):
        return f"Book: {self.book_name}, ISBN: {self.isbn_number}, Borrowed: {self.is_borrowed}"

class User:
    max_limit = 3

    def __init__(self, name):
        self.name = name
        self.no_of_books_borrowed = 0
        self.books = []
    def __add__(self, book):
        if self.no_of_books_borrowed < User.max_limit and not book.is_borrowed:
            self.books.append(book)
            self.no_of_books_borrowed += 1
            book.is_borrowed = True
            print(f"{book.book_name} borrowed")
        else:
            print("Cannot borrow book")
        return self
    def __sub__(self, book):
        if book in self.books:
            self.books.remove(book)
            self.no_of_books_borrowed -= 1
            book.is_borrowed = False
            print(f"{book.book_name} returned")
        return self
    def __contains__(self, book):
        return book in self.books
    def __len__(self):
        return self.no_of_books_borrowed
    def __str__(self):
        return f"User: {self.name}, Books Borrowed: {self.no_of_books_borrowed}"


b1 = Book("Python", 12345)
b2 = Book("Java", 67890)
u1 = User("Jhansi")
u1 + b1
u1 + b2
print(u1)
print(b1 in u1)
print(len(u1))
u1 - b1
print(u1)
print(b1)
