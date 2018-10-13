# coding=utf-8

"""
This is an example script.

It seems that it has to have THIS docstring with a summary line, a blank line
and sume more text like here. Wow.
"""

message = "Hello Python World !"
print(message)

message = "Hello Python Crash Course world!"
print(message)

# Méthode : Majuscule première lettre de chaque mot -----
name = "ADA lovelace"
print(name.title())

# Méthode : tout en maj ou min .upper() .lower() ---------
name = "Ada Lovelace"
print(name.upper())
print(name.lower())

first_name = "maël"
last_name = "prost"

# Concaténation ------------------------------------------
full_name = first_name.title() + " " + last_name.upper()
print(full_name)

# Spaces : tab \t  return \n -----------------------------
print("Languages:\n\tPython\n\tC\n\tJavaScript")

"""
Méthode : Supprimer les espaces en trop
.strip() both
.rstrip() droite
.lstrip() gauche

"""
favorite_language = 'python '
print(favorite_language)

print(favorite_language.strip())

favorite_language = favorite_language.strip()
print(favorite_language)
