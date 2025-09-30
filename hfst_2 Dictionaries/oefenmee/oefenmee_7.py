# Start de oefen mee met onderstaande dictionary.
gasten = { # Sleutel is naam, waarde is job.
    "Jan":     "reporter",
    "Piet":    "acteur",
    "Joris":   "regisseur",
    "Korneel": "scenarist"
}
conditie = True
while conditie:
    naam = input("Wat is jouw naam? ")
    if naam not in gasten and not "STOP":
            print(f"De naam {naam} staat niet op de lijst.  ")
    elif naam in gasten:
        job = gasten[naam]
        print(f"Welkom {job} {naam}, kom binnen. ")
        gasten.pop(naam)
    elif "STOP":
        conditie = False