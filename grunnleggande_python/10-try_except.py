# Eksempel 1, frå boka, kap. 1C, "validering av input"
gyldig = False

while not gyldig:
    tall = input("Skriv et tall: ")

    try:
        tall = int(tall)
        gyldig = True
    except ValueError:
        print("Du må skrive inn et heltall.")

print(f"Du skrev inn {tall}.")

# Eksempel 2, med litt utvidelsar
gyldig = False

try:
    while not gyldig:
        tall = input("Skriv et positivt tall: ")

        try:
            tall = int(tall)
            if tall > 0:
                gyldig = True
            else:
                print("Tallet må være større enn 0.")
        except ValueError:
            print("Du må skrive inn et heltall.")
except KeyboardInterrupt:
    print("\nProgrammet ble avbrutt av brukeren.")