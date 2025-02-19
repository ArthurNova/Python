from tkinter import *
from tkinter import messagebox
import sqlite3
import hashlib
import os

db_path = "tkinter/example.db"  # Modifier le chemin si nécessaire

def hash_username(username: str) -> str:
    """Hash une chaîne de caractères (nom d'utilisateur ou autre)."""
    if not username:
       messagebox.showerror("Erreur", "Vous devez renseigner un nom d'utilisateur")
       return
    return hashlib.sha256(username.encode()).hexdigest()

def hash_password(password: str) -> str:
    """Hash le mot de passe avec un sel."""
    if not password:
       messagebox.showerror("Erreur", "Vous devez renseigner un mot de passe")
       return
    salt = os.urandom(16)
    hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    return salt.hex() + ':' + hashed_password.hex()

def insert_bdd(inscription_window):
    username_value = value_username.get().strip()
    password_value = value_password.get().strip()

    hashed_username = hash_username(username_value)
    hashed_password = hash_password(password_value)

    if not hashed_username or not hashed_password:
        return

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
    """)

    try:
        cursor.execute("SELECT id FROM users WHERE username = ?", (hashed_username,))
        existing_user = cursor.fetchone()
        if existing_user:
            messagebox.showerror("Erreur", "L'utilisateur existe déjà")
            return

        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (hashed_username, hashed_password))
        conn.commit()
        messagebox.showinfo("Succès", f"L'utilisateur '{username_value}' a été ajouté avec succès !")

        inscription_window.destroy()
        accueil()
        
        
    except sqlite3.IntegrityError as e:
        messagebox.showerror("Erreur", f"L'insertion a échoué : {e}")
    finally:
        conn.close()
        

def verify_password(stored_password: str, provided_password: str) -> bool:
    # Vérifier que la chaîne contient bien un sel et un hash
    if ':' not in stored_password:
        messagebox.showerror("Erreur", "Le mot de passe stocké est invalide.")
        return False

    salt, stored_hash = stored_password.split(':')
    salt = bytes.fromhex(salt)
    hashed_password = hashlib.pbkdf2_hmac('sha256', provided_password.encode(), salt, 100000)
    
    return hashed_password.hex() == stored_hash

def authenticate_user(connexion_window) -> bool:
    """Authentifie un utilisateur en vérifiant son mot de passe."""
    hashed_username = hash_username(value_username.get().strip())
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute("SELECT password FROM users WHERE username = ?", (hashed_username,))
    result = cursor.fetchone()
    conn.close()
    
    if result is None:
        messagebox.showerror("Erreur", "Utilisateur non trouvé.")
        return False

    stored_password = result[0]
    
    # Utilisation du mot de passe de l'interface
    provided_password = value_password.get().strip()

    if verify_password(stored_password, provided_password):
        messagebox.showinfo("Succès", "Connexion réussie !")
        connexion_window.destroy()
        user_main_page()
        return True
    else:
        messagebox.showerror("Erreur", "Mot de passe incorrect.")
        return False

def accueil():
    global main_windows
    main_windows = Tk()
    main_windows.title("Connexion | Inscription")
    main_windows.minsize(300, 200)

    Button(main_windows, text="Connexion", command=connexion_page).pack(pady=5)
    Button(main_windows, text="Inscription", command=inscription_page).pack(pady=5)
    Button(main_windows, text="Quitter", command=main_windows.destroy).pack(pady=5)

    main_windows.mainloop()

def inscription_page():
    global value_username, username, value_password, password

    # Fermer la fenêtre principale
    main_windows.destroy()

    # Création d'une nouvelle fenêtre principale
    inscription_window = Tk()

    # Titre (Label)
    titre = Label(inscription_window, text="Page d'inscription")
    titre.pack()

    inscription_window.title("Inscription")     
    inscription_window.minsize(300, 200)

    cadre = Frame(inscription_window)
    cadre.pack()

    # Saisie de value_username
    value_username = StringVar()
    value_username.set("")  # texte par défaut affiché dans l'entrée
    username_input = Entry(cadre, textvariable=value_username, width=30)
    username_input.pack()

    value_password = StringVar()
    value_password.set("")  # texte par défaut affiché dans l'entrée
    password_input = Entry(cadre, textvariable=value_password, show="*", width=30)
    password_input.pack()

    username = StringVar()
    output_username = Label(cadre, textvariable=username)
    output_username.pack()

    password = StringVar()
    output_password = Label(cadre, textvariable=password)
    output_password.pack()

    # Bouton pour exécuter la fonction insert_bdd, fermer la fenêtre, et retourner à la page d'accueil
    bouton = Button(cadre, text="Créer", command=lambda: (insert_bdd(inscription_window)))
    bouton.pack()

    quit_button = Button(cadre, text="Retour", command=lambda: (inscription_window.destroy(), accueil()))
    quit_button.pack()

    inscription_window.mainloop()


def connexion_page():
    global value_username, username, value_password, password

    # Fermer la fenêtre principale
    main_windows.destroy()

    # Création d'une nouvelle fenêtre principale
    connexion_window = Tk()

    # Titre (Label)
    titre = Label(connexion_window, text="Page de connexion")
    titre.pack()

    connexion_window.title("Connexion")     
    connexion_window.minsize(300, 200)

    cadre = Frame(connexion_window)
    cadre.pack()

    # Saisie de value_username
    value_username = StringVar()
    value_username.set("")  # texte par défaut affiché dans l'entrée
    username_input = Entry(cadre, textvariable=value_username, width=30)
    username_input.pack()

    value_password = StringVar()
    value_password.set("")  # texte par défaut affiché dans l'entrée
    password_input = Entry(cadre, textvariable=value_password, show="*", width=30)
    password_input.pack()

    username = StringVar()
    output_username = Label(cadre, textvariable=username)
    output_username.pack()

    password = StringVar()
    output_password = Label(cadre, textvariable=password)
    output_password.pack()

    # Bouton pour exécuter la fonction d'authentification et fermer la fenêtre
    bouton = Button(cadre, text="Connexion", command=lambda: (authenticate_user(connexion_window)))
    bouton.pack()

    quit_button = Button(cadre, text="Retour", command= lambda :(connexion_window.destroy(), accueil()))
    quit_button.pack()

    connexion_window.mainloop()

def user_main_page():
    global main_page

    main_page = Tk()

    main_page.title("Bienvenue sur l'application")
    main_page.minsize(300, 200)

    cadre = Frame(main_page)
    cadre.pack()

    title = Label(cadre, text = f"Vous êtes connectés en temps que : {value_username.get().strip()} à l'application")
    title.pack()

    quit_button = Button(cadre, text="Déconnexion", command= lambda : (main_page.destroy(), accueil()))
    quit_button.pack()

    main_page.mainloop()
 
accueil()