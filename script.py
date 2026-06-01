# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from abc import ABC, abstractmethod
import copy

# ---------------- ITEM & BOOK ----------------

class Item(ABC):
    @abstractmethod
    def get_summary(self):
        pass

class Book(Item):
    catalog_tag = "BOOK"

    def __init__(self, title, metadata, available=True):
        self.title = title
        self._metadata = {}

        for k, v in metadata.items():
            if self.validate_key(k):
                self._metadata[k] = v

        self._available = available

    @staticmethod
    def validate_key(key):
        return isinstance(key, str)

    @property
    def metadata(self):
        return self._metadata

    @classmethod
    def update_tag(cls, tag):
        cls.catalog_tag = tag

    def pricing(self, price, discount=0):
        return price - (price * discount / 100)

    def get_summary(self):
        return f"{self.title} - {self._metadata}"

    def __str__(self):
        return f"Book: {self.title}"

    def __repr__(self):
        return f"Book('{self.title}', {self._metadata})"


b1 = Book("Python", {"author": "ABC"})
b2 = Book("Java", {"author": "XYZ"})

print(str(b1))
print(repr(b1))
Book.update_tag("LIBRARY")
print(Book.catalog_tag)
books = [b1, b2]
shallow = copy.copy(books)
deep = copy.deepcopy(books)
books[0]._metadata["author"] = "NEW"
print(shallow[0]._metadata)
print(deep[0]._metadata)


# ---------------- USERBASE & MEMBER ----------------

class UserBase(ABC):
    @abstractmethod
    def get_role(self):
        pass

class Member(UserBase):
    user_count = 0
    admin_flag = False

    def __init__(self, username, credentials):
        self.username = username
        self._credentials = credentials
        self.__perms = []
        Member.user_count += 1

    @staticmethod
    def validate_perm(perm):
        return perm.isalpha()

    def __add__(self, perm):
        if self.validate_perm(perm):
            self.__perms.append(perm)
        return self

    def __sub__(self, perm):
        if perm in self.__perms:
            self.__perms.remove(perm)
        return self

    def __eq__(self, other):
        return self.username == other.username and self.__perms == other.__perms

    @classmethod
    def update_admin(cls, val):
        cls.admin_flag = val

    def perform(self, action, timeout=3):
        print(f"{self.username} performs {action} in {timeout}s")

    def get_role(self):
        return "Member"

    def __str__(self):
        return f"User: {self.username}"

    def __repr__(self):
        return f"Member('{self.username}', '***')"


u1 = Member("john", "1234")
u2 = Member("john", "5678")
u1 + "read"
u1 + "write"
u1 - "write"
print(u1 == u2)
users = [u1]
s1 = copy.copy(users)
d1 = copy.deepcopy(users)
u1 + "edit"
print(s1[0])
print(d1[0])


# ---------------- VEHICLEBASE & CAR ----------------

class VehicleBase(ABC):
    @abstractmethod
    def diagnose(self):
        pass

class Car(VehicleBase):
    service_rate = 10

    def __init__(self, model, miles, log):
        self.model = model
        self._miles = miles
        self.__log = log

    @staticmethod
    def validate_miles(m):
        return m >= 0

    @property
    def miles(self):
        return self._miles

    @miles.setter
    def miles(self, value):
        if self.validate_miles(value):
            self._miles = value

    def diagnose(self):
        print(f"{self.model} diagnosis complete")

    def service_cost(self):
        return self._miles * Car.service_rate

    def __str__(self):
        return f"Car: {self.model}"

    def __repr__(self):
        return f"Car('{self.model}', log='***')"

class Fleet:
    def __init__(self):
        self.cars = []

    def __add__(self, car):
        self.cars.append(car)
        return self

    def __len__(self):
        return len(self.cars)

    def __contains__(self, car):
        return car in self.cars


c1 = Car("BMW", 100, ["oil"])
c2 = Car("Audi", 200, ["brake"])

fleet = Fleet()
fleet + c1
fleet + c2

print(len(fleet))
print(c1 in fleet)

for i in fleet.cars:
    i.diagnose()

sfleet = copy.copy(fleet)
dfleet = copy.deepcopy(fleet)

c1._Car__log.append("engine")

print(sfleet.cars[0]._Car__log)
print(dfleet.cars[0]._Car__log)


# ---------------- PRODUCT & CART ----------------

class Product:
    discount = 10

    def __init__(self, pid, price):
        if pid.isalnum():
            self.id = pid
        self._price = price

    @property
    def price(self):
        return self._price - (self._price * Product.discount / 100)

class Cart:
    def __init__(self):
        self.__products = []

    def add(self, product, qty=1):
        for i in range(qty):
            self.__products.append(product)

    def __add__(self, product):
        self.add(product)
        return self

    def __sub__(self, product):
        if product in self.__products:
            self.__products.remove(product)
        return self

    def __len__(self):
        return len(self.__products)

class Order:
    def __init__(self, cart, deep=False):
        if deep:
            self.snapshot = copy.deepcopy(cart)
        else:
            self.snapshot = copy.copy(cart)

    def __str__(self):
        return "Order Created"

    def __repr__(self):
        return "Order(snapshot)"


p1 = Product("P101", 1000)

cart = Cart()
cart + p1
cart.add(p1, 2)

print(len(cart))

order1 = Order(cart)
order2 = Order(cart, True)

cart - p1

print(order1)
print(order2)


# ---------------- CHARACTER, WARRIOR, MAGE ----------------

class Character(ABC):
    global_buff = 5

    def __init__(self, hp):
        self._hp = hp
        self.__inventory = []

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        self._hp = max(0, value)

    def change_hp(self, amount, reason='combat'):
        self.hp += amount
        print(reason)

    def __add__(self, item):
        if isinstance(item, str):
            self.__inventory.append(item)
        return self

    def __sub__(self, item):
        if item in self.__inventory:
            self.__inventory.remove(item)
        return self

    def __contains__(self, item):
        return item in self.__inventory

    @abstractmethod
    def attack(self, target):
        pass

    def __str__(self):
        return f"HP: {self.hp}"

    def __repr__(self):
        return f"Inventory='***'"

class Warrior(Character):
    def attack(self, target):
        print(f"Warrior attacks {target} with buff {Character.global_buff}")

class Mage(Character):
    def attack(self, target):
        print(f"Mage attacks {target} with buff {Character.global_buff}")

class Party:
    def __init__(self):
        self.__chars = []

    def add(self, char):
        self.__chars.append(char)

    def __len__(self):
        return len(self.__chars)

    def __iter__(self):
        return iter(self.__chars)


w = Warrior(100)
m = Mage(80)
w + "Sword"
m + "Magic"
party = Party()
party.add(w)
party.add(m)
for i in party:
    i.attack("Enemy")
sparty = copy.copy(party)
dparty = copy.deepcopy(party)
w + "Shield"
print(sparty)
print(dparty)
Character.global_buff = 20
w.attack("Boss")
m.attack("Boss")
