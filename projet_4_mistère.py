'''import random

def mistere():            
        essaie = 5
        i = 0
        print("Bienvenu dans le jeu des nombres mistères!")
        nombre_aleatoire = random.randint(0,100)
        while i < essaie :
            try:               
                print("Vous avez {} essaies.".format(essaie - i))
                entree = int(input("Entree votre nombre! : "))       
                if nombre_aleatoire == entree:
                        print("vous avez gagné la partie!")
                        print("nombre d'essaie, {} fois!".format(i))
                        break
                else:
                    if entree > nombre_aleatoire:
                        print("votre nombre est superieur au nombre genere par l'ordi!")                          
                    else:
                        print("votre nombre est inferieur au nombre genere par l'ordi!")

                i += 1
                if i == essaie:
                    print("Fin de la partie!")
            except ValueError:
                  print("Veullez rentrer un bon numéro.")
                  continue       
mistere()''' 

import random

def mystere():
    essais = 7
    i = 0
    nombre_aleatoire = random.randint(0, 100) # emission du nombre aleatoire
    print("Bienvenue dans le jeu des nombres mystères!")
    print("Vous avez {} essais pour deviner un nombre entre 0 et 100.".format(essais))

    while i < essais:# tant que i est inferieur à essaie le jouer peut toujours tenter sa chance 
        try:
            print("Vous avez {} essais restants.".format(essais - i))
            entree = int(input("Entrez votre nombre : "))

            if nombre_aleatoire == entree:
                print("Vous avez gagné la partie!")
                print("Nombre d'essais utilisés : {}.".format(i + 1))
                break
            else:
                if entree > nombre_aleatoire:
                    print("Votre nombre est supérieur au nombre généré par l'ordinateur!")
                else:
                    print("Votre nombre est inférieur au nombre généré par l'ordinateur!")

            i += 1
            if i == essais:
                print("Fin de la partie! Le nombre était : {}".format(nombre_aleatoire))
        except ValueError:
            print("Veuillez entrer un numéro valide.")
            continue

mystere()


   


    

