# Variablar
tall1 = 5
tall2 = 4
resultat = tall1 + tall2

# Skrive ut ...
print("Summen av",tall1,"og",tall2,"er",resultat,sep=" ")
#print("Summen av " + tall1) # Dette går ikke fordi...
print(f"Summen av {tall1} og {tall2} er {resultat}") # Formatted string

# Oppgave: Gjør det mulig for brukeren å velge hva tall1 og 2 er.
tallEn = int(input("Tall 1: ")) # kunne brukt float for å ....
tallTo = int(input("Tall 2: "))
resultatet = tallEn + tallTo
print(f"Summen av {tallEn} og {tallTo} er {resultatet}.")