s = input(" donner une phrase ") 
i = s.split()
mot="" 
for x in i : 
    if (len(x) > len(mot)) : 
        mot = x  
        
print (" le mot le plus long de la phrase est " , mot) 