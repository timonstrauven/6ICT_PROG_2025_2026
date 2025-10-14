# Maak voor deze oefen mee gebruik van onderstaande dictionary van dictionaries.
spelinfo = {
    'speler1': {
        'naam': 'Alice',
        'positie': {
            'x': 10,
            'y': 5
        },
        'inventaris': {
            'wapen': 'zwaard',
            'goud': 50
        }
    },
    'speler2': {
        'naam': 'Bob',
        'positie': {
            'x': 2,
            'y': 8
        },
        'inventaris': {
            'wapen': 'boog',
            'goud': 9999999999
        }
    }
}
#niveau_2
# print(spelinfo["speler2"]["naam"])
# print(spelinfo["speler1"]["positie"])
# print(spelinfo["speler2"]["inventaris"]["wapen"])

# niveau_3
# goud = 0
# spelinfo['speler2']['inventaris']['goud'] = goud
# print(spelinfo['speler2']['inventaris']['goud'])

# niveau_4
spelinfo['speler1']['hacker'] = True
spelinfo['speler2']['hacker'] = False
spelinfo['speler1']['inventaris']['bepantsering'] = "schild"
print(spelinfo)