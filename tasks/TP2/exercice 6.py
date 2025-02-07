
a = input("Entrez un caractère : ")

if a.isalpha():
    print(f"{a} est une lettre de l'alphabet.")

elif a.isdigit():
    print(f"{a} est un chiffre.")

else:
    print(f"{a} est un caractère spécial.")
