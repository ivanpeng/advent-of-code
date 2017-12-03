
def calculate_surrounding_value(grid, x, y):
    return grid[x-1][y+1] + grid[x][y+1] + grid[x+1][y+1] + grid[x+1][y] + grid[x+1][y-1] + grid[x][y-1] + grid[x-1][y-1] + grid[x-1][y]


def generate_spiral(size, input):
    grid = [[0 for i in range(size)] for j in range(size)]
    x = y = 0
    dx = 0
    dy = -1
    for i in range(1, size**2):
        # Transform to absolute coordinates, with 1 being the center
        # Write value at this square first
        if (i == 1):
            value_at_square = 1
        else:
            value_at_square = calculate_surrounding_value(grid, x, y)
        grid[x][y] = value_at_square
        print(str(value_at_square) + ": (" + str(x) + ", " + str(y) + ")")
        if (value_at_square > input):
            return value_at_square
        if x == y or (x < 0 and x == -y) or (x > 0 and x == 1-y):
            dx, dy = -dy, dx
        x, y = x+dx, y+dy
    return None


def main(num):
    i = 1
    while (i*i < num + 1):
        i += 1
    return generate_spiral(i + 1, num) # Need a bigger spiral in this situation because of the 0s summing up



if __name__ == '__main__':
    # print(main(1))
    # print(main(12))
    # print(main(23))
    # print(main(1024))
    print(main(277678))
