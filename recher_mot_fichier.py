#version plus amelioré de mon code pour une recherche très exhaustive

from pathlib import Path

def recherche():
    chemin = Path.home()
    liste = []
    entrer = input("Entrez le mot à rechercher ! : ").lower()

    if chemin.exists() and chemin.is_dir():
        try:
            # Recherche récursive pour parcourir tous les sous-dossiers
            for dossier in chemin.rglob('*'): # il recupère tout les dossiers dont  l"extension commence par "*"
            # il recherche dans tous les sous-dossiers et fichiers de manière récursive.
                if entrer in dossier.name.lower():
                    liste.append(dossier.name)

        except PermissionError:
            print(f"Permission refusée pour accéder à certains fichiers ou dossiers dans {chemin}.")

    if liste:
        print(f"Voici le(s) chemin(s) pour votre mot de recherche '{entrer}' :")
        for i, fich_dossier in enumerate(liste, 1):
            print(f"{i}. {fich_dossier}")
    else:
        print(f"Le mot de recherche '{entrer}' n'existe pas dans le répertoire.")

recherche()
# version simple dans un repertoir 
"""from pathlib import Path
chemin = Path.home()
liste = []
def recherche():
    entrer = input("Entrez le mot rechercher! : ").lower()
    if chemin.exists() and chemin.is_dir():
        for dossier in chemin.iterdir():
            if entrer == dossier.name.lower() :
                liste.append(dossier)

    if liste:            
        print(f" voici le chemin de votre mot de recherche {entrer} :")
        for fich_dossier in liste:
            print(fich_dossier)
            
    else:
        print(f"votre mot de recherche '{entrer}', n'existe pas dans le repertoire.")    
recherche()
"""
