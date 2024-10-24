# from typewriter_effect import *
# eller
import typewriter_effect as jbh # Gjer det tydelegare at det er ditt eige..?

setning = "Jo Bjørnar Hausnes elskar OOP."

# Eksempel 1
print("Standard bruk av print:")
print(setning)

# Eksempel 2
print("Eigendefinert 'typewriter', med kjapp standardinnstilling:")
jbh.skrivUt(setning) # Kjapt er satt som standard, kunne skrive ", True" om me ville vere tydeleg

# Eksempel 3
print("Eigendefinert 'typewriter', med spesifisert treig innstilling:")
jbh.skrivUt(setning, False)