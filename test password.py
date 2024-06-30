tries = 4
mainpassword = "oussama123"
inputpassword = input("write password :")
while inputpassword != mainpassword  :
    tries -= 1
    print(f"wrong password , {'last' if tries == 0 else tries } chance left ")
    inputpassword = input("write password :")
if tries == 0 and tries == 0 and inputpassword != mainpassword:
        print("all tries is finish ")

else:
         print("password correct !")
