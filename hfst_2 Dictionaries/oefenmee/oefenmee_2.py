# Start de oefen mee met onderstaande dictionary.
fruitmand = { # Sleutel is fruit, waarde is aantal
    "appel": 5,
    "banaan": 3,
    "kers": 50,
   
}
nieuw_fruit  = "mango"
nieuw_aantal = 1
fruitmand[nieuw_fruit] = nieuw_aantal
fruit = "banaan"
nieuw_aantal = 8
fruitmand[fruit] = nieuw_aantal
fruit = "kers"
nieuw_aantal = 43
fruitmand["kers"] = fruitmand["kers"] - nieuw_aantal
terugleggen_fruit = "kers"
fruitmand.pop(terugleggen_fruit)
print(fruitmand)
