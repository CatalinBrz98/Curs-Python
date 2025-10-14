import random

import pandas as pd

import matplotlib.pyplot as plt

if __name__ == "__main__":
    numes = [
        "Andrei", "Maria", "Ioana", "Mihai", "Elena", "George", "Ana", "Vlad", "Diana", "Radu",
        "Carmen", "Alexandru", "Cristina", "Ionut", "Gabriela", "Stefan", "Oana", "Robert", "Bianca", "Daniel",
        "Alina", "Catalin", "Raluca", "Lucian", "Lavinia", "Paul", "Denisa", "Florin", "Madalina", "Cosmin",
        "Georgiana", "Adrian", "Monica", "Victor", "Laura", "Claudiu", "Teodora", "Emil", "Simona", "Sebastian",
        "Cezar", "Irina", "Tudor", "Anca", "Roxana", "Nicolae", "Cristian", "Alexandra", "Sorin", "Patricia"
    ]

    orase = [
        "Bucuresti", "Cluj-Napoca", "Timisoara", "Iasi", "Constanta",
        "Brasov", "Sibiu", "Oradea", "Arad", "Ploiesti", None
    ]

    # Dictionar pentru DataFrame
    data = {
        "Nume": random.choices(numes, k=50),
        "Varsta": [random.randint(18, 65) for _ in range(50)],
        "Oras": random.choices(orase, k=50)
    }

    df = pd.DataFrame(data)

    # groups = df.groupby("Oras")
    # for group in groups:
    #     print(group[0])
    #     print(group[1])
    #     print(group[1]["Varsta"].mean())
