import requests, json
lng_gebruiker = float(input("Wat is uw longitude "))
lat_gebruiker = float(input("Wat is uw latitude "))
url = f"https://api.sunrisesunset.io/json?lat={lat_gebruiker}&lng={lng_gebruiker}"
response_json = requests.get(url).json()

with open("hfst_4 API\oefenmee\sunrisesunset_io.json", "w" )as fp:
    json.dump(response_json, fp)