import math ##nécessaire pour la racine


class Point :
    def __init__(self,x:int,y:int):
        self.x=x
        self.y=y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def norm(self):
        return math.sqrt(self.x**2+self.y**2)
    


# pour tester

try:
    p = Point(3, 4)
    assert (p.x, p.y) == (3, 4)
    assert p.norm() == 5.0
    assert repr(p) == "Point(3, 4)"
    q = Point(0, 1)
    assert (q.x, p.x) == (0, 3)
except Exception as e:
    print("OOPS - Something's wrong")
    print(f"Error message : {e}")
else:
    print('Congrats ! Your implementation works !')

p=Point(3, 4)
print(p.norm(),Point.norm(p)) ## Affiche bel et bien la même chose

class Bad:
    items = []

    def add(self, x):
        self.items.append(x)

a, b = Bad(), Bad()
a.add(1)
print(b.items)
#a et b sont associés à items donc les changements de l'un influe l'autre

# Correction
class Bad:
    def __init__(self):
        self.items=[]

    def add(self, x):
        self.items.append(x)

a, b = Bad(), Bad()
a.add(1)
print(b.items)
## Chaque élément est maintenant repéré par son self et a un items associé

#Tirelire
class Tirelire :
    def __init__(self):
        self.tirelire=[]

    def total(self):
        S=0
        for c in self.tirelire :
            S+=c
        return S

    def deposit(self,value:float):
        if value<=0:
            raise ValueError("Une pièce ne peut pas être négative")
        else :
            self.tirelire.append(value)

    def __len__(self):
        return len(self.tirelire)
    
    def __repr__(self):
        return f"Tirelire({len(self.tirelire)} coins, total={self.total()})"

#Test 
t = Tirelire()
t.deposit(0.5)
t.deposit(1)
assert len(t) == 2
assert t.total() == 1.5
print(repr(t))
other = Tirelire()
assert len(other) == 0
print("Ca marche")    

##La Classe Student