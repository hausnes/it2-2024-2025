'''
    Oppgave 2: Quiz
    Denne versjonen av quizen tek v1 eit steg vidare, og ser i større grad på korleis
    ein kan handtere fleire svaralternativ for naboland, samt korleis ein kan handtere
    innbyggjartal som heiltal - og godta eit svar innan +-10%.
'''

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

# Funksjon som stiller eit spørsmål om eit tilfeldig land og eit tilfeldig faktaspørsmål
def ask_question():
    # Velger eit tilfeldig land frå data-dictionaryen
    country = random.choice(list(fakta.keys()))
    # Velger eit tilfeldig attributt/fakta frå landet
    attribute = random.choice(list(fakta[country].keys()))
    
    # Henter det korrekte svaret frå data-dictionaryen
    answer = fakta[country][attribute]
    
    # Printar spørsmålet
    print(f"What is the {attribute} of {country}?")
    
    # Henter brukarinput
    user_answer = input()

    # Sjekker om attributtet er "population" (altså forventar me eit tal)
    if attribute == "population":
        try:
            user_answer = int(user_answer)
            lower_bound = answer * 0.9
            upper_bound = answer * 1.1
            if lower_bound <= user_answer <= upper_bound:
                print("Correct!")
            else:
                print(f"Wrong. The correct answer is {answer}.")
        except ValueError:
            print(f"Invalid input. The correct answer is {answer}.")
    
    # Sjekker om attributtet er "neighbors" (altså forventar me potensielt fleire svar)
    elif attribute == "neighbors":
        user_neighbors = [n.strip().lower() for n in user_answer.split(",")]
        correct_neighbors = [n.lower() for n in answer]
        if sorted(user_neighbors) == sorted(correct_neighbors):
            print("Correct!")
        else:
            print(f"Wrong. The correct answer is {', '.join(answer)}.")

    # Dersom attributtet ikkje er "population" eller neighbors
    else: 
        # Sjekker om brukarinput er likt det korrekte svaret
        if user_answer == answer or user_answer in answer:
            print("Correct!")
        else:
            # Opplyser om at svaret er feil, og viser det korrekte svaret
            print(f"Wrong. The correct answer is {answer}.")

# For å starte quizen:
ask_question()