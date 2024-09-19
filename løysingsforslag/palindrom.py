def er_palindrom(s):
    # Fjerner mellomrom og gjør strengen til små bokstaver
    s = s.replace(" ", "").lower()
    # Sjekker om strengen er lik sin reverserte versjon
    return s == s[::-1]

def er_palindrom_alternativ(s):
    # Fjerner mellomrom og gjør strengen til små bokstaver
    s = s.replace(" ", "").lower()
    
    # Initialiserer to pekere, en på starten og en på slutten av strengen
    start = 0
    slutt = len(s) - 1
    
    # Sjekker tegnene fra start og slutt mot midten
    while start < slutt:
        if s[start] != s[slutt]:
            return False
        start += 1
        slutt -= 1
    
    return True

# Eksempel på bruk
test_streng = "A man a plan a canal Panama"
print(er_palindrom(test_streng))  # Output: True
print(er_palindrom_alternativ(test_streng)) # Output: True