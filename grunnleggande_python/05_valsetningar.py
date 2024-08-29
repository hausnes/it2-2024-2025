# Valsetningar
alder = 15  # latar som om me har fått input frå brukar

if alder > 0 and alder < 100:
    print("Du er over 0 og mindre enn 100 AKA mellom 1 og 99.")
else:
    print("Du er under 0.")

# Oppgåve: Be brukaren om alder. Skriv ut kva type førarkort hen kan ta.
alderen = int(input("Kor gamal er du? "))

# Denne løsninga fungerer, men ...
# if alderen >= 21:
#     print("Du kan ta førarkort for buss, bil og moped.")
# elif alderen < 21 and alderen >= 18:
#     print("Du kan ta førarkort for bil og moped.")
# elif alderen < 18 and alderen >= 16:
#     print("Du kan ta førarkort for moped.")
# else:
#     print("Du har ikkje riktig alder.")

if alderen >= 21:
    print("Du kan ta førarkort for buss, bil og moped.")
elif alderen >= 18:
    print("Du kan ta førarkort for bil og moped.")
elif alderen >= 16:
    print("Du kan ta førarkort for moped.")
else:
    print("Du har ikkjee riktig alder.")

# Lete etter "noe" i en string
interesse = "chips og VuRdErinGsarbeid"  # NB: Legg merke til store og små bokstavar
if "vurdering" in interesse.lower():
    print("Min venn, me har noko til felles!")
else:
    print("...")

