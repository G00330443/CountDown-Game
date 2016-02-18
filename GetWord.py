
f = open('wordlist.txt', 'r')
o = open('Nine-Letter-wordsList.txt', 'w')
WordList=[]
def checkWord(f):
    for word in f:
        word = word.strip()
       # print(word)
        if len(word)==9:
            if ' ' in word :
                 o.write('')
            else:
                 WordList.append(word)              
                 o.write(word + "\n")

checkWord(f)