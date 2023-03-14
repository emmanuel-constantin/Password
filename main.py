import string
# contient des constantes de chaînes de caractères représentant des classes de caractères courantes
# telles que les lettres, les chiffres et les caractères de ponctuation.
import hashlib
import json
import os.path


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

def addtojson(user, password):
    if os.path.isfile("passwords.json"):
        with open('passwords.json', 'r+') as file_json:
            dict_json = json.load(file_json)
            dict_json.setdefault("infos", []).append({"user": user, "password": password})
            file_json.seek(0)
            file_json.truncate(0)
            json.dump((dict_json), file_json)
    else:
        with open('passwords.json', 'w') as file_json:
            json.dump({"infos": [{"user": user, "password" : password}]}, file_json)
    
def show_passwords():
    with open('passwords.json', 'r') as f: 
        passwords = json.loads(f.read())
    print(passwords)

def password_exists(password):
    if os.path.isfile('passwords.json'):
        with open('passwords.json', 'r+') as f:
            file_contents = f.read()
        data = json.loads(file_contents)
        for entry in data.get('infos', []):
            if entry.get('password') == hash_password(password):
                return True 
    else:
        return False

def user_exists(user):
    if os.path.isfile('passwords.json'):
        with open('passwords.json', 'r+') as f:
            file_contents = f.read()
        data = json.loads(file_contents)
        for entry in data.get('infos', []):
            if entry.get('user') == user:
                return True 
    else:
        return False
        
def menu():
    while True: 
        print("1. Ajouter un mot de passe")
        print("2. Afficher les mots de passe")
        print("3. Quitter")
        choice = input("Que voulez vous faire ? (1-3) : ")
        user_valide = False
        if choice == '1':
            while not user_valide:
                user = input("Entrez votre nom : ")
                if user_exists(user):
                    print("Ce nom existe déjà.")
                    # break
                else: 
                    user_valide = True
            mot_de_passe_valide = False
            while not mot_de_passe_valide:
                password = input("Choisissez un mot de passe, il doit contenir au minimum une lettre minuscule, une lettre majuscule, un caractère spécial et doit avoir une longueur de 8 caractères minimum : ")
                if len(password)>= 8 and contientmaj(password) and contientminusc(password) and contientchiffre(password) and contientcaractspe(password):
                    if password_exists(password):
                        print("Ce mot de passe existe déjà. ")
                    else: 
                        addtojson(user,hash_password(password))
                        print("Mot de passe valide, il a été crypté et enregistré.")
                        mot_de_passe_valide = True
                else:
                    print ("Mot de passe invalide, veuilez réessayer ")
        elif choice == '2':
            show_passwords()
        elif choice == '3':
            break

menu()

