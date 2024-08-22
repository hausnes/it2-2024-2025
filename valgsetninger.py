# Valgsetninger
alder = 15

if alder > 0 and alder < 100:
    print("Du er over 0.")
else:
    print("Du er under 0.")

# Oppgave: Be brukeren om alder. Skriv ut hvilket type førerkort hen kan ta.
alderen = int(input("Hvor gammel er du? "))

# Denne løsningen fungerer, men ...
# if alderen >= 21:
#     print("Du kan ta førerkort for buss, bil og moped.")
# elif alderen < 21 and alderen >= 18:
#     print("Du kan ta førerkort for bil og moped.")
# elif alderen < 18 and alderen >= 16:
#     print("Du kan ta førerkort for moped.")
# else: 
#     print("Du har ikke riktig alder.")

if alderen >= 21:
    print("Du kan ta førerkort for buss, bil og moped.")
elif alderen >= 18:
    print("Du kan ta førerkort for bil og moped.")
elif alderen >= 16:
    print("Du kan ta førerkort for moped.")
else:
    print("Du har ikke riktig alder.")

# Lete etter "noe" i en string
interesse = "chips og VuRdErinGsarbeid"
if "vurdering" in interesse.lower():
    print("Min venn")
else:
    print("...")