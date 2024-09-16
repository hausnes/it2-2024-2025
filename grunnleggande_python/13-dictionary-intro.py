person = {
  "fornavn": "Per", 
  "etternavn": "Christensen"
}
# Eksempel på korleis skrive ut utvalt del
print(person["etternavn"])
# Nyttig å vite at me kan spesifisere keys, values og items
print(person.keys())
print(person.values())
print(person.items())

personer = {
    "999999-99999": {
        "fornavn"   : "Jo Bjørnar",
        "etternavn" : "Hausnes"
    },
    "000000-00000": {
        "fornavn"   : "Jo Bjarne",
        "etternavn" : "Hausnesia"
    }
}
# Eksempel på korleis skrive ut utvalt del
print(personer["000000-00000"]["fornavn"])

norske_byer = {
    "Oslo": {
        "innbyggere": 697899, 
        "fylke": "Oslo", 
        "landemerker": ["Holmenkollen", "Vigelandsparken", "Operaen"] 
    },
    "Bergen": {
        "innbyggere": 298969, 
        "fylke": "Vestland", 
        "landemerker": ["Bryggen", "Fløyen", "Fisketorget"] 
    },
    "Trondheim": {
        "innbyggere": 209462, 
        "fylke": "Trøndelag", 
        "landemerker": ["Nidarosdomen", "Tyholttårnet", "Gamle Bybro"] 
    },
    "Stavanger": {
        "innbyggere": 148289, 
        "fylke": "Rogaland", 
        "landemerker": ["Preikestolen", "Oljemuseet", "Domkirken"] 
    }
}
# Eksempel på korleis skrive ut utvalt del
print(norske_byer["Bergen"]["landemerker"])
# Eksempel på korleis skrive ut utvalt del vha løkke
for landemerke in norske_byer["Bergen"]["landemerker"]:   
    print(f"{landemerke}.")