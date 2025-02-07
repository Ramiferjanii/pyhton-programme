def saisir_entiers():
    e = []
    while True:
        n = int(input("donner un entier  : "))
        if n == -1:
            break
        e.append(n)
    return e

def maxi(e):
    max_val = e[0]
    max_index = 0
    for i in range(1, len(e)):
        if e[i] > max_val:
            max_val = e[i]
            max_index = i
    return max_val, max_index+1

def facto(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * facto(n - 1)

def est_premier(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def premier():
    entiers = saisir_entiers()
    max_val, max_index = maxi(entiers)
    
    fact_max_val = facto(max_val)
    est_max_premier = est_premier(max_val)
    print(f"Le maximum de ces entiers est {max_val} et son indice est  {max_index}.")
    print(f"Le factoriel  {max_val} est {fact_max_val}.")
    if est_max_premier:
            print(f" le nombre {max_val} est un nombre premier.")
    else:
            print(f" le nombre {max_val} n'est pas un nombre premier.")
    


premier()




     
        
        
