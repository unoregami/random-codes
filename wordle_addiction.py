from english_words import get_english_words_set
import random


a = list(get_english_words_set(['web2'], lower=True))

def countWords():   # counts the words in english words set
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

def pickWord(five): # pick random word
    return five[random.randrange(0, len(five))]


# stores 5-letter words
five = list()
for i in a:
    if len(i) == 5:
        five.append(i.upper())

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

