sexe  = input (" entre le sexe : " ).upper()
t = float ( input (" entre la taille en cm : " ) )
p = float  ( input ( " entre le poid en kg : "  ) )
if sexe == 'M' :
    pi = (t - 100 ) - (t - 150 ) / 4
    print (f" votre poids idéal est : {pi:.2f} ")  
elif sexe == 'F' :
    pi = (t - 100 ) - ( t - 150 ) / 2
    print (f" votre poids idéal est : {pi:.2f} ")  
t = t / 100 
bmi = p / (t * t )
if bmi< 27 :
    print (" vous etes : normale ")
elif bmi>=27 and bmi < 32 :
    print (" vous etes : Obése ")
elif bmi>=32  :
    print (" vous etes : malade ")

    
