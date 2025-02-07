s = input ( " donner une chaine de caractere ") 
premiermot =""
i =  0  
while (s[i] !="" and i==len(s) )  : 
        premiermot += s[i] 
        i+=1 

        if ( i==len(s)) : 
                break 
        
print (f" le premier mot est {premiermot}")
