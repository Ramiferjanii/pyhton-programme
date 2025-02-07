for i in range(1 , 101 ) :
    nb = 0 
    for j in range (1 , i+1) : 
        if (i%j == 0) : 
            nb+=1 

    if nb == 2 : 
        print (f"{i} --- ", end="") 