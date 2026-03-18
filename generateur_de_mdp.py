import random
import string

# Définition des types de caractères
lower = string.ascii_lowercase
upper = string.ascii_uppercase
digits = string.digits
symbols = string.punctuation

all_chars = lower + upper + digits + symbols

def generate_password(length):
    """Génère un mot de passe respectant toutes les contraintes"""
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols)
    ]
    
    # Complète avec des caractères aléatoires jusqu'à la longueur demandée
    if length > 4:
        password += [random.choice(all_chars) for _ in range(length - 4)]
    
    random.shuffle(password)  # Mélange pour éviter l’ordre prévisible
    return ''.join(password)

# Boucle jusqu’à obtenir un mot de passe valide
while True:
    try:
        length = int(input("Longueur du mot de passe (≥ 8) : "))
        if length < 8:
            print("⚠️ Le mot de passe doit contenir au moins 8 caractères. Réessaie !")
            continue
        password = generate_password(length)
        print("Mot de passe généré :", password)
        break
    except ValueError:
        print("⚠️ Merci de saisir un nombre valide.")