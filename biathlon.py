from random import randint

open = 0
closed = 1

def splash():
    print()
    print("#########################################")
    print("##               Biathlon              ##")
    print("##                                     ##")
    print("##         a hit or miss game          ##")
    print("#########################################")
    print()

def is_open(target):
    if target == open:
        return True
    else:
        return False
    
def is_closed(target):
    if target == closed:
        return True
    else:
        return False
    
def new_targets():
    targets = []
    for _ in range(5):
        targets.append(open)
    return targets

def close_target(targets, position):
    targets[position] = closed
    return targets

def points(targets):
    n = 0

    for target in targets:
        if is_closed(target):
            n = n+1
    return n

def targets_to_string(targets):
    string = "     "
    for target in targets:
        if is_closed(target):
            string = string + f"* "
        else:
            string = string + f"O "
    return string

def view_targets(targets):
    print()
    print("     1 2 3 4 5")
    print()
    print(targets_to_string(targets))    
    print()

def random_hit():
    hit = randint(0,1)
    if hit:
        return True
    else:
        return False
    
def shoot(targets, position):
    hit = random_hit()

    if hit and is_open(targets[position]):
        close_target(targets,position)
        return "Hit on open target!"
    elif hit and is_closed(targets[position]):
        return "Hit on closed target!"
    else:
        return "Miss!"