# Variablar
tall1 = 4
tall2 = 6
resultat = tall1 + tall2

# Utskrift
print("Resultatet av", tall1, "og", tall2, "er", resultat, sep=" ")
print(f"Resultatet av {tall1} og {tall2} er {resultat}") # formatted string

# Oppgåve: La brukaren velgje kva tall1 og tall2 er.
# Meir avansert oppgåve: Handter feil.


# Valsetningar
alder = 15

if alder > 0 and alder <= 100:
    print("Innanfor grensene.")
else:
    print("Utanfor grensene.")

'''
Oppgåve: 
    La brukaren skrive inn alder. Dersom brukaren er innanfor grensene 
    legg du personen i ulike kategoriar. Dvs. auk antallet innanfor kategoriane
    -  0 -  20
    - 21 -  40
    - 41 -  60
    - 61 -  80
    - 81 - 100
'''

# Valsetningar og å leite innan strings
svar = "Jeg liker chips og vurderingsbunker."

if "vurdering" in svar:
    print("Du likte vurdering, din fjott!")
else:
    print("Du likte ikke vurdering.")

# Oppgåve: La det vere likegyldig om brukaren skriv med store eller små bokstavar.