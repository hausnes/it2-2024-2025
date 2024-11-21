# Sjekkar om tala æ, ø eller å er i input frå brukar:
innlest = input("Input: ")
for bokstav in innlest.lower():
    if bokstav == "æ" or bokstav == "ø" or bokstav == "å":
        print("Ikkje lov til å bruke æ, ø eller å.")

# Alternativ versjon
# Sjekkar om tala æ, ø eller å er i input frå brukar:
innlest = input("Input: ")
forbudte_bokstaver = {"æ", "ø", "å"}
if any(bokstav in forbudte_bokstaver for bokstav in innlest.lower()):
    print("Ikkje lov til å bruke æ, ø eller å.")

# Stein, saks, papir og tilfeldigheiter
# Kva betyr det at noko er tilfeldig?
import random

antallStein = 0
antallSaks = 0
antallPapir = 0

for kast in range(4):
    resultat = random.choice(["stein", "saks", "papir"])
    if resultat == "stein":
        antallStein += 1
    elif resultat == "saks":
        antallSaks += 1
    else:
        antallPapir += 1
    
print(f"Stein: {antallStein},\n Saks: {antallSaks},\n Papir: {antallPapir}")