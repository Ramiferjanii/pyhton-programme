# Demander à l'utilisateur de saisir deux nombres entiers
a = int(input("Entrez le premier nombre entier (a) : "))
b = int(input("Entrez le deuxième nombre entier (b) : "))

# Calculer le quotient et le reste de la division euclidienne
quotient = a // b
reste = a % b

# Afficher les résultats
print(f"Le quotient de {a} divisé par {b} est {quotient}")
print(f"Le reste de la division de {a} par {b} est {reste}")
