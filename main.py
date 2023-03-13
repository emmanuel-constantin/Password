import string
# contient des constantes de chaînes de caractères représentant des classes de caractères courantes
# telles que les lettres, les chiffres et les caractères de ponctuation.
import hashlib
import json


def contientmaj(password):
    return any(lettre.isupper() for lettre in password)
   
    # Autre manière de le faire : 
    # for lettre in password:
    #     if lettre.isupper():
    #         return True
    # return False

def contientminusc(password):
    return any(lettre.islower() for lettre in password)

def contientchiffre(password):
    return any(chiffre.isdigit() for chiffre in password)

def contientcaractspe(password):
    caracteres_speciaux = set(string.punctuation)
    for caractere in password:
        if caractere in caracteres_speciaux:
            return True
    return False

def hash_password(password):
    hasher = hashlib.sha256()
    hasher.update(password.encode())
    chainehachee = hasher.hexdigest()
    return chainehachee

def addpassword(password):
    open_file = open('passwords.json','a')
    json.dump(password, open_file)
    open_file.close()
    
def show_passwords():
    with open('passwords.json', 'r') as f: 
        passwords = json.load(f)
    # for password in passwords:
    print(passwords)

def menu():
    while True: 
        print("1. Ajouter un mot de passe")
        print("2. Afficher les mots de passe")
        print("3. Quitter")
        choice = input("Que voulez vous faire ? (1-3) : ")
        if choice == '1':
            while True:
                password = input("Choisissez un mot de passe, il doit contenir au minimum une lettre minuscule, une lettre majuscule, un caractère spécial et doit avoir une longueur de 8 caractères minimum : ")
                if len(password)>= 8 and contientmaj(password) and contientminusc(password) and contientchiffre(password) and contientcaractspe(password):
                    addpassword(hash_password(password))
                    print("Mot de passe valide, voici votre mot de passe crypté, qui a été ajouté à votre liste de mots de passe  :", hash_password(password))
                    break 
                else:
                    print ("Mot de passe invalide, veuilez réessayer ")
        elif choice == '2':
            show_passwords()
        elif choice == '3':
            break

menu()

