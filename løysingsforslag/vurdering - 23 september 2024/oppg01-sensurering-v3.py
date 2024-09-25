'''
    Oppgåve 1: Sensurering, v3
'''
import random

# Problematiske ord som skal sensurast:
problematiske_ord = ["fis", "stygtord1", "stygtord2", "stygtord3", "stygtord4"]

# Setning som skal sensurerast:
setning = "Dette er ein tekst med fisen og stygtord1 og stygtord2 og stygtord3 og stygtord4."

# Funksjon som skal sensurere setningar:
def sensurer(setning, problematiske_ord, erstatningTegn = True): # erstatningTegn er ein valgfri parameter, som default er True
    for ord in problematiske_ord:
        if erstatningTegn: # Som i at me ynskjer å erstatte stygge ord med *
            setning = setning.replace(ord, "*" * len(ord))
        else: # Som i at me ynskjer å erstatte stygge ord med "søte erstatningsord"
            setning = setning.replace(ord, random.choice(["prompen", "erstatningsord2", "erstatningsord3", "erstatningsord4"]))

    # Returner den sensurerte setninga:
    return setning

# Sensurerer setninga:
print(sensurer(setning, problematiske_ord))
print(sensurer(setning, problematiske_ord, False))