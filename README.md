# Générateur de mot de passe sécurisé

## Description
Ce projet est un **générateur de mot de passe sécurisé** développé en Python.  
Il permet de créer un mot de passe respectant les contraintes de sécurité suivantes :

- Contient **au moins une majuscule, une minuscule, un chiffre et un symbole**  
- **Longueur minimale : 8 caractères**  
- Mélange aléatoire pour éviter tout ordre prévisible  

Ce projet est conçu pour apprendre à manipuler **Python**, les **listes**, les **boucles** et la **librairie `random`**.

---

## Auteur
**Laeticia Kacimi**

---

## Fonctionnement

1. L’utilisateur est invité à saisir la **longueur souhaitée** du mot de passe (minimum 8 caractères).  
2. Le programme génère un mot de passe respectant les contraintes :  
   - 1 lettre minuscule  
   - 1 lettre majuscule  
   - 1 chiffre  
   - 1 symbole  
3. Le mot de passe est ensuite complété avec des caractères aléatoires pour atteindre la longueur demandée.  
4. Le mot de passe est **mélangé** pour éviter un ordre prévisible et affiché à l’écran.

---

## Instructions pour exécuter le projet

1. Assurez-vous d’avoir **Python 3.x** installé sur votre machine.  
2. Téléchargez le fichier `password_generator.py` (ou nom du fichier que vous avez utilisé).  
3. Dans le terminal, exécutez :

```bash
python3 password_generator.py
