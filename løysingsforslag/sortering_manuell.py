'''
    Skriv en kode som bytter plass på verdiene i lista tall = [3, 4, 1, 2, 5] 
    slik at den blir sortert. Du skal altså sortere lista manuelt.
'''

import timeit

# Den enklaste og mest lettleste algoritmen (Jens Leonard Engeset sin løysing)
def jens_sort(tall):
    tallKopi = tall[:]
    tallSortert = []
    
    for _ in tall:
        minst = min(tallKopi)
        tallSortert.append(minst)
        tallKopi.remove(minst)

# Boblesortering
def bubble_sort(tall):
    n = len(tall)
    for i in range(n):
        for j in range(0, n-i-1):
            if tall[j] > tall[j+1]:
                tall[j], tall[j+1] = tall[j+1], tall[j]

# Utvalgssortering
def selection_sort(tall):
    n = len(tall)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if tall[j] < tall[min_idx]:
                min_idx = j
        tall[i], tall[min_idx] = tall[min_idx], tall[i]

# Liste som skal sorteres
tall = [3, 4, 1, 2, 5]

# Tid for jens-sortering
tid_jens = timeit.timeit(lambda: jens_sort(tall.copy()), number=10000)
print(f"Jens-sort tid: {tid_jens}")

# Tid for boblesortering
tid_bubble = timeit.timeit(lambda: bubble_sort(tall.copy()), number=10000)
print(f"Boblesortering tid: {tid_bubble}")

# Tid for utvalgssortering
tid_selection = timeit.timeit(lambda: selection_sort(tall.copy()), number=10000)
print(f"Utvalgssortering tid: {tid_selection}")

'''
Liten diskusjon rundt valet mellom å vere lett å forstå, og kor effektiv algoritmen er. 
På grunn av måten jens_sort håndterer elementene i listen er den ikkje like effektiv, men
den vil typisk vere lettare å forstå. 

La oss sjå nærare på dette med effektivitet, og kva som gjer at den blir mindre effektiv:

min-funksjonen:
jens_sort bruker min-funksjonen for å finne det minste elementet i den gjenværande delen av lista. 
min-funksjonen har ein tidskompleksitet på O(n) for kvart kall, der n er antall element i lista.
Sidan min-funksjonen kallast inne i ei løkke som går gjennom alle elementa i lista, blir den totale 
tidskompleksiteten O(n^2).

remove-funksjonen:
jens_sort bruker og remove-funksjonen for å fjerne det minste elementet frå lista. 
remove-funksjonen har ein tidskompleksitet på O(n) fordi den må finne elementet før det kan fjernast.
Dette betyr at for kvar iterasjon, vil remove-funksjonen og bidra til den totale 
tidskompleksiteten på O(n^2).

Sammenligning med boblesortering og utvalgssortering:
Boblesortering og utvalgssortering har begge ein tidskompleksitet på O(n^2), men dei gjør færre 
operasjoner per iterasjon samanlikna med jens_sort.
Boblesortering og utvalgssortering gjer samanlikninger og byter element direkte, medan jens_sort 
gjer fleire operasjonar (kall til min og remove) som kvar har ein tidskompleksitet på O(n).

Sjølv om jens_sort kan vere lettare å lese og forstå, er den generelt mindre effektiv på grunn av 
dei ekstra operasjonane som blir utført i kvar iterasjon. Dette kan forklare kvifor jens_sort ofte 
er treigere enn boblesortering og utvalgssortering i praksis, spesielt for større lister.
'''