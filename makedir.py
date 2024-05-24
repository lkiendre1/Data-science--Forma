import os

chemin = "/Users/leapa/tuto-sqlite/sqlite"
dossier = os.path.join(chemin, "dossier")
creation = os.makedirs("dossier")
print(creation)