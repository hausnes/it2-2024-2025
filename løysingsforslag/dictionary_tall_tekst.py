# Opprett en ordbok som inneholder tallene som nøkler og tekstene som verdier
tall_tekst = {
    1: "en", 
    2: "to", 
    3: "tre", 
    4: "fire", 
    5: "fem", 
    6: "seks", 
    7: "syv", 
    8: "åtte", 
    9: "ni", 
    10: "ti"
}

# Skriv ut alle tallene med sine tilhørende tekster i tabellform
print("Tall | Tekst")
print("-----|------")
for tall, tekst in tall_tekst.items():
    print(f"{tall:<5}| {tekst}")

# Test ordboka ved å la en bruker skrive inn et tall
tall_inn = int(input("Skriv inn et tall mellom 1 og 10: "))
if tall_inn in tall_tekst:
    print(f"Teksten for {tall_inn} er {tall_tekst[tall_inn]}.")
else:
    print(f"Ugyldig tall. Prøv igjen.")