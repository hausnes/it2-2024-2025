fakta = {
    "Norway" : {
        "capital" : "Oslo",
        "population" : 5378857,
        "neighbors" : ["Sweden", "Finland", "Russia"]
    },
    "Sweden" : {
        "capital" : "Stockholm",
        "population" : 10099265,
        "neighbors" : ["Norway", "Finland"]
    },
    "Finland" : {
        "capital" : "Helsinki",
        "population" : 5540720,
        "neighbors" : ["Sweden", "Norway", "Russia"]
    },
    "Russia" : {
        "capital" : "Moscow",
        "population" : 144526636,
        "neighbors" : ["Finland", "Norway"]
    }
}

import random

tilfeldige_sporsmal = random.sample(fakta.keys(), 3)

print(tilfeldige_sporsmal)