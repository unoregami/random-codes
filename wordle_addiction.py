from english_words import get_english_words_set
import random
from string import ascii_uppercase

# stores uppercase letters to a list
uppercase = []
for i in ascii_uppercase:
    uppercase.append(i)

# uses letterpress list text file
a = open("letterpress_words_list.txt", "r")
text = a.read()
a.close()
a = text.upper()
five = list()
web2 = list(get_english_words_set(['web2']))

#12,653
word = ""
for i in a:
    if i in uppercase:
        word += i
        continue
    if len(word) == 5:
        five.append(word)
    word = ""

#10,237
for i in range(len(web2)):
    if len(web2[i]) == 5:
        five.append(web2[i].upper())
# TOTAL = 22,890


def countWords(a):   # counts the words in english words set
    count = {}
    for i in a:
        try:
            count.update({len(i): count[len(i)] + 1})
        except:
            count.update({len(i): 1})

    keys = list(count.keys())
    keys.sort()
    count = {i: count[i] for i in keys}
    for i in count:
        print(f"{i}: {count[i]}")
    print(f"TOTAL: {sum(count.values())}")

def pickWord(five): # pick random word
    return five[random.randrange(0, len(five))]

def playWordle():
    tries = 5
    word = pickWord(five)
    wLetters = [i for i in word]
    notinword = []


    while tries != 0:
        guess = ""
        while guess not in five:
            print(f"{tries} ATTEMPT {notinword}")
            guess = input("").upper()

        if guess == word:
            print("YOU WIN BITCH")
            break
        else:
            tries -= 1
            if tries == 0:
                print("YOU LOST BITCH")
                print(word)
            gLetters = [i for i in guess]
            for i in range(5):
                if gLetters[i] in wLetters:
                    if gLetters[i] == wLetters[i]:
                        print(f"{gLetters[i]} IS RIGHT POSITION")
                        continue
                    print(f"{gLetters[i]} IS IN WORD")
                else:
                    print(f"{gLetters[i]} IS NOT IN WORD")
                    if gLetters[i] not in notinword:
                        notinword.append(gLetters[i])
        print()
