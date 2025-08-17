import requests, sqlite3

# TODO 1: vervang URL door te doorzoeken webpagina.
URL = "https://thesmartbarn.netlify.app" 
html_code = requests.get(URL).text

# Overloop iedere regel HTML-code apart.
for regel in html_code.split("\n"):
    if "href" in regel: # TODO 2: ALS regel een link bevat...
        print("##############")
        print(regel)
        print("##############")

naam  = "NAAM OPGEGEVEN TIJDENS LOGIN"
query = f"SELECT * FROM account_tabel WHERE naam=?"
account = sqlite3.executequery(query, (naam))