'''
MÅ ikkje bruke same standard som boka beskriv, 
men hald deg i det minste til ein standard!
'''

# Om å vere tydeleg nok i navngjevinga:
lengde = 4
bredde = 3
areal = lengde * bredde
# eller..
lengdeRektangel = 5
breddeRektangel = 4
arealRektangel = lengdeRektangel * breddeRektangel
# eller..
lengde_rektangel = 3
# eller..
rektangelLengde = 5
rektangelBredde = 4
rektangelAreal = rektangelLengde * rektangelBredde

# Konstantar - bruk berre store bokstavar - skal ikkje endrast i koden
LYSETS_HASTIGHET = 300000 # Lysets hastighet i km/s
PI = 3.14
# Apropos pi..
import math
PI_LANG = math.pi

# Spesifisere at det er input frå bruker (?)
inputSideA = float(input("Side A: "))

# Når me kjem til funksjonar, hugs å typisk bruke verb for å beskrive kva som blir gjort
def regnUtArealRektangel(sideA, sideB):
    areal = sideA * sideB
    return areal

print(regnUtArealRektangel(4,7))