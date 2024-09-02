'''
    Oppgåve: Lag eit system som handterer innlogging. 
    Ha eit fokus på korleis du kan sjekke kriterier på best måte (kva er "best"?).
    Brukaren må skrive inn brukarnavn og passord, og skal få tydelege feilmeldingar.
    NB: Særs forenkla når det gjeld lagring av brukarnavn og passord, kryptering mm. 
'''
innlogga = False

brukarnavnFraaDatabase = "Brukar01"
passordFraaDatabase = "Passord01"

while not innlogga:
    # Brukarnavn
    brukarnavn = input("Ditt brukarnavn: \n")
    if brukarnavn != brukarnavnFraaDatabase:
        print("Brukaren eksisterer ikkje.")
        break

    # Passord
    passord = input("Ditt passord: \n")
    if passord != passordFraaDatabase:
        print("Feil passord.")
        break

    innlogga = True

'''
    Ein litt meir avansert løysning med kryptering av passord, 
    og ein "database" med brukarnamn og passord.
    Merk at det ikkje blir spesifisert om brukaren har skrive 
    inn feil brukarnamn eller passord. Kvifor det, trur du?
'''
# import bcrypt

# # Simulert database med brukarnavn og hashed passord
# brukere = {
#     "Brukar01": bcrypt.hashpw("Passord01".encode('utf-8'), bcrypt.gensalt())
# }

# innlogga = False
# forsok = 0
# maks_forsok = 3

# while not innlogga and forsok < maks_forsok:
#     brukarnavn = input("Ditt brukarnavn: \n")
#     passord = input("Ditt passord: \n").encode('utf-8')

#     if brukarnavn in brukere and bcrypt.checkpw(passord, brukere[brukarnavn]):
#         innlogga = True
#         print("Innlogging vellykket!")
#     else:
#         forsok += 1
#         print(f"Feil brukernavn eller passord. Du har {maks_forsok - forsok} forsøk igjen.")

# if not innlogga:
#     print("For mange mislykkede forsøk. Tilgang nektet.")