def miror(x) : 
    while (x!=0) : 
        rest = x%10 
        print (rest , end ="") 
        x =  x//10 
a= int ( input ("donner un nombre "))
print (f" le nombre miroro est = 54{miror(a)} " )
