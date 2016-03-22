import random

inputWord=[]
vowels="aeiou"
consonants="bcdfghjklmnpqrstvwxyz"
l="abcdefghijklmnopqrstuvwxyz"
c=0
def isVowels(letter) :
    if letter in vowels :
        return "true"


def isConsonants(letter) :
    if letter in consonants :
        return "true"

def vowel() :
    index=random.randint(0,len(vowels)-1)
    inputWord.append(vowels[index])
    return (vowels[index])

def con() :
    index = random.randint(0,len(consonants)-1)
    inputWord.append(consonants[index])
    return (consonants[index])


def inputLetters(i):
    for i in range(8):
        if i<3 :
            letter=input("please input  vowels, enter 0 :\n")
        elif i<7:
            letter=input("please input  consonants ,enter 1 :\n")
        else :
             letter=input("please input  letter ,enter 2 :\n")
             
        if letter=='0' :
            index=random.randint(0,len(vowels)-1)
            inputWord.append(vowels[index])
            print(vowels[index])
        elif letter=='1':
            index=random.randint(0,len(consonants)-1)
            inputWord.append(consonants[index])
            print(consonants[index])
        elif letter =='2':
            index=random.randint(0,len(l)-1)
            inputWord.append(l[index])
            print(l[index])
        else :
            print("please reenter letter")
            inputLetters(i)
            break
    print(inputWord)

def inputLetterss():
    vvv=0
    ccc=0
    word=input("please input word :\n")
    for letter in word :
        if letter in vowels :
            vvv=vvv+1
        elif letter in consonants :
            ccc=ccc+1
    print(ccc)
    if vvv>=3 and ccc>=4 :
        print(word)
    else :
        print("please enter again")
        inputLetterss()
            
#inputLetters(0)
              
