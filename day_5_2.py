def main(input):
    i = 0
    count = 0
    current_location = 0
    while (current_location < len(input)):
        # do the action
        #print("i: " + str(count) + ", current location: " + str(current_location))
        #print(input)
        current_location += input[i]
        # Special rule here if increment is greater than 3
        if (input[i] >= 3):
            input[i] -= 1
        else:
            input[i] += 1
        i = current_location
        count += 1
    print("Out at count " + str(count))


if __name__ == '__main__':
    input = []
    with open('day_5.txt', 'r') as f:
        for line in f:
            input.append(int(line.strip()))
    main(input)