import random
import timeit
 
items = ['stein', 'saks', 'papir']
 
count_stein = 0
count_saks = 0
count_papir = 0
 
def tidsskjekk():
    global count_stein, count_saks, count_papir  # Deklarer globale variabler

    for x in range(500):
        valg = random.choice(items)
    
        if valg == 'stein':
            count_stein += 1
        elif valg == 'saks':
            count_saks += 1
        elif valg == 'papir':
            count_papir += 1
 
 
    #print(f"stein ble valgt {count_stein} ganger.")
    #print(f"saks ble valgt {count_saks} ganger.")
    #print(f"papir ble valgt {count_papir} ganger.")
 
 
tidsskjekk()
 
tid1 = timeit.timeit(tidsskjekk, number=10000)
print(f"tid: {tid1}")

# # Unike tal i ei liste
# liste = [1, 2, 3, 4, 4, 4, 5]
# print(f"Liste med alle verdiar: {liste}\n")
# unike = set(liste)
# print(unike)

# # Litt om random
# import random
# import datetime

# random.seed(10)
# print(random.random())

# random.seed(10)
# print(random.random()) # Denne blir lik som den over

# tidspunktAkkuratNo = datetime.datetime.now()
# print(tidspunktAkkuratNo)
# random.seed(str(tidspunktAkkuratNo))
# print(random.random())

# random.seed("2024-09-12 09:09:47.249662")
# print(random.random())
# random.seed("2024-09-12 09:09:47.249662")
# print(random.random())

# # Gjettespel, om tal (Mario)
# import random as rnd

# tall = rnd.randint(1, 100)
# forsok = 0
# kriterier = list(range(1, 101))

# print("Eit tilfeldig tall mellom ein og hundre er generert. Du har 5 forsøk på å gjette tallet")

# while forsok < 5:
#     try:
#         brukerValg = int(input("Skriv inn eit tall mellom 1 og 100: "))
#         if brukerValg not in kriterier:
#             print("Tallet du skriver MÅ vere mellom ein og hundre")
#         # NB: Dei to linjene over her er ikkje effektive, gjer heller dette:
#         # if brukerValg < 1 or brukerValg > 100:
#         elif brukerValg > tall:
#             print("Tallet du leiter etter har ein lavere verdi")
#         elif brukerValg < tall:
#             print("Tallet du leiter etter har ein høgere verdi")
#         else:
#             print("Du har funnet riktig tall")
#             break
#     except ValueError:
#         print("Du må skrive inn et gyldig tall.")
    
#     forsok += 1
#     print(f"Du har {5 - forsok} forsøk igjen")

# if forsok == 5:
#     print(f"Du har brukt opp alle forsøkene dine. Tallet du leita etter var {tall}")