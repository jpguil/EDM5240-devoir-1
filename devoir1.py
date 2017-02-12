#coding: utf-8

#tous les possibles débuts de matricule selon les années
annees1 = list(range(0,18))
annees2 = list(range(30,100))

#fusionner les deux lists
annees1.extend(annees2)

#format pour garder que les deux derniers chiffres des années
annee = ['{:02}'.format(annee) for annee in annees1]

#toutes les fins de matricule possibles
numeros = ['{:03}'.format(numeros) for numeros in range(1, 1000)]

#pour chaque année, ajouter toutes les fins de matricule possibles
matricule = []
for an in annee:
  for numero in numeros:
    matricule.append(an + numero)

print(matricule)
