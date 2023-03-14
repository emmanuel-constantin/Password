import string
# contient des constantes de chaînes de caractères représentant des classes de caractères courantes
# telles que les lettres, les chiffres et les caractères de ponctuation.
import hashlib
import json
import os.path
from tkinter import *


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
        
def save_password():
    user = user_entry.get()
    password = password_entry.get()
    if len(password) >= 8 and contientmaj(password) and contientminusc(password) and contientchiffre(password) and contientcaractspe(password):
        if password_exists(password):
            message_label.config(text = "Ce mot de passe existe déjà.")
        else: 
            addtojson(user,hash_password(password))
            message_label.config(text = "Mot de passe valide, il a été crypté et enregistré.")
    else:
        message_label.config(text="Votre mot de passe ne remplit pas les critères de sécurité, veuillez réessayer.")

def show_passwords():
    with open('passwords.json', 'r') as f: 
        passwords = json.loads(f.read())
    message_label.config(text = str(passwords))

root = Tk()
root.title("Gestionnaire de mots de passe")

user_label = Label(root, text ="Nom d'utilisateur")
user_label.pack()

user_entry = Entry(root)
user_entry.pack()

password_label = Label(root, text="Mot de passe")
password_label.pack()

password_entry = Entry(root, show="*")
password_entry.pack()

save_button = Button(root, text="Enregistrer", command=save_password)
save_button.pack()

show_button = Button(root, text="Afficher les mots de passe", command=show_passwords)
show_button.pack()

message_label = Label(root, text="")
message_label.pack()

root.mainloop()







