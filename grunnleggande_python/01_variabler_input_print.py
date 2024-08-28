# Variablar
tall1 = 5
tall2 = 4
summen = tall1 + tall2

# Skrive ut ...
print("resultat av",tall1,"og",tall2,"er",summen,sep=" ") # alt. 1: sep lar oss spesifisere kva mellomrom skal vere
#print("resultat av " + tall1) # Utfordring: datatypar # alt. 2
print(f"resultat av {tall1} og {tall2} er {summen}") # alt. 3: formatted string, anbefalt måte

# Oppgåve: Gjer det mogleg for brukaren å velgje kva tall1 og 2 er.
tallEn = int(input("Tall 1: ")) # kunne brukt float for å ....
tallTo = int(input("Tall 2: "))
resultatet = tallEn + tallTo
print(f"Resultat av {tallEn} og {tallTo} er {resultatet}.")