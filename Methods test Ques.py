# 1. Decorator for Subtraction Function
def check_negative(func):
    def inner(a, b):
        result = func(a, b)
        if result < 0:
            return 0
        return result
    return inner

@check_negative
def subtract(a, b):
    return a - b

print(subtract(5, 10))   # 0
print(subtract(20, 5))   # 15

#2. Product Class
class Product:
    total_products = 0

    def __init__(self, name, category, price, quantity):
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity
        Product.total_products += 1

    @classmethod
    def from_string(cls, product_str):
        name, category, price, quantity = product_str.split("-")
        return cls(name, category, float(price), int(quantity))

    @staticmethod
    def is_valid_price(price):
        return price > 0

    def __str__(self):
        return f"{self.name} {self.category} {self.price} {self.quantity}"

# Validate price before creating product
if Product.is_valid_price(500):
    p1 = Product("Laptop", "Electronics", 500, 15)

p2 = Product.from_string("Mobile-Electronics-300-20")
p3 = Product.from_string("Book-Education-100-5")

products = [p1, p2, p3]

print("Total Products:", Product.total_products)

# Quantity > 10
print("\nProducts with quantity > 10:")
for p in filter(lambda x: x.quantity > 10, products):
    print(p)

# Sort by price
print("\nSorted by Price:")
for p in sorted(products, key=lambda x: x.price):
    print(p)

#3. HotelRoom Class
class HotelRoom:
    base_price = 1000

    def __init__(self, room_number, nights_booked, guest_name):
        self.room_number = room_number
        self.nights_booked = nights_booked
        self.guest_name = guest_name

    def calculate_bill(self):
        return self.nights_booked * HotelRoom.base_price

    @classmethod
    def update_base_price(cls, new_price):
        cls.base_price = new_price

    @staticmethod
    def valid_nights(nights):
        return isinstance(nights, int) and nights > 0


# Creating rooms
r1 = HotelRoom(101, 3, "Jhansi")
r2 = HotelRoom(102, 5, "Ravi")

print("Room 101 Bill:", r1.calculate_bill())
print("Room 102 Bill:", r2.calculate_bill())

# Change base price
HotelRoom.update_base_price(1500)

print("\nAfter Base Price Update:")
print("Room 101 Bill:", r1.calculate_bill())
print("Room 102 Bill:", r2.calculate_bill())

# Validation
print("\nValidation:")
print(HotelRoom.valid_nights(4))    # True
print(HotelRoom.valid_nights(-2))   # False
