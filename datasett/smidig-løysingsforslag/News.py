'''
    <The Pandas Way>
    Legg merke til bruken av value_counts, head (og potensielt tail)
'''

# import pandas
# import matplotlib.pyplot as plt

# # Last inn fila med nyheiter.
# df = pandas.read_json("News_Category_Dataset_v3.json", lines=True)

# # Kor mange saker i kvar kategori?
# # Brukar https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.value_counts.html 
# print("\nSaker i kvar kategori:")
# antall_saker = df['category'].value_counts()
# # print(antall_saker)
# print(antall_saker.head(5)) # Viser dei forfattarane med flest saker (5)

# # Plotting av antall saker i kvar kategori
# plt.figure(figsize=(10, 6))
# antall_saker.head(5).plot(kind='bar') # NB: Ta vekk .head(5) for å vise alle
# plt.xlabel("Kategori")
# plt.ylabel("Antall saker")
# plt.title("Antall saker i kvar kategori")
# plt.xticks(rotation=90)
# plt.show()

# print("\nSaker per forfattar:")
# # Kor mange artiklar har kvar forfattar skrive?
# artikkel_teller = df['authors'].value_counts()
# # print(artikkel_teller)
# print(artikkel_teller.tail(5)) # Viser dei siste 5 ...

# 

'''
    <The 'manual' way>
'''

import json
import matplotlib.pyplot as plt

# Filnavn
filnavn = "News_Category_Dataset_v3.json"

# Ordbok for å telle antall artiklar per forfatter
artikkel_teller = {}

# Les JSON-fila linje for linje
with open(filnavn, encoding="utf-8") as fil:
    for linje in fil:
        data = json.loads(linje)
        forfatter = data.get("authors", "Ukjent forfattar") # "Ukjent forfattar blir lagt til dersom ingen author er oppgitt"
        if not forfatter:  # Sjekk for tom streng
            forfatter = "Ukjent forfattar"
        if forfatter in artikkel_teller:
            artikkel_teller[forfatter] += 1
        else:
            artikkel_teller[forfatter] = 1

# Sorter forfattarar etter antall artiklar i synkande rekkefylgje
sorterte_forfattarar = sorted(artikkel_teller.items(), key=lambda item: item[1], reverse=True)

# Fjern "Ukjent forfattar" fra listen
sorterte_forfattarar = [item for item in sorterte_forfattarar if item[0] != "Ukjent forfattar"]

# Skriv ut de 5 mest produktive forfatterne
# for i in range(min(5, len(sorterte_forfattarar))):
#     forfatter, antall = sorterte_forfattarar[i]
#     print(f"{forfatter}: {antall} artikler")

# Hent ut de 5 mest produktive forfatterne
topp_5_forfattarar = sorterte_forfattarar[:5]

# Lag lister for x- og y-aksene
forfattarar = [forfatter for forfatter, antall in topp_5_forfattarar]
antall_artiklar = [antall for forfatter, antall in topp_5_forfattarar]

# Plotting av de 5 mest produktive forfatterne
plt.figure(figsize=(10, 6))
plt.bar(forfattarar, antall_artiklar, color='skyblue')
plt.xlabel("Forfatter")
plt.ylabel("Antall artiklar")
plt.title("Dei 5 mest produktive forfattarane")
plt.xticks(rotation=45)
plt.subplots_adjust(bottom=0.3)  # Juster margane for å få meir plass under x-aksen
plt.show()