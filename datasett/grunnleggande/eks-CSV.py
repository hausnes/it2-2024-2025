'''
Kjelde: Aunivers, IT2
https://innhold.aunivers.no/fagpakker/realfag/informasjonsteknologi-1-2/it-2/3-databehandling/3b-reelle-datasett/lese-og-bruke-csv-filer

NB: Ikkje bruk av OOP, Pandas eller andre bibliotek enn matplotlib for enkel oppteikning.
'''

import csv
import matplotlib.pyplot as plt

filnavn = "data/befolkning_1951_2022.csv"

# Lister for å ta vare på alle årstall og befolkningsstørrelser
aarstall = []
befolkning = []

with open(filnavn, encoding="utf-8-sig") as fil: # sig handterer mellom anna æ, ø og å
    filinnhold = csv.reader(fil, delimiter=";")

    overskrifter = next(filinnhold)
    print(overskrifter)

    for rad in filinnhold:
        aarstall.append(int(rad[0]))
        befolkning.append(int(rad[1]))

# Tegner grafen
plt.plot(aarstall, befolkning) # Utgangspunkt i listene, x- og y-akse
plt.grid()
plt.show()