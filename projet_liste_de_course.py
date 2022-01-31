liste_courses = { }

def ajouter(nom):
    global liste_courses
    if (nom) in liste_courses:
        print("Elément existe déjà ")
    else:
        type = input("Entrez le type : ")
        qty = int(input("Entrez la quantité : "))
        liste_courses[(nom)] = (type, qty)

def supprimer(nom):
    if (nom) in liste_courses:
        print("Elément existe")
        liste_courses.pop((nom))
    else:
        print ("Elément existe pas")

def consulter(nom):
    global liste_courses
    if liste_courses.get((nom))!=None:
        print ('Le type est {0:s}'.
								format(liste_courses.get((nom))[0]))
        print ('La quantité est {0:d}'.
								format(liste_courses.get((nom))[1]))
    else:
        print ('Ce contact n\'existe pas')

def vider(liste_courses):
    if len(liste_courses) != 0:
        print("Liste vidée")
        liste_courses.clear()
    else:
        print("Liste déjà vide")
    


def menu():
    choix = None
    while choix != '5':
        choix = input('Entrez un choix :\n\t\t\t\t '
                      '1)Ajouter \n\t\t\t\t '
                      '2)Supprimer \n\t\t\t\t '
                      '3)Afficher\n\t\t\t\t '
                      '4)Vider\n\t\t\t\t '
                      '5)Quitter\n')
        choix = choix.lower()
        if choix == '5':
            print("Bye Bye")
        elif choix == '4':
            vider(liste_courses)
        elif choix in '123' :
            nom = input('Ajouter élément à la liste : ')
            nom = nom.capitalize()
            if choix == '1':
                ajouter(nom)
            elif choix == '2':
                supprimer(nom)
            elif choix == '3':
                consulter(nom)

menu()
