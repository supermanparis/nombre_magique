import random #ici imortation du module random qui va nous permettre de generer un nombre aléatoire

'''
def demander_nombre(nb_min, nb_max):
    reponse = input("Quel est le nombre magique? (Entre 1 et 10)")
    if int(reponse) < 5:
        print("Le nombre magique est plus grand!")
    elif int(reponse) > 5:
        print("Le nombre magique est plus petit!")
    else :
        print("Bravo, vous avez trouvé le nombre magique !")

demander_nombre(1, 10)
'''


NOMBRE_MIN = 1              # constante (toujours en MAJUSCULE !)
NOMBRE_MAX = 100            # constante (toujours en MAJUSCULE !)
# NOMBRE_MAGIQUE = 5        # constante (toujours en MAJUSCULE !)
NOMBRE_MAGIQUE = random.randint(1,100)        # ici pour generer un nombre aléatoire compris entre les 2 chiffres
NB_CHANCE = 100





'''

# ci dessous le dev de ma proposition de fonction def demander_nombre(NOMBRE_MIN, NOMBRE_MAX):

def demander_nombre(NOMBRE_MIN, NOMBRE_MAX):
    reponse = input(f"Quel est le nombre magique (Entre {NOMBRE_MIN} et {NOMBRE_MAX})?") # ici avec l'utilisation d'une f string
    #reponse = input("Quel est le nombre magique (Entre " + str(NOMBRE_MIN) +" et " + str(NOMBRE_MAX) + ")?")

    while not reponse == NOMBRE_MAGIQUE:
        if int(reponse) > NOMBRE_MAX:
            print("Le nombre magique doit etre inférieur ou égale à "+ str(NOMBRE_MAX))
        elif int(reponse) < NOMBRE_MIN:
            print("Le nombre magique doit etre supérieur ou égale à "+ str(NOMBRE_MIN))
        elif int(reponse) < NOMBRE_MAGIQUE:
            print("Le nombre magique est plus grand!")
        elif int(reponse) > NOMBRE_MAGIQUE:
            print("Le nombre magique est plus petit!")
        else :
            print("Bravo, vous avez trouvé le nombre magique !")
            break
        

        reponse = input(f"Quel est le nombre magique (Entre {NOMBRE_MIN} et {NOMBRE_MAX})?")

demander_nombre(1, 10)  # ici entre 1 et 10  # ici appel de la fonction demander_nombre(1,10) pour tester.


'''



########## CORRECTION ############


# ci dessous la propostion de correction pour la definition de la fonction:

def demander_nombre (nb_min,nb_max):
    nombre_str = input(f"Quel est le nombre magique (entre {nb_min} et {nb_max})?") # l'input recupère le nombre str
    nombre_int = int(nombre_str) # on crée une variable nombre_int à partir de nombre_str
    return nombre_int # on retourne nombre int



def demander_nombre (nb_min,nb_max): 
    nombre_int = 0  # ici initialisation de la valeure de la variable nombre_int à 0
    while nombre_int == 0: # boucle while, "tant que nombre_int == 0 "
        nombre_str = input(f"Quel est le nombre magique (entre {nb_min} et {nb_max})?") # donc tant que... on demande une reponse à l'input qui sera enrigistrée dans la vairable nombre_str
        try:  # ici on va gérer les erreur, donc try (donc vérifie bien) que nombre_int = int(nombre_str)
            nombre_int = int(nombre_str)
        except:
            print("ERREUR - Vous devez entrer une valeure numérique ! Réessayez ! ") # si le try n'est pas bon et qu'il y une exception, gère la et affiche : "ERREUR - Vous devez entrer une valeure numérique !"
        else:
            if nombre_int > nb_max or nombre_int < nb_min:
                print(f"ERREUR - Vous devez entrer une valeure numérique (entre {nb_min} et {nb_max})?! Réessayez !") 
                nombre_int = 0
                #nombre_str = input(f"Quel est le nombre magique (entre {nb_min} et {nb_max})?")
    return nombre_int # retour du nombre_int



# ci dessous la correction :

chance = NB_CHANCE

'''
############# ci -dessous ave une DEBUT boucle while: ####################


nombre = 0 # initialisation de la valeur a zero pour lancer le programme.

while not nombre == NOMBRE_MAGIQUE:
    nombre = demander_nombre(NOMBRE_MIN,NOMBRE_MAX)
    print(f"Vous disposez de {chance} chances.")
    if nombre == NOMBRE_MAGIQUE:
        print(f"Bravo! Gagné! Vous avez trouvé le nombre magique! Vous avez ganné 1000 chances supplémentaires !!! ")
        chance += 1000
        print(f"Vous disposez de {chance} chances.")
        break
    elif nombre > NOMBRE_MAGIQUE:
        print("Le nombre magique est plus petit!")
        chance -= 1
    else :
        print("Le nombre magique est plus grand!")
        chance -= 1
if chance == 0:
    print("Vous avez perdue !!! ") # si chance = 0 on sort de la boucle et on affiche le message
    print("Le nombre magique etait: {NOMBRE_MAGIQUE}.")


# nombre = demander_nombre(NOMBRE_MIN,NOMBRE_MAX)

############# FIN  ####################



'''

############# ci -dessous ave une DEBUT boucle for : ####################

gagne = False

for i in range(0,NB_CHANCE):
    nombre = demander_nombre(NOMBRE_MIN,NOMBRE_MAX)
    chance -= 1
    print(f"Vous disposez de {chance} chances.")
    if nombre == NOMBRE_MAGIQUE:
        print(f"Bravo! Gagné! Vous avez trouvé le nombre magique! Vous avez ganné 1000 chances supplémentaires !!! ")
        chance += 1000
        print(f"Vous disposez désormais de {chance} chances.")
        gagne = True
        break

    elif nombre > NOMBRE_MAGIQUE:
        print("Le nombre magique est plus petit!")
    else :
        print("Le nombre magique est plus grand!")

    
if not gagne:
    print("Vous avez perdue !!! ") # si chance = 0 on sort de la boucle et on affiche le message
    print(f"Le nombre magique etait: {NOMBRE_MAGIQUE}.")

############# FIN  ####################





########## FIN CORRECTION ############
