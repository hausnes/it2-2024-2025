'''
Oppgave 15 fra kapittel 1A:
---------------------------
Vi har en rettvinklet trekant.
Vi kjenner en vinkel (60 grader) og den hosliggende kateten (7).
Vi ønsker å finne hypotenusen (x).
Python's math-bibliotek bruker radianer, så vi må konvertere grader til radianer.
'''

import math

# Gitt informasjon
vinkel_grader = 60
hosliggende_katet = 7

# Konverter grader til radianer
vinkel_radianer = math.radians(vinkel_grader)

# Bruk cosinus for å finne hypotenusen
# cos(vinkel) = hosliggende_katet / hypotenus
# Dermed: hypotenus = hosliggende_katet / cos(vinkel)
hypotenus = hosliggende_katet / math.cos(vinkel_radianer)

print("Hypotenusen er:", hypotenus)