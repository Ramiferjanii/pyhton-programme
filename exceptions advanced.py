the_file =      None
tries = 5

while tries > 0  :
    try:
        print(" enter the file name with absolule path to open ")
        print(f" you have { tries} tries left ")
        print( r" exemple of path : d:\python\files\yourfile.extension")
        file_named_path = input("file name => ").strip()
        the_file = open(file_named_path , "r")
        print(the_file.read())
        break
    except FileNotFoundError:
        print("Error happen  ,  the  file not find")
    finally:
        if the_file is not None :
            the_file.close()
            print("file closed !")



else :
        print(" all tries is done ")