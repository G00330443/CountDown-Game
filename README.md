# CountDown_Game
----------------------------------
__Theory of Algorithms__

## Project title: Word_Countdown Game
 By Haoyu Wang 
 ---------------------------
 
### Introduction

######  a Python script that solves the Countdown letters game, and a document explaining how to solver works.

###### The Countdown letters game is as detailed on Wikipedia. Esentially, you are given a list of nine random letters which contains at least three vowels and four consonants
 
###### You must find the longest possible word in the Oxford English dictionary that is an anagram of some or all of the letters in the random list.


### Function realized

* Random generate vowels and consonants through press vowels and consonants button.

* start Rockon time when typing the last letter 

* generate all words use random generated letters.

* throuh setting length of answers to generate the longest word .

* input answer that you guessed in input textfield  


### Language use --python (use PYQt5 to build GUI ) 

* Download library for PYQT to run this app

>- address for source : http://pyqt.sourceforge.net/Docs/PyQt5/installation.html

* reason of use PYQT to built GUi rather than original python

>- althought original pyton have package of Gui but it's limited, only have few types. I download PYQT it can design frame of app very easy and nice.

* use it

>-  Generate Ui file from this app and convert ui file to pyhon file .

### How to use this App

* Double click runMainpage.py 

* MainPage show
>![image](https://github.com/G00330443/CountDown-Game/blob/master/Graph/mainpage.PNG)
>
* Click Vowel or Consonants to generate word 
>![image](https://github.com/G00330443/CountDown-Game/blob/master/Graph/generated%20Word.PNG)

* Start time

* input answer you guessed and length of word you want to check  (word length default by 5)
>![image](https://github.com/G00330443/CountDown-Game/blob/master/Graph/inputword%20and%20set%20len%20of%20word.PNG)

* check information you need to fill then click submit
>![image](https://github.com/G00330443/CountDown-Game/blob/master/Graph/submit.PNG)
--------------------

### Python Code

##### Preprocessing
When you first run the script, the user will have to enter the vowels and consonants using the marked buttons. The count time starts automatically. the user inputs the guessed answer and specify the length of the answer (english word) and finally click on the Submit button. The script will generate all the possible english words (from the vowels and consonants) that have the specified length and above.
* The function below is used to solve count time problem using a QThread .
```python 
from PyQt5.QtCore import *

class WorkThread(QThread):
    trigger = pyqtSignal()
    def __int__(self):
        super(WorkThread,self).__init__()

    def run(self):
        for i in range(203300030):
            pass
        self.trigger.emit()  
```

* The function below generates random vowels and consonants.
* ``` python def vowels() and def()consonants ``` return a new randomly generated letter to mainpage.py

```python
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
            
#inputLetters(0)
              

```

* This function generates all the possible english words (answers)
```python 
import inputLetter
import time
f = open('words.txt', 'r')
wordlist=[]
dic={}
infor={}
#inputWord=inputLetter.inputWord
#inputWord="agreement"
def set_input_word(inputword) :
    start = time.time()
    checkWord(f,inputword)
    end = time.time()
    print (end-start)


def check(word,flag,inputword) :
    cc=list(inputword)
  #  print(cc)
    n=0
    flag=flag
    ww=list(word)
   # print(word)
    for i in word :
     #   print(ww)
      #  print(i)
      #  print(i in cc)
        if i in cc :
            
            ww.remove(i)
            cc.remove(i)
        #    print(ww)
      
        if len(ww)==0 :
            break 
     
    if len(ww)==flag :
        return 0;
 
 ```
 * This function gets the user input and as well reads from words.txt. It gets the word and checks against the english words generated from the user inputs and puts it into the wordlist.
 
 ```python       
        
def checkWord(f,inputword):
    infor.clear()
    f=open('words.txt', 'r')
    for word in f:
        word = word.strip()

        if check(word,0,inputword)==0 :
          #  print(word)
            wordlist.append(word)
            infor[word]=len(word)
    print(sorted(infor.items(), key=lambda item: item[1]))


#set_input_word(inputWord)
```
### Efficiency

* THis script work efficiency , generate all answers need 2.6sec. result image in below 

>![image](https://github.com/G00330443/CountDown-Game/blob/master/Graph/result.PNG)

### References
* Begin Start Learn Pyqt5:   http://www.thehackeruniversity.com/2014/01/23/pyqt5-beginner-tutorial/
* Watch his video in youtube when i start doing python :https://www.youtube.com/user/onestopprogramming
