def gestion_course() :

   liste_course = []

   def ajouter():
        entrer = input("Entrez nouveau element : ")
        liste_course.append(entrer)
        print("un element ajouté !")
    
   def retirer():
        entrer = input("Ecrivez élément à rétirer : ")
        for i in liste_course :
            if entrer == i :
                liste_course.remove(entrer)
                print("L'element {} à ete supprimé de laliste_course".format(entrer))
                break 
            else:
                print("Votre élément ne figure pas dans la liste des courses.")
                break

   def afficher():
        print(liste_course)

   def vider():
         liste_course.clear()
   def quiter():
       entrer = input("Voulez vous quitter o/n ? ")
       if entrer == "o":
           exit()
       else :
           gestion_course()
       
   while True :
      print("1. Ajouter")
      print("2. Retirer")
      print("3. Afficher")
      print("4. Vider")
      print("5. Quitter") 
      resultat = int(input("Choississez votre action : "))
      if resultat == 1:
         ajouter()
      elif resultat == 2 :
         retirer()
      elif resultat == 3 :
         afficher()
      elif resultat == 4 :
         vider() 
      elif resultat == 5 :
          quiter()            
      else:
        print("Veuillez choisir un chiffre allant de 1 à 5 pour taches !")

gestion_course()