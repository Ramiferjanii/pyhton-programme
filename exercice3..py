n = int ( input( " donner le nombre de l'element  " ) )
my_list = []
for i in range (n) :
    element  = int ( input ( f" entree element {i+1} " ) )
    my_list.append(element)
print ( " list : " , my_list )

sum_element = sum(my_list)
p = 1
for i in my_list :
    p *= i
print ( " sum : " , sum_element  )
print (" produit : " , p )
max_element = max(my_list )
min_element = min ( my_list )
print (" plus grand element et : " , max_element )
print (" le petit nombre element et  : " , min_element )

sublist = my_list[ : 3 ]
print (" le premiere element et : " , sublist )

suprimer_element = my_list.remove(my_list[0])
print (my_list)

my_list.insert(2 , 8 )
print(my_list)

my_list.reverse()
print (my_list)

print (" finale list et : " , my_list ) 

