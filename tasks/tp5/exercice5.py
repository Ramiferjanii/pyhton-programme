n = int  ( input(" donner le nombre de list " ) )
my_list = []
for i in range(n) :
    element  = int ( input ( " donner les element de la list " ) )
    my_list.append(element)

for i in my_list :
    if (my_list.count(i) > 1) :
        my_list.remove(i)


print (my_list) 
        
    
    

    
