################### recursion function  ##############################

def cleanword(word)  :
    if len(word) == 1 :
        return word

    if word[0] == word[1] :
        return  cleanword(word[1:])

    return word[0] + cleanword(word[1:])

print(cleanword("wwwwwwwwwwwwwwwwoooooooooooooooooooooooooorlddddddddd"))