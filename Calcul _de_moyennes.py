import statistics

#Listes de données

pupils_names = []
pupils_moyennes = []

#Nom de chaque élève, le nombre de matières, les notes correspondantes et leur moyenne
pupils_number = int(input("Veuillez entrer le nombre d'élèves : "))
for j in range(pupils_number):

    #Données pour chaque élève
    matières_name = []
    matières_notes = []

    #Nom de chaque élève
    pupils_names.append(input("Veuillez entrer le nom de l'élève : "))
    matières_nombres = int(input(f"Veuillez entrer le nombre de matières pour {pupils_names[j]} : "))

    #Matières et notes pour chaque élève
    for i in range(matières_nombres):
        matières_name.append(input("Veuillez entrer le nom de la matière : "))
        matières_notes.append(float(input("Veuillez entrer la note correspondante à cette matière : ")))
    print(f"Voici chaque matière avec sa note pour l'élève {pupils_names[j]} : ")
    
    for i in range(matières_nombres):

    #Moyenne de chaque élève    
        print(f"{matières_name[i]} = {matières_notes[i]}")
        moyenne = statistics.mean(matières_notes)

    pupils_moyennes.append(statistics.mean(matières_notes))
    print(f"La moyenne de {pupils_names[j]} est de :", pupils_moyennes[j])

#Final
print("La liste des élèves et leurs moyennes est la suivante : ")
for j in range(pupils_number):
    print(f"La moyenne de {pupils_names[j]} est de : {pupils_moyennes[j]}")
