# 100 wordle plays * 10 = 20 to 21 average attempts
# ^^^ improve accuracies if can

import Wordle_Addiction as wrdl


five = wrdl.five

"""
# Algo for looking specific 5-letter words w/ specific letters in specific places
# Might improve accuracy (?)
for i in five:
    if "A" in i[3] and "K" in i[1]:
        print(i)
"""

def autoWordle(word, five):
    dLetters = []
    pLetters = []
    cLetters = ["A","A","A","A","A"]
    guesses = []
    wLetters = [i for i in word]
    attempts = 0 

    while True:
        # picking guesses
        if attempts == 0:
            guess = wrdl.pickWord(five)
            gLetters = [i for i in guess]
        else:
            # this is attempts > 0
            while True:
                isLetterInDiscard = False
                guess = wrdl.pickWord(five)
                gLetters = [i for i in guess]
                for i in gLetters:
                    if i in dLetters:
                        isLetterInDiscard = True
                if not isLetterInDiscard:
                    break
                
        attempts += 1
        guesses.append(guess)
        if guess == word:
            print(f"WORD: {word}\nATTEMPTS: {attempts}")    # \n GUESSES: {guesses}
            return attempts
            #break
        else:
            for i in range(5):
                if gLetters[i] in wLetters:
                    if gLetters[i] == wLetters[i]:
                        cLetters[i] = gLetters[i]
                else:
                    if gLetters[i] not in dLetters:
                        dLetters.append(gLetters[i])

inp = ""
at, w = 0, 0
"""
while inp != "n":
    word = wrdl.pickWord(five)
    at += autoWordle(word, five)
    w += 1
    inp = input("")
print(f"AVERAGE: {round(at/w, 1)}")
"""
ave = 0
for i in range(10):
    at, w = 0, 0
    for j in range(100):
        word = wrdl.pickWord(five)
        at += autoWordle(word, five)
        w += 1
    ave += at/w
    print(at/w)
print(round(ave/10, 1))