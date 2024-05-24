'''Dans cet exercice, nous avons un dictionnaire qui représente plusieurs employés
d'une entreprise avec differents id.
1.Patrick a quitté l'entreprise cette année, nous devons donc l'enlever du dictionnaire
2. Julie a fêté son anniversaire hier, il faut donc changer son âge(elle a maintenant 26 ans).
3. Paul quant à lui fêtera son anniversaire la semaine prochaine. Nous voulons donc récupérer 
son âge  pour savoir quel âge il aura.
Il faudra également récupérer l'âge de Paul dans une variable 'age_paul', qui devra donc être égale à 32.
Notre dictionnaire  d'entrée est comme ceci:
'''
employes = {
       "id01": {"prenom": "Paul", "nom": "Dupont", "age": 32},
       "id02": {"prenom": "Julie", "nom": "Dupuit", "age": 25},
       "id03": {"prenom": "Patrick", "nom": "Ferrand", "age": 36}
}
clean_id03 = employes.pop('id03')
employes["id02"]["age"] = 26
age_paul = employes["id01"]["age"]
print(age_paul)
print(employes)
