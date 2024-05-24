import json
import os

def execution():
    chemin = "C:/Users/leapa/Downloads/Bureau/Tuto-python/listes-cours"
    fichier_json = "liste.json"
    acces = os.path.join(chemin, fichier_json)
    
    def charger_liste():
        if os.path.exists(acces):
            try:
                with open(acces, "r") as f:
                    return json.load(f)
            except Exception as e:
                print(f"Erreur lors de la lecture du fichier JSON : {e}")
        else:
            print("Le fichier n'existe pas.")
            return []

    def sauvegarder_liste(liste):
        with open(acces, "w") as f:
            json.dump(liste, f, indent=4)
    
    def ajouter():
        liste_courses = charger_liste()
        ajout = input("Entrez le nom de la course à ajouter : ")
        liste_courses.append(ajout)
        sauvegarder_liste(liste_courses)
    
    def retirer():
        liste_courses = charger_liste()
        retire_course = input("Choisissez la course à retirer : ").lower()
        if retire_course in liste_courses:
            liste_courses.remove(retire_course)
            sauvegarder_liste(liste_courses)
        else:
            print("Cette course n'existe pas dans la liste.")

    def afficher():
        liste_courses = charger_liste()
        print("Liste des courses :")
        for course in liste_courses:
            print(course)

    def vider():
        if input("Voulez-vous vraiment vider la liste de courses ? (o/n) : ").lower() == "o":
            sauvegarder_liste([])
            print("La liste de courses a été vidée.")

    while True:
        print("1- Ajouter")
        print("2- Retirer")
        print("3- Afficher")
        print("4- Vider")
        print("5- Quitter")
        action = input("Choisissez votre action (1-5) : ")
        if action == "1":
            ajouter()
        elif action == "2":
            retirer()
        elif action == "3":
            afficher()
        elif action == "4":
            vider()
        elif action == "5":
            print("Au revoir !")
            return
        else:
            print("Veuillez entrer un nombre entre 1 et 5.")

execution()
