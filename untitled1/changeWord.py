import random
import chooseWord

word=chooseWord.choosedWord
items = [word[0],word[1] , word[2], word[3], word[4], word[5],word[6],word[7],word[8]]
random.shuffle(items)

changedWord=items
print(word)
print(items)
