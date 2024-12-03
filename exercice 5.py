
a = float(input("Entrez le coefficient a : "))
b = float(input("Entrez le coefficient b : "))


if a != 0:
    x = -b / a
    print(f"La solution de l'équation {a}x + {b} = 0 est x = {x}")
else:
    if b == 0:
        print("L'équation a une infinité de solutions.")
    else:
        print("L'équation n'a pas de solution.")

