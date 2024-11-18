import string
import random
import time

a = input("Text: ")
letters = string.ascii_letters + string.whitespace
result = ""
for i in a:
    rand = ""
    while i != rand:
        rand = letters[random.randint(0, len(letters)-1)]
        if rand == string.whitespace:
            break
        print(result + rand)
        time.sleep(0.01)
    result = result + rand