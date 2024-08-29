# Oppgåve: Lag stein, saks og papir. La spelaren spele mot datamaskina

# Først litt om random...
import random

tilfeldigTall = random.randint(1, 5)
print(tilfeldigTall)

tilfeldigTall = random.randrange(1, 11, 3)  # Kva gjer denne?
print(tilfeldigTall)

tilfeldigVal = random.choice(
    ["Karakter 1", "Karakter 2", "Karakter 3", "Karakter 4", "Karakter 5", "Karakter 6"]
)
print(tilfeldigVal)

