
from guitar import Guitar

g1 = Guitar()
g1.name = "Gibson L-5 CES"
g1.year = 1922
g1.cost = 16035.40

g2 = Guitar("Another Guitar", 2013, 15000.25)

print(g1)
print(g1.get_age())
print(g1.is_vintage())

print(g2)
print(g2.is_vintage())