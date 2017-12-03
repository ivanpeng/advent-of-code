
def generate_spiral(size, input):
    x = y = 0
    dx = 0
    dy = -1
    distance = 0
    for i in range(1, size**2):
        #print(str(i) + ": (" + str(x) + ", " + str(y) + ")")
        # Transform to absolute coordinates, with 1 being the center
        # First check if it's at the correct spot before incrementing in spiral
        if (i == input):
            distance = abs(x) + abs(y)  # absolute distance for manhattan to center
            break
        if x == y or (x < 0 and x == -y) or (x > 0 and x == 1-y):
            dx, dy = -dy, dx
        x, y = x+dx, y+dy
    return distance 


def main(num):
    i = 1
    while (i*i < num + 1):
        i += 1
    return generate_spiral(i, num)



if __name__ == '__main__':
    print(main(1))
    print(main(12))
    print(main(23))
    print(main(1024))
    print(main(277678))
