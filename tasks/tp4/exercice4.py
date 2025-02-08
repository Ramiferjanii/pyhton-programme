def entier_1 () :
    a= int(input ( "donner le premier entier : " ) )
    return a

def entier_2 () :
    b = int(input(" donner le deuxieme entier : " ) )
    return b

def calculer(a,b) :
    s= a+b
    return s

def affichier (s) :
    return s

a = entier_1()
b = entier_2()
s= calculer(a,b)
print (f" le somme de deux entier et {s}")

