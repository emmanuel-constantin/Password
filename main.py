import string
# contient des constantes de chaînes de caractères représentant des classes de caractères courantes
# telles que les lettres, les chiffres et les caractères de ponctuation.

def contientmaj(password):
    lettre = ''
    return any(lettre.isupper() for lettre in password)
   
    # Autre manière de le faire : 
    # for lettre in password:
    #     if lettre.isupper():
    #         return True
    # return False

def contientminusc(password):
    lettre = ''
    return any(lettre.islower() for lettre in password)

def contientchiffre(password):
    chiffre = 0 
    return any(chiffre.isdigit() for chiffre in password)

def contientcaractspe(password):
    caracteres_speciaux = set(string.punctuation)
    for caractere in password:
        if caractere in caracteres_speciaux:
            return True
    return False

def testmdp():
    while True:
        password = input("Choisissez un mot de passe : ")
        if len(password)>= 8 and contientmaj(password) and contientminusc(password) and contientchiffre(password) and contientcaractspe(password):
            print("Mot de passe valide")
            break 
        else:
            print ("Mot de passe invalide, veuilez réessayer ")

testmdp()

        

