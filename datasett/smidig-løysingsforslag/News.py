'''
    The Pandas Way
'''

# # import pandas

# # Last inn fila med nyheiter.
# df = pandas.read_json("News_Category_Dataset_v3.json", lines=True)

# # Gruppér etter forfatter og tell antall artikler
# artikkel_teller = df['authors'].value_counts()

# # Skriv ut resultatet
# print(artikkel_teller)

'''
    The manual way..
'''

import json

# Filnavn
filnavn = "News_Category_Dataset_v3.json"

# Ordbok for å telle antall artikler per forfatter
artikkel_teller = {}

# Les JSON-filen linje for linje
with open(filnavn, encoding="utf-8") as fil:
    for linje in fil:
        data = json.loads(linje)
        forfatter = data.get("authors", "Ukjent forfatter")
        if forfatter in artikkel_teller:
            artikkel_teller[forfatter] += 1
        else:
            artikkel_teller[forfatter] = 1

# Sorter forfatterne etter antall artikler i synkende rekkefølge
sorterte_forfattere = sorted(artikkel_teller.items(), key=lambda item: item[1], reverse=True)

# Skriv ut de 5 mest produktive forfatterne
for i in range(min(5, len(sorterte_forfattere))):
    forfatter, antall = sorterte_forfattere[i]
    print(f"{forfatter}: {antall} artikler")