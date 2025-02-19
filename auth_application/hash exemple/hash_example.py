import sqlite3
import hashlib
import os
from tkinter import messagebox

def hash_username(value: str) -> str:
    """Hash une chaîne de caractères (nom d'utilisateur ou autre)."""
    return hashlib.sha256(value.encode()).hexdigest()

def hash_password(password: str) -> str:
    """Hash le mot de passe avec un sel."""
    salt = os.urandom(16)
    hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    return salt.hex() + ':' + hashed_password.hex()



def verify_password(stored_password: str, provided_password: str) -> bool:
    """Vérifie si un mot de passe correspond au hash stocké."""
    salt, stored_hash = stored_password.split(':')
    salt = bytes.fromhex(salt)
    hashed_password = hashlib.pbkdf2_hmac('sha256', provided_password.encode(), salt, 100000)
    return hashed_password.hex() == stored_hash

def insert_user(username: str, password: str, db_path: str = "tkinter/hash_example.db"):
    """Insère un utilisateur avec son mot de passe hashé en base de données."""
    hashed_username = hash_username(username)
    hashed_password = hash_password(password)
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      username TEXT UNIQUE,
                      password TEXT)''')
    
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (hashed_username, hashed_password))
        conn.commit()
        print("Utilisateur ajouté avec succès.")
    except sqlite3.IntegrityError:
        print("Erreur : ce nom d'utilisateur existe déjà.")
    finally:
        conn.close()

def authenticate_user(username: str, password: str, db_path: str = "tkinter/hash_example.db") -> bool:
    """Authentifie un utilisateur en vérifiant son mot de passe."""
    hashed_username = hash_username(username)
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute("SELECT password FROM users WHERE username = ?", (hashed_username,))
    result = cursor.fetchone()
    conn.close()
    
    if result is None:
        print("Erreur : utilisateur non trouvé.")
        return False
    
    print("Connexion réussi")
    return verify_password(result[0], password)

# Exemple d'utilisation




username = input("username : ")
password = input("password : ")

insert_user(username, password)

print(authenticate_user(username, password))
