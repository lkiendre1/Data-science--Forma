def trieur():
    from pathlib import Path
    
    # Définition du chemin du dossier contenant les fichiers
    chemin = Path("C:/Users/leapa/Downloads/Bureau/Tuto-python/projet6_letrieur/data")
    
    # Définition des associations entre les extensions et les catégories
    dictionnaire = {
        "Images": ["*.bmp", "*.png", "*.jpg"],
        "Videos": ["*.avi", "*.mp4", "*.gif"],
        "Documents": ["*.txt", "*.pptx", "*.csv", "*.xls", "*.odp", "*.pages"],
        "Musique": ["*.mp3", "*.wav", "*.flac"],
        "Divers": []
    }

    # Initialisation du dictionnaire pour stocker les fichiers triés
    fichiers = {cle: [] for cle in dictionnaire.keys()}
    
    # Fonction pour trier les fichiers selon leurs extensions
    def trieur_fichier():
        for cle, extensions in dictionnaire.items():
            for ext in extensions:
                fichiers[cle].extend(chemin.glob(ext))

    # Appeler la fonction pour trier les fichiers
    trieur_fichier()
    
    # Afficher les fichiers correspondant à la catégorie spécifiée par l'utilisateur
    def affichage(cle):
        print(f"Affichons les fichiers de la catégorie '{cle}':")
        for fichier in fichiers[cle]:
            print(fichier.name)

    # Boucle pour permettre à l'utilisateur de choisir une catégorie
    while True:
        try:
            print("Que souhaitez-vous afficher ?")
            print("1- Images")
            print("2- Vidéos") 
            print("3- Documents") 
            print("4- Musique")
            print("5- Divers")
            print("6- Quitter")
            entree = int(input("Choisissez votre action : "))
            if entree == 1:
                affichage("Images")
            elif entree == 2:
                affichage("Videos")
            elif entree == 3:
                affichage("Documents")
            elif entree == 4:
                affichage("Musique")
            elif entree == 5:
                affichage("Divers")
            elif entree == 6:
                print("Au revoir !")
                break
            else:
                print("Veuillez choisir un numéro valide !")    
        except ValueError:
            print("Veuillez entrer un numéro valide !")

# Appeler la fonction principale
trieur()
