#coding: utf-8

#tous les possibles débuts de matricule selon les années
annees1 = list(range(0,18))
annees2 = list(range(30,100))

#fusionner les deux lists
annees2.extend(annees1)

#format pour garder que les deux derniers chiffres des années
annee = ['{:02}'.format(annee) for annee in annees2]

#toutes les fins de matricule possibles
numeros = ['{:03}'.format(numeros) for numeros in range(1, 1000)]

#pour chaque année, ajouter toutes les fins de matricule possibles
matricule = []
for an in annee:
  for numero in numeros:
  	print(an + numero) ### Mon ajout
    # matricule.append(an + numero)

# print(matricule)


### Mes commentaires sont précédés de trois hashtags pour les différencier des tiens :)

### Ton script marche bien!
### Tu as bien construit ta liste «numeros» en la démarrant à 1, car effectivement, les numéros de permis de médecin commencent par 001.
### Tu aurais pu afficher directement les numéros de permis