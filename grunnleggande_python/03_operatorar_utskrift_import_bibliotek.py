# Meir om utskrifter
print(f"Ei utskrift kan ha \nlinjeskift.")
print(f'''
Ei utskrift kan gå
over fleire linjer
dersom du har problem med
å
få plass.
''') # NB: Kan òg bruke """..."""

# Operatorar, utgangspunkt for eksempla under
tall1 = 3
tall2 = 4
tall3 = 2
resultat = 0

# Pluss
resultat = tall1 + tall2 + tall3
print(f"Pluss: {tall1} + {tall2} + {tall3} = {resultat}")

# Minus
resultat = tall1 - tall3
print(f"Minus: {tall1} - {tall3} = {resultat}")

# Gange
resultat = tall1 * tall2
print(f"Ganging: {tall1} * {tall2} = {resultat}")

# Dele
resultat = tall1 / tall3
print(f"Deling: {tall1} / {tall3} = {resultat}")

# Eksponent
resultat = tall1**tall3
print(f"Eksponent: {tall1} opphøyd i {tall3} = {resultat}")

'''
Frå bok:
Python følger samme regnerekkefølge som du er vant til.
Det vil si at eksponenter beregnes først,
deretter multiplikasjon/divisjon
og til sist addisjon/subtraksjon.

Hvis en utregning inneholder flere operatorer som skal
utføres samtidig, vil de bli utført fra venstre mot høyre.

NB: Bruk parantesar for å overstyre.
'''

# Heiltalsdivisjon og modulus (rest ved divisjon)
speletidMinutter = 124 # minutt
antallTimar = speletidMinutter // 60 # heiltalsdivisjon
rest = speletidMinutter % 60 # Modulus
print(f"""
Ein film med speletid på {speletidMinutter} minutt
varar i
- {antallTimar} timar, og
- {rest} minutt.
""")

'''
Frå bok:
I tillegg til de vanlige regneoperasjonene har vi også
tilgang til heltallsdivisjon (//) og modulus (%) i Python.
Heltallsdivisjon gir oss resultatet av vanlig divisjon,
men uten resten (desimalene blir strøket). Hvis vi skriver
13 // 2, får vi vite hvor mange ganger 2 går opp i 13,
altså 6. Modulus gjør det omvendte, det vil si at vi bare
får resten som resultat. Da vil 13 % 2 gi 1, fordi 13 delt
på 2 blir 6 med 1 i rest.
'''

# Math-biblioteket og innebygde konstantar og funksjonar
import math
tall = 9
print(f"Kvadratrota av {tall} er {math.sqrt(tall)}.")
# Andre kjekke ting å kjenne til frå math-biblioteket er ...
