annee = int ( input (" entre une annee :" ))
if (annee % 4 == 0 and annee % 100 != 0 ) or annee % 400 == 0 :
              print (f"l'annee {annee} et une anne bissextile " )
else :
    print (f"l'anne  {annee} est n'est pas bissextile ") 
