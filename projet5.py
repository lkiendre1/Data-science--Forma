import random

def jeu_nombre():
    utilisateur = 50
    enemie = 50
    potion = 3
    
    def joueur():
        nonlocal utilisateur, enemie, potion
        while True:
            try:
                entree_1 = int(input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? : "))
                if entree_1 == 1:
                    if enemie > 0:
                        coup = random.randint(5, 10)
                        enemie -= coup
                        print(f"Bravo, votre adversaire vient de perdre {coup} point(s) de vie !")
                        if enemie <= 0:
                            print("Ennemi à terre ! Vous avez gagné !")
                            break
                    else:
                        print("L'ennemi est déjà à terre !")
                elif entree_1 == 2:
                    if potion > 0:
                        bonus = random.randint(15, 50)
                        utilisateur += bonus
                        print(f"Vous avez récupéré {bonus} points de vie. Vous êtes à {utilisateur} points de vie.")
                        potion -= 1
                    else:
                        print("Vous n'avez plus de potions.")
                else:
                    print("Entrée incorrecte ! Veuillez choisir 1 ou 2.")
                
                if enemie > 0:
                    adversaire()
                if utilisateur <= 0:
                    print("Vous avez été vaincu par l'adversaire. Game Over !")
                    break

            except ValueError:
                print("Veuillez saisir un nombre valide.")
                
    def adversaire():
        nonlocal utilisateur
        perte_vie = random.randint(5, 15)
        utilisateur -= perte_vie
        print(f"L'adversaire attaque ! Vous venez de perdre {perte_vie} points de vie. Il vous reste {utilisateur} points de vie.")
        
    debuter = input("Débutez votre jeu en tapant 'ok' ou 'quitter' pour quitter : ").lower()
    while debuter == "ok":
        joueur()
        if utilisateur <= 0 or enemie <= 0:
            break
        debuter = input("Tapez 'ok' pour rejouer ou 'quitter' pour quitter : ").lower()

jeu_nombre()
