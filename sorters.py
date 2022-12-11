def sortgrayyellowgreen(allwords, gray, yellow, green, debug):
    if debug:
        print("\nModifications Log:")
    tempwords = []
    for word in allwords:
        delword = False

        j = 0
        for letter in green:
            if (letter != word[j]) and (letter != ""):
                # print(letter + word[j])
                delword = True
                if debug:
                    print("Deleted \"" + word + "\" because it did not contain the green letter \"" + letter + "\".")
            j += 1

        j = 0
        for lettergroup in yellow:
            if lettergroup != "":
                for letter in lettergroup:
                    if letter not in word:
                        delword = True
                        if debug:
                            print ("Deleted \"" + word + "\" because it did not contain the yellow letter \"" + letter + "\".")
                    if (letter == word[j]):
                        # print(letter + word[j])
                        delword = True
                        if debug:
                            print ("Deleted \"" + word + "\" because it contained the yellow letter \"" + letter + "\" but at the position it was previously at.")
            j += 1

        for letter in gray:
            if (letter in word):
                delword = True
                if debug:
                    print("Deleted \"" + word + "\" because it contained the gray letter \"" + letter + "\".")

        if not delword:
            tempwords.append(word)

    return tempwords

def topword(allwords, debug):
    temp = []
    returnlist = []
    vowels = ["a", "e", "i", "o", "u"]
    letterrank = []
    topletters = []
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    topscore = 0

    with open('commonwords.txt') as cmnwords:
        commonwords = cmnwords.readlines()
    commonwords = [x.strip().lower() for x in commonwords]

    for i in range (0,len(alphabet)):
        letterrank.append(0)

    for eachword in commonwords:
        for eachletter in eachword:
            letterrank[alphabet.index(eachletter)] += 1

    for i in range (0,26):
        topindex = 0
        topindexvalue = 0
        for j in range (0,26):
            if letterrank[j] > topindexvalue:
                if alphabet[j] not in topletters:
                    topindexvalue = letterrank[j]
                    topindex = j
        topletters.append(alphabet[topindex])

    common = False
    for word in allwords:
        if word in commonwords:
            common = True
            temp.append(word)
    if not common:
        temp = allwords

    if debug:
        print("\nSorting words based on vowel counts:")
    for word in temp:
        tempscore = 0
        templetterstore = []
        for letter in word:
            if (letter in vowels) and (not letter in templetterstore):
                tempscore += 1
                templetterstore.append(letter)
        if tempscore == topscore:
            returnlist.append(word)
            if debug:
                print("Added '" + word + "' to list of top vowel words because it tied for top with " + str(tempscore) + " vowels.")
        if tempscore > topscore:
            returnlist = [word]
            topscore = tempscore
            if debug:
                print("Reset the top vowel words list because '" + word + "' had " + str(tempscore) + " vowels, more then previously scanned words.")
    if debug:
        print ("\nWord list sorted based on vowels:")
        print (returnlist)

    if not returnlist:
        return "-----"
    else:
        if len(returnlist) == 1:
            return returnlist[0]
        else:
            if debug:
                print("\nDuplicate vowel amounts occurred, further narrowing based on letter frequency:")
            temp2 = []
            topscore = 0
            tempscore = 0
            templetterstore = []
            for word in returnlist:
                explination = word + " - "
                templetterstore = []
                tempscore = 0
                for letter in word:
                    if letter not in templetterstore:
                        tempscore = tempscore + (27 - topletters.index(letter))
                        explination =  explination + "added " + letter + " for " + str(27 - topletters.index(letter)) + " points - "
                    if letter in templetterstore:
                        tempscore = tempscore + (0 - topletters.index(letter))
                        explination = explination + "penalized duplicate " + letter + " for " + str(-27 + topletters.index(letter)) + " points - "
                    templetterstore.append(letter)
                if tempscore > topscore:
                    topscore = tempscore
                    temp2 = [word]
                if tempscore == topscore:
                    temp2.append(word)
                if debug:
                    print (explination + "final score: " + str(tempscore))
            if debug:
                print("\nFinal word:")
            return temp2[0]

def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb