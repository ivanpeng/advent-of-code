def main(input):
    count = 0
    for line in input:
        d = {}
        words = line.split(" ")
        is_valid = True
        for word in words:
            if word in d:
                is_valid = False
                break
            d.update({word: 1})
        if is_valid:
            count += 1
    return count

if __name__ == '__main__':
    input = []
    with open('day_4_input.txt', 'r') as f:
        for line in f:
            input.append(line.strip())
    print(input)
    print(main(input))