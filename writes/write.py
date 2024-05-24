import json
chemin = "C:/Users/leapa/Downloads/Bureau/Tuto-python/dossier_2/fichier.json"
with open(chemin, "r") as f :
    lecture = json.load(f)
    print(lecture)

lecture.append(8)

with open(chemin, "w") as d:
     json.dump(lecture, d)
  