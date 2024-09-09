'''
    timeit-biblioteket i Python kan brukast for å vurdere effektiviteten 
    av ulike versjonar av kode. 
    Les meir: https://docs.python.org/3/library/timeit.html
'''
# Om det å sjekke kva for ein versjon av kode som er mest effektiv
import timeit

# Første versjon
def versjon1():
    innlest = "din teststreng her"  # Sett inn ein teststreng
    for bokstav in innlest.lower():
        if bokstav == "æ" or bokstav == "ø" or bokstav == "å":
            return "Ikkje lov til å bruke æ, ø eller å."

# Andre versjon
def versjon2():
    innlest = "din teststreng her"  # Sett inn ein teststreng
    forbudte_bokstaver = {"æ", "ø", "å"}
    if any(bokstav in forbudte_bokstaver for bokstav in innlest.lower()): # generatoruttrykk (bruker lite minne), ligner på list comprehension
        return "Ikkje lov til å bruke æ, ø eller å."

# Måle køyretid
tid1 = timeit.timeit(versjon1, number=10000)
tid2 = timeit.timeit(versjon2, number=10000)

print(f"Versjon 1 tid: {tid1}")
print(f"Versjon 2 tid: {tid2}")

# Di oppgåve: Samanlikn match-case og if-elif-else
# ...