import random

def sortgrayyellowgreen(allwords, gray, yellow, green):

    tempwords = []
    for word in allwords:
        delword = False

        j = 0
        for letter in green:
            if (letter != word[j]) and (letter != ""):
                # print(letter + word[j])
                delword = True
            j += 1

        j = 0
        for lettergroup in yellow:
            if lettergroup != "":
                for letter in lettergroup:
                    if letter not in word:
                        delword = True
                    if (letter == word[j]):
                        # print(letter + word[j])
                        delword = True
            j += 1

        for letter in gray:
            if letter in word:
                delword = True

        if not delword:
            tempwords.append(word)

    return tempwords

def topword(allwords):
    temp = []
    returnlist = []
    vowels = ["a", "e", "i", "o", "u"]
    topscore = 0

    with open('commonwords.txt') as cmnwords:
        commonwords = cmnwords.readlines()
    commonwords = [x.strip().lower() for x in commonwords]

    common = False
    for word in allwords:
        if word in commonwords:
            common = True
            temp.append(word)
    if not common:
        temp = allwords

    for word in temp:
        tempscore = 0
        templetterstore = []
        for letter in word:
            if (letter in vowels) and (not letter in templetterstore):
                tempscore += 1
                templetterstore.append(letter)
        if tempscore == topscore:
            returnlist.append(word)
        if tempscore > topscore:
            returnlist = [word]
            topscore = tempscore

    if not returnlist:
        return "-----"
    else:
        return random.choice(returnlist)

def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb
rgb_to_hex((255, 255, 195))