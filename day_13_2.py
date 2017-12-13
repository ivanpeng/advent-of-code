import copy

def move_scanners(scanners, scanner_directions):
    for key in scanners:
        if scanner_directions[key] == 1:
            # going down the layer
            scanners[key].insert(0, 0)
            scanners[key].pop()
        else:
            # Coming back up the layer
            scanners[key].append(scanners[key].pop(0))
        # Final check to see if they have switched directions
        if scanners[key].index(1) == len(scanners[key]) - 1 and scanner_directions[key] == 1:
            scanner_directions[key] = -1
        if scanners[key].index(1) == 0 and scanner_directions[key] == -1:
            scanner_directions[key] = 1

def simulate(scanners, scanner_directions):
    # We're given a certain state of the scanners and firewall. Return true or false if it makes it through all the way through

    # Now that we have a map, let's initialize the movement of the packet
    # Keep in mind there are two steps to the event: packet moves FIRST, then scanner moves SECOND
    # Need to only track when packet moves onto scanner, NOT THE OTHER WAY
    pos = -1
    caught_arr = []
    while pos < input[-1][0]: # We haven't made it out yet
        # step 1: packet moves
        pos += 1
        # CHeck if caught
        # We check if the scanner's position at this time is at the top layer 0
        # Also need to check if the current position has a scanner
        if pos in scanners and scanners[pos][0] == 1:
            # Caught!
            caught_arr.append(pos)
        # step 2: all scanners move
        move_scanners(scanners, scanner_directions)
    if len(caught_arr) == 0:
        return True
    else:
        return False


def main(input):
    # Generate scanner map range first
    scanners = {}
    scanner_directions = {}
    for elem in input:
        depth, range = elem
        scanners[depth] = [0]*range
        scanner_directions[depth] = 1
    # Initalize each element in the array with 1, as that's the original position of the scanner
    for key in scanners:
        scanners[key][0] = 1
    wait = 0
    while True:
        is_successful = simulate(copy.deepcopy(scanners), copy.deepcopy(scanner_directions))
        if not is_successful:
            move_scanners(scanners, scanner_directions)
            wait += 1
        else:
            break
    print(wait)
    



if __name__ == '__main__':
    input = []
    with open('day_13.txt', 'r') as f:
        for line in f:
            stripped_line = [int(x.strip())  for x in line.split(":")]
            input.append((stripped_line[0], stripped_line[1]))
    print(input)
    main(input)