# Konsept til eit særs enkelt tekstbasert eventyrspel
valg = input("Du står ved et veikryss. Går du til høyre (h) eller venstre (v)? ")
if valg == 'h':
    print("Du finner en skatt!")
elif valg == 'v':
    print("Du møter en drage. Vil du kjempe (k) eller flykte (f)?")
    valg2 = input()
    if valg2 == 'k':
        print("Du tapte kampen.")
    elif valg2 == 'f':
        print("Du slapp unna.")
else:
    print("Ugyldig valg.")

# Oppgåve: Lag din eigen versjon av eit liknande konsept - med meir kompleksistet.
# import random

# def eventyr():
#     # Opprett en verden med flere rom
#     rom = {
#         "start": {"beskrivelse": "Du står i et mørkt rom. Det er en dør til nord og en gang til øst.", "utforsket": False, "valg": {"nord": "nord", "øst": "øst"}},
#         "nord": {"beskrivelse": "Du har funnet et sverd!", "utforsket": False, "valg": {"sør": "start"}},
#         "øst": {"beskrivelse": "Det er en drage som vokter en skatt.", "utforsket": False, "valg": {"vest": "start"}},
#         "skattkammer": {"beskrivelse": "Du har funnet skatten! Gratulerer!", "utforsket": False, "valg": {}}
#     }
    
#     inventar = []
#     nåværende_rom = "start"

#     def vis_inventar():
#         if inventar:
#             print("Du har følgende i inventaret ditt: " + ", ".join(inventar))
#         else:
#             print("Inventaret ditt er tomt.")

#     def hjelp():
#         print("Kommandoer: nord (n), øst (ø), sør (s), vest (v), inventar (i), hjelp (h)")

#     while True:
#         print(rom[nåværende_rom]["beskrivelse"])

#         if not rom[nåværende_rom]["utforsket"]:
#             rom[nåværende_rom]["utforsket"] = True

#         valg = input("Hva vil du gjøre? (h for hjelp) ").strip().lower()

#         if valg in ["n", "ø", "s", "v"]:
#             retning = {"n": "nord", "ø": "øst", "s": "sør", "v": "vest"}[valg]
#             if retning in rom[nåværende_rom]["valg"]:
#                 nåværende_rom = rom[nåværende_rom]["valg"][retning]
#                 if nåværende_rom == "nord":
#                     inventar.append("sverd")
#                     print("Du har nå et sverd!")
#                 elif nåværende_rom == "øst" and "sverd" in inventar:
#                     print("Du bruker sverdet ditt og beseirer dragen! Du har funnet skatten!")
#                     nåværende_rom = "skattkammer"
#                     break
#                 elif nåværende_rom == "øst":
#                     print("Dragen er for sterk for deg. Du må finne et våpen.")
#                     nåværende_rom = "start"
#             else:
#                 print("Du kan ikke gå den veien.")
#         elif valg == "i":
#             vis_inventar()
#         elif valg == "h":
#             hjelp()
#         else:
#             print("Ugyldig kommando. Prøv igjen.")

# eventyr()