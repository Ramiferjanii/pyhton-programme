admin = [ "oussama" , "rami" ,"ahmed" , "salem" , "malek" , "hayder"]
name = input("please enter your name " ).strip().lower()

if  name in admin :
    print(f"welcom back  {name}!!")
    option = input("delete your name or update ?").strip().lower()
if option  == "update" :
    newname = input("please enter your name ").strip().lower()
    admin[admin.index(name)] = newname
    print("name is updated !!!")
    print(admin)
elif option == "delete" :
    admin.remove(name)
    print(admin)
    else:
        print("wrong option choosed !!!")
else:
    print("your are not admin ")
        status =  input("do you have add your name to admin ??? yes , no ").strip().lower()
        if status == "yes" :
            admin.append(name)
            print("you have been add")
            print(admin)
        else:
            print("you welcom !!!! ")