import operator

def main(input):
    registers = {}
    for line in input:
        # parse line
        key, is_inc, inc_amount, _, if_key, comparator, if_amount = line.split(" ")
        inc_amount = int(inc_amount)
        if_amount = int(if_amount)
        inc_multiplier = 1 if is_inc == "inc" else -1
        if key not in registers:
            registers[key] = 0
        if if_key not in registers:
            registers[if_key] = 0
        # Figure out sum now
        # Determine if the condition is true
        condition = False
        if comparator == ">":
            condition = registers[if_key] > if_amount
        elif comparator == "<":
            condition = registers[if_key] < if_amount
        elif comparator == "!=":
            condition = registers[if_key] != if_amount
        elif comparator == ">=":
            condition = registers[if_key] >= if_amount
        elif comparator == "<=":
            condition = registers[if_key] <= if_amount
        elif comparator == "==":
            condition = registers[if_key] == if_amount
        if condition is True:
            registers[key] += inc_multiplier * (inc_amount)
    print(registers)
    max_key = max(registers.items(), key=operator.itemgetter(1))[0]
    print(max_key, registers[max_key])


if __name__ == '__main__':
    #input = ["b inc 5 if a > 1", "a inc 1 if b < 5", "c dec -10 if a >= 1", "c inc -20 if c == 10"]
    #main(input)
    input = []
    with open("day_8.txt", 'r') as f:
        for line in f:
            input.append(line.strip())
        main(input)