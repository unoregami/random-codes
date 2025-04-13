import random
import time

def insertBullet(valve):
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
        index = random.randint(0,5)
        if valve[index] != 1:
            valve[index] = 1
            break

def spinChamber(valve):
    print("Spinning...")
    for i in range(random.randint(1,2)):
        time.sleep(2)
        print("...", end="\n")
    print()
    
    for i in range(len(valve)):
        x = random.randint(0,5)
        y = valve[x]
        valve[x] = valve[i]
        valve[i] = y

valve = [0,0,0,0,0,0]
spins, spinH = 3, 0
bullet = 0
history = []

while True:
    x = input("Play russian roulette? ").lower()
    if x == "n" or x == "no":
        break
    while True:
        if valve.count(0) == 1:
            print("congrats. now leave.")
            print("\nGAME HISTORY")
            for i in history: print(i)
            exit()
        
        insertBullet(valve)
        if valve.count(1) == 1:
            print(f'{valve.count(1)} bullet in chamber.')
        else:
            print(f'{valve.count(1)} bullets in chamber.')
        bullet += 1
        history.append(f'Bullet {bullet}: {valve}')

        while True:
            x = input(f"Click or Spin again ({spins} left) ").lower()
            if x == "s" or x == "spin":
                if spins > 0:
                    spins -= 1
                    spinChamber(valve)
                    spinH += 1
                    history.append(f'Spin   {spinH}: {valve}')
                    continue
                else:
                    print("no more spins left buddy.")
                    break
            break
        
        print("Clicking...")
        for i in range(0, 3):
            time.sleep(2)
            print('...',end='\n')

        if valve[0] != 1:
            print('nice\n')
            time.sleep(2)
            continue
        print('you\'re dead.')
        print('\nGAME HISTORY')
        for i in history: print(i)
        exit()
        

print("Pussy.")
exit()


