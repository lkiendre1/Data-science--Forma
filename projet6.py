from pathlib import Path
chemin = "C:/Users/leapa/Downloads/Bureau/Tuto-python/cree-dossier"
    #"ENTREZ UN CHEMIN DE DOSSIER DANS LEQUEL CRÉER LA STRUCTURE"
 

def createur_dossier(objet):
    

    d = {"Films": ["Le seigneur des anneaux",
                "Harry Potter",
                "Moon",
                "Forrest Gump"],
        "Employes": ["Paul",
                    "Pierre",
                    "Marie"],
        "Exercices": ["les_variables",
                    "les_fichiers",
                    "les_boucles"]
            }

    objet = Path(objet)# creation d'un object "objet"
    for dossiers, sous_dossiers in d.items():# iteration sur notre dictionnaire 
        #pour recuperer les cles et les valeurs qu'on va transformer en dossiers et sous dossiers
        dossier = objet/dossiers # creation d'un chemin vers notre dossier
        dossier.mkdir(parents = True, exist_ok = True) # si le dossier exixte ok sinon cree le 
        for sous_dossier in sous_dossiers :
            fichier2 = dossier / sous_dossier
            fichier2.mkdir(parents = True, exist_ok = True)

createur_dossier(chemin) # "chemin" represente le chemin qui mène vers le dossier principale ou les creations se feront   