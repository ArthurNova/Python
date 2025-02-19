import hashlib
import sqlite3

# Connexion à SQLite
conn = sqlite3.connect("example.db")
cursor = conn.cursor()

# Création de la table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL
)
""")
conn.commit()

# Fonction pour hacher un mot de passe
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Fonction pour ajouter un utilisateur
def add_user(username, password):
    password_hash = hash_password(password)
    try:
        cursor.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", (username, password_hash))
        conn.commit()
        print("Utilisateur ajouté avec succès.")
    except sqlite3.IntegrityError as e:
        print(f"Erreur : {e}")


add_user("arthur", "123")

def authenticate_user(username, password):
    password_hash = hash_password(password)
    cursor.execute("SELECT password_hash FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    
    if result is None:
        print("Utilisateur non trouvé.")
        return False

    stored_hash = result[0]
    if stored_hash == password_hash:
        print("Authentification réussie.")
        return True
    else:
        print("Mot de passe incorrect.")
        return False

# Exemple d'authentification
authenticate_user("arthur", "123")  # Authentification réussie
authenticate_user("arthur", "mauvaisMotDePasse")  # Mot de passe incorrect

conn.close()

