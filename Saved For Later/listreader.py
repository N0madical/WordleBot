with open('fivewords.txt') as words:
    wordlist = words.readlines()

wordlist = [x.strip() for x in wordlist]

print (wordlist)

with open(r'wordsarray.txt', 'w') as newlist:
    newlist.write(str(wordlist))