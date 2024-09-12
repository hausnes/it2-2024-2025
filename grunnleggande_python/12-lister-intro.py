'''
    --------------------
    Obs! Aller først, kva er ein string/setning?
    --------------------
'''
setning = "Hei, verden!"
for bokstav in setning:
    if bokstav == "!":
        continue # Hopp over utskrift av utropsteiknet
    else:
        print(bokstav, end=" ")

'''
    --------------------
          Lister
    --------------------
'''
print("\nListe:")
nummer = [1, 2, 3, 4, 5, ["seks", "sju"]] # NB! Mogleg med liste i liste
# Skriv ut heile lista
print("Alle nummer:",nummer)
# Skriv ut siste element i lista
print("Siste nummer i lista:",nummer[-1])
# Legg til eit element i lista
nummer.append(8)
print("Lista etter at nye data er lagt til:",nummer)

# Finn ut om eit element er i lista
if 8 in nummer:
    print("\nTallet 8 er i lista.")

# Løkke som går gjennom alle elementa i lista
print("\nfor-in-løkke:")
for tall in nummer:
    print(tall)

# Løkke som går gjennom alle elementa i lista
print("\nwhile-løkke:")
i = 0
while i < len(nummer):
    print(nummer[i])
    i += 1

# Løkke som går gjennom alle elementa i lista
print("\nfor-in-range-løkke med indeks:")
for i in range(len(nummer)):
    print(nummer[i])

# Multidimensjonal liste:
print("\nMultidimensjonal liste:")
koordinater = [
    [1, 2, 3],
    [4, 5, 6]
]
print("Alle koordinater:", koordinater)

for k in koordinater:
    print("Koordinat:", k[0], k[1], k[2])

# Liste med bokstaver
listeBokstaver = ["e", "b", "C", "a", "d"]
print("\nListe med bokstavar:", listeBokstaver)
# Sorter lista
listeBokstaver.sort()
print("Sortert liste med bokstavar:", listeBokstaver)

liste1 = [1,2,[3,[4,5]]]
liste2 = liste1.copy()
print("Liste 2, kopiert:", liste2)

'''
    --------------------
           Tuppel
    --------------------
'''
print("\nTuppel:")
koordinater = (1, 2, 3)
print(koordinater)
# Legg tiol eit element i tuppelen
koordinater = koordinater + (4,)
print(koordinater)




# Sett
print("\nSett:")
unike_nummer = {1, 2, 3, 4, 5}
print(unike_nummer)

# Mengde
print("\nMengde:")
unike_bokstaver = set("Hello, world!")
print(unike_bokstaver)