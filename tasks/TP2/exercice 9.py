base = float ( input (" donne la base en DT : " ))
ps = int ( input (" sonne le puissance de la voiture en cv : " ))
type_v = input (" donne le type de la voiture ( 'U' : utilaire , 'C' : commerciale , 'T' : trajet , 'P' : promenade ) : " ).upper()
if ps>7 :
    prime = base+ (base*40/100)
elif ps<=5 :
    prime = base
else :
    prime = base + (base*20/100)

if type_v == 'U' :
    prime += prime*5/100
elif type_v == 'C' :
    prime += prime*10/100
elif type_v == 'T' :
    prime += prime * 15/100
elif type_v == 'P' :
    prime += prime * 30/100

print (f" la prime d'assurance et : {prime:.2f} DT ") 
