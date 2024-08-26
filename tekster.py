# Eksempel på bruksområde for deler av fagtoffet..
filnavn = "Joe Bjørnars - Dans, Dans, Dans.mp3"
filtype = filnavn[-3:]
print(filtype)

# Leite etter "noko" i ein string
interesse = "chips og VuRdErinGsarbeid"
if "vurdering" in interesse.lower():
    print("Min venn")
else:
    print("...")

# Erstatte innhald
navn = "Jo Bjørnar Hausnes"
domene = "@skule.no"
epost = navn.replace(" ",".").lower().replace("ø","o")
print(epost)

# Begrense antall desimalar
import math
print(math.pi)
print(f"{math.pi:.2f}")

# Om å sette av nok plass
radius1 = 8
areal1 = math.pi*radius1**2

radius2 = 72.3
areal2 = math.pi*radius2**2

print(f"Arealet av en sirkel med radius {radius1:5} er {areal1:8.2f}.")
print(f"Arealet av en sirkel med radius {radius2:5} er {areal2:8.2f}.")