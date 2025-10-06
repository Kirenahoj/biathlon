from random import randint

open = 0
closed = 1

def splash():           # Visar en splash screen när programmet körs.
    print()
    print("#########################################")
    print("##               Biathlon              ##")
    print("##                                     ##")
    print("##          a hit or miss game         ##")
    print("#########################################")
    print()

def is_open(target):     # Kontrollerar om målet är öppet.
    if target == open:
        return True
    else:
        return False
    
def is_closed(target):     # Kontrollerar om målet är stängt.
    if target == closed:
        return True
    else:
        return False
    
def new_targets():       # Skapar en ny måltavla och returnerar den som en lista.
    targets = []
    for _ in range(5):
        targets.append(open)
    return targets

def close_target(targets, position):        # Stänger målet på en given position.
    targets[position] = closed
    return targets

def points(targets):     # Beräknar hur många träffar man fick (antalet mål som är stängda).
    n = 0

    for target in targets:
        if is_closed(target):
            n = n+1
    return n

def targets_to_string(targets):      #  Omvandlar måltavlan till sträng-form. Öppna mål representeras av * och stängda av O.
    string = "     "
    for target in targets:
        if is_open(target):
            string = string + f"* "
        else:
            string = string + f"O "
    return string

def view_targets(targets):      # Skriver ut sträng-formen av måltavlan.
    print()
    print("     1 2 3 4 5")
    print()
    print(targets_to_string(targets))    
    print()

def random_hit():     # 50/50 om man träffar.
    hit = randint(0,1)
    if hit:
        return True
    else:
        return False
    
def shoot(targets, position):   # Representerar ett skott
    hit = random_hit()       # Kallar på random_hit för att avgöra om man träffar eller inte.

    if hit and is_open(targets[position]):    # Om träff och målet är öppet. Målet stängs.
        close_target(targets,position)
        return "Hit on open target!"
    elif hit and is_closed(targets[position]):     # Om träff och målet är stängt. Inget händer.
        return "Hit on closed target!"
    else:
        return "Miss!"
    
def parse_target(string):
    if string.isnumeric() and 1 <= int(string) <= 5:      # Om strängen kan tolkas som ett positivt heltal och är mellan 1 och 5. 
        return int(string) - 1     # Talet minskas med 1 för att stämma överens med indexet för listan
    else:
        return None
    
def play_game(): # Funktion där själva spelet körs
    splash()
    
    shots = 5
    print(f"You got {shots} shots.")
    
    targets = new_targets()
    for n in range(shots):
        view_targets(targets)
        
        while True:      # Kontrollerar så att inputen är 1-5. Annars får man försöka igen.
            target_choice = parse_target(input(f"Shot nr {n+1} at target: "))
            if target_choice == None:
                print("You have to enter 1-5!")
                print()
            else:
                break

        print()
        print(shoot(targets, target_choice))

    view_targets(targets)
    hits = points(targets) 
    print(f"You hit {hits}/5 targets!")
    print()
        


play_game()    # Spelet startar
