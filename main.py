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
NOMBRE_MAX = 10            # constante (toujours en MAJUSCULE !)
NOMBRE_MAGIQUE = 5          # constante (toujours en MAJUSCULE !)



def demander_nombre(NOMBRE_MIN, NOMBRE_MAX):
    reponse = input("Quel est le nombre magique (Entre " + str(NOMBRE_MIN) +" et " + str(NOMBRE_MAX) + ")?")
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

demander_nombre(1, 10)  # ici entre 1 et 10