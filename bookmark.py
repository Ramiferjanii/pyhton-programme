## empty list
mylist = [ ]
## maximum aalowed websites
maximumwebs  = 5


while maximumwebs > 0 :
## input the new website
    web = input(" website name without HTTPS://")
## add the new website to the list
    mylist.append(f"https://{web.strip().lower()}")
##decrease one number from zllowed websites
    maximumwebs -= 1
## print the add message
    print(f"websites add , {maximumwebs} place left ")
    print(mylist)
else:
    print("my list is full you can add more ")



## check if list is not empty
if len(mylist) > 0 :
    mylist.sort()
    index = 0
    print("printing the list of websites in your boookmark ")
    while index < len(mylist) :
        print(mylist[inedx])
        index += 1