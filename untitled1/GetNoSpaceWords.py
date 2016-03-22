
f = open('wordsList.txt', 'r')
o = open('9-6.txt', 'w')
WordList=[]
def checkWord(f):
    for word in f:
        word = word.strip()
       # print(word)
        if len(word)<=9 and len(word)>6 :
            if ' ' in word :
                 o.write('')
            else:
                 WordList.append(word)              
                 o.write(word + "\n")

checkWord(f)