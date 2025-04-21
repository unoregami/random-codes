# 100 wordle plays * 10 = 20 to 21 average attempts
# ^^^ improve accuracies if can

# Auto_Wordle2 = added consideration for words w/ correct letters, added "the wordle setup", improved computing speed, cleaner/concise look 
# Auto_Wordle2 got ~8 to 8.6 attempts/game. HUGE INCREASE!

# Using combined list of new Letterpress words list and the ol' web2. Average attempts went up to ~ 8.4 to 9.2 attempts/game & ~9.1 attempts/1000 games... not bad
# BUT, still not up to wordle standards as wordle only has 6 attempts per game.

import Wordle_Addiction as wrdl


five = wrdl.five


"""
# Algo for looking specific 5-letter words w/ specific letters in specific places
# Might improve accuracy (?)
for i in five:
    if "A" in i[3] and "K" in i[1]:
        print(i)
"""

def pickGuessWord(guessList, dLetters, cLetters, five):
    # searches for more specific words w/ specific letters
    removedFromGuessListCounter = 0     # adjust guessList length based on words with discarded letters.

    for i in range(len(cLetters)):
        if cLetters[i] == "-":
            continue
        if len(guessList) == 0:
            for j in five:
                if cLetters[i] in j[i]:
                    guessList.append(j)
        else:
            guessListPh = []
            for j in guessList:
                if cLetters[i] in j[i]:
                    guessListPh.append(j)
            guessList = guessListPh.copy()
        

    while True:
        isLetterInDiscard = False
        if len(guessList) == 0: # pick random if cLetters is all empty
            guess = wrdl.pickWord(five)
        else:
            guess = wrdl.pickWord(guessList)
        gLetters = [i for i in guess]
        for i in range(len(gLetters)):
            if gLetters[i] in dLetters[i]:
                isLetterInDiscard = True
                removedFromGuessListCounter += 1
                break
        if not isLetterInDiscard:
            return guessList, guess, gLetters, removedFromGuessListCounter

def autoWordle(word, five):
    dLetters = [[],[],[],[],[]]
    cLetters = ["-","-","-","-","-"]
    guesses = []
    guessList = []
    wLetters = [i for i in word]
    attempts = 0 
    rFGLC = 0   # abbr. removedFromGuessListCounter

    while True:
        print(cLetters)

        # picking guesses
        if attempts == 0:
            guess = wrdl.pickWord(five)
            gLetters = [i for i in guess]
        else:
            # this is attempts > 0
            guessList, guess, gLetters, rFGLC = pickGuessWord(guessList, dLetters, cLetters, five)

        attempts += 1
        guesses.append(guess)
        if guess == word:
            print(f"WORD: {word}\nATTEMPTS: {attempts}")    # \n GUESSES: {guesses}
            return attempts
        for i in range(5):
            if cLetters[i] != "-":
                continue
            if gLetters[i] == wLetters[i]:
                cLetters[i] = gLetters[i]
            else:
                if gLetters[i] not in dLetters[i]:
                    dLetters[i].append(gLetters[i])
        
        print(len(guessList)-rFGLC)
        print(guess)


at, w = 0, 0

# Custom wordle plays
inp = ""
while inp != "n":
    word = wrdl.pickWord(five)
    at += autoWordle(word, five)
    w += 1
    inp = input("")
print(f"AVERAGE: {round(at/w, 1)}")
"""

# Auto 1000 wordle plays
ave = 0
for i in range(10):
    at, w = 0, 0
    for j in range(100):
        word = wrdl.pickWord(five)
        at += autoWordle(word, five)
        w += 1
    ave += at/w
    print(f"AVERAGE ATTEMPTS/game: {at/w}")
print(f"AVERAGE ATTEMPTS/1000 games: {round(ave/10, 1)}")
"""
