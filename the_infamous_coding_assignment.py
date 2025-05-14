# For old time's sake :)
import time
import random

def classic(h, rev=0, animate=0):
    f = 0
    if animate:
        f = 0.05
    if rev:
        for i in range(h, 0, -1):
            print(i * "■")
            time.sleep(f)
    else:
        for i in range(h):
            print(i * "■")
            time.sleep(f)
    

def tree(h, animate=0):
    f = 0
    if animate:
        f = 0.05
    for i in range(1, h, 2):
        print(int((h-i)/2) * " ", end="")
        print("■" * i)
        time.sleep(f)

def vee(h, animate=0):
    f = 0
    if animate:
        f = 0.05
    for i in range(h-1, 0, -2):
        print(int((h-i)/2) * " ", end="")
        print("■" * i)
        time.sleep(f)

def diamond(h, animate=0):
    f = 0
    if animate:
        f = 0.05
    half = int(((h/2)-1)/2)
    bottom = []
    for i in range(1, h, 2):
        ph = ""
        if int(((h-i)/2)) >= half:
            ph += int((h-i)/2) * " "
            ph += "■" * i
            print(ph)
            bottom.append(ph)
            time.sleep(f)
            continue
    for i in range(len(bottom)-2, -1, -1):
        print(bottom[i])
        time.sleep(f)

def timeDial(h, animate=0):
    f = 0
    if animate:
        f = 0.05
    mid = int(h/2)
    bottom = []
    for i in range(mid, 0, -2):
        ph = ""
        ph += int((h-i)/2) * " "
        ph += "■" * (i)
        print(ph)
        bottom.append(ph)
        time.sleep(f)

    for i in range(len(bottom)-2, -1, -1):
        print(bottom[i])
        time.sleep(f)


h = 50
"""
# Sleepy time
while True:
    x = random.randint(0,5)
    match x:
        case 0:
            timeDial(h, 1)
        case 1:
            tree(h,1)
        case 2:
            vee(h,1)
        case 3:
            classic(h,0,1)
        case 4:
            classic(h,1,1)
        case 5:
            diamond(h,1)
"""