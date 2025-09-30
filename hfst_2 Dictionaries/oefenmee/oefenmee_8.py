# Start de oefen mee met onderstaande dictionary.
steden_temp = { # Sleutel is stad, waarde is temp 
    "Hasselt": 25,
    "Oostende": 21,
    "Antwerpen": 24,
    "Brussel": 23,
    "Luik": 23,
    "Namen": 24
}
for stad in steden_temp:
    stad = input("In welke stad bent u? ")
    temp = steden_temp.get(stad)
    if stad not in steden_temp:
        print(f"Het is hier ??? °C. ")
    if stad in steden_temp:
        print(f"Het is hier {temp}°C. ")
    
