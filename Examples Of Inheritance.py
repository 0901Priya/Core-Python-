class Character:
    def __init__(self,name,hp,attack,buff=0.2):
        self.n=name
        self.hp=hp
        self.attack=attack
        self.buff=buff
    def __str__(self):
        return f"name:{self.n}\n Hp:{self.hp} attack:{self.attack} buff:{self.buff}"
    def __repr__(self):
        return str(self)
class Mage(Character):
    pass
class Warrior(Character):
    pass

m1=Mage("Divya",100,1,0.3)
w1=Warrior("Ramya",1000,10,0.4)
print(m1.__str__())
print(w1.__str__())
print(m1.__repr__())
print(w1.__repr__())

