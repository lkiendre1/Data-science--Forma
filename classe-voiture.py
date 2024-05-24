'''Dans cet exercice sur la programmation orientée objet, vous allez devoir créer une classe
Voiture, qui doit contenir plusieurs attributs et méthodes afin de la faire fonctionner 
correctement.
1- Créez une classe voiture avec un attribut essence qui est égal à 100.
2- Créez une méthode afficher_reservoir qui affiche le nombre de litres d’essence restant
(La voiture contient x litres d’essence).
3- Créez une méthode roule avec un paramètre km (kilomètre) qui va faire avancer la voiture 
et vider petit à petit le réservoir. On considère une consommation de 5L pour 100km
4- Si le réservoir est vide quand on essaie de rouler, afficher la phrase : 
Vous n'avez plus d'essence, faites le plein ! et empêchez la voiture d’avancer.
5- Si la jauge d’essence descend en dessous de 10L, affichez la phrase : 
Vous n'avez bientôt plus d'essence !
6- Créez une méthode faire_le_plein qui remet le niveau d’essence à 100L et qui affiche
 la phrase Vous pouvez repartir !'''

from dataclasses import dataclass

@dataclass
class Voiture:
    essence: int = 100  # Essence par défaut

    def afficher_reserv(self):
        print("La voiture contient {} litres d'essence".format(self.essence))

    def roule(self):
        consommation_litre_km = 0.05
        metrage = int(input("Entrez le kilométrage : ")) 
        observation_litrage = metrage * consommation_litre_km
        if observation_litrage < 10:
            print("Vous n'avez bientôt plus d'essence")
            print("Vous avez consommé {} litre(s) d'essence".format(observation_litrage))
        elif observation_litrage == 0:
            print("Vous n'avez plus d'essence, faites le plein!")
        else:
            print("Vous avez assez de carburant pour arriver à destination!")

        # Mettre à jour le niveau d'essence après le roulement
        self.essence -= observation_litrage
        # Actualiser l'affichage du réservoir
        self.afficher_reserv()

    def faire_le_plein(self):
        self.essence = 100
        print("Vous avez fait le plein!")

# Boucle pour répéter les opérations jusqu'à ce que l'utilisateur choisisse de quitter
while True:
    print("1. Afficher réservoir")
    print("2. Démarrer")
    print("3. Faire le plein")
    print("4. Quitter")

    entrer = int(input("Quelle option choisissez-vous ? "))

    info_1 = Voiture()  # Instanciation de la voiture

    if entrer == 1:
        info_1.afficher_reserv()
    elif entrer == 2:
        info_1.roule()
    elif entrer == 3:
        info_1.faire_le_plein()
    elif entrer == 4:
        print("Au revoir !")
        break
    else:
        print("Option invalide. Veuillez choisir une option valide.")

