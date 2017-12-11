def cube_distance(a, b):
    # two 3-tuples
    # probably a generic way to do this but easier to do it just manually
    return max(abs(a[0]-b[0]), abs(a[1]-b[1]), abs(a[2]-b[2]))

def main(input):
    # Need to act on 3 axes, and track how far we go in that, each time
    # From that we'll do some pythagorean math
    dir_increment_map = {'n': (0, 1, -1), 'ne': (1, 0, -1), 'se': (1, -1, 0), 's': (0, -1, 1), 'sw': (-1, 0, 1), 'nw': (-1, 1, 0)}
    absolute_distance = (0, 0, 0)
    for direction in input:
        absolute_distance = tuple(map(sum,zip(absolute_distance, dir_increment_map[direction])))
    print(absolute_distance)
    # Now calculate absolute distance from (0, 0, 0) to this distance
    print(cube_distance(absolute_distance, (0,0,0)))


if __name__ == '__main__':
    # directions: n, ne, se, s, sw, nw

    with open('day_11.txt', 'r') as f:
        input = f.readline().split(",")
        main(input)