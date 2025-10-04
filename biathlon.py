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