import random
import time

def insertBullet(valve):
    # For "loading"
    phrases = [
        "Inserting bullet", 
        "Deleting browser history", 
        "Preparing vodka", 
        "Attempting to call loved ones", 
        "All-in", 
        "Baking a cake", 
        "Taking adderall",
        "Locking in",
        "Doomscrolling"]
    index = random.randint(1, 2)
    for i in range(index):
        print(phrases[random.randint(0, len(phrases)-1)], end='...\n')
        time.sleep(2)
    print()

    while True:
        index = random.randint(0,5) # Picks random position in the chamber, if 0 put bullet else random again
        if valve[index] != 1:
            valve[index] = 1
            break

def spinChamber(valve):
    # Same concept with "loading"
    print("Spinning...")
    for i in range(random.randint(1,2)):
        time.sleep(2)
        print("...", end="\n")
    print()

    # Picks random number 1-6 for revolution of the chamber. Adjusts the bullets in the chamber accordingly.
    k = random.randint(1,6)
    for j in range(k):
        x = valve.copy()
        for i in range(len(valve)-1):
            if i == 0:
                valve[0] = x[-1]
            valve[i+1] = x[i]


valve = [0,0,0,0,0,0]
spins, spinH = 3, 0
bullet = 0
history = []

while True:
    x = input("Play russian roulette? ").lower()
    if x == "n" or x == "no":
        break
    while True:
        if valve.count(0) == 1: # breaks loop if only 1 slot free in the chamber.
            print("congrats. now leave.")
            print("\nGAME HISTORY")
            for i in history: print(i)
            exit()
        
        insertBullet(valve)
        if valve.count(1) == 1:
            print(f'{valve.count(1)} bullet in chamber.')   # boilerplate for bullet amount
        else:
            print(f'{valve.count(1)} bullets in chamber.')
        bullet += 1
        history.append(f'Bullet {bullet}: {valve}')

        while True:
            x = input(f"Click or Spin again ({spins} left) ").lower()   # asks user to click or spin
            if x == "s" or x == "spin":
                if spins > 0:   # checks if there are spins left
                    spins -= 1  # decrement spin
                    spinChamber(valve)
                    spinH += 1  # increment spin in history
                    history.append(f'Spin   {spinH}: {valve}')
                    continue
                else:
                    print("no more spins left buddy.")
            break
        
        # "loading"
        print("Clicking...")
        for i in range(0, 3):
            time.sleep(2)
            print('...',end='\n')

        # if still alive
        if valve[0] != 1:
            print('nice\n')
            time.sleep(2)
            continue
        # if not, here.
        print('you\'re dead.')
        print('\nGAME HISTORY')
        for i in history: print(i)
        exit()
        

# if n/no, here.
print("Pussy.")
exit()
