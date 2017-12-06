def make_allocation(max_bank, idx, length):
    arr = [0]*length
    # Final operation of subtracting max bank to allocation so that it works out in the addition
    arr[idx] = arr[idx] - max_bank
    i = idx + 1
    while (max_bank > 0):
        j = i % length
        max_bank -= 1
        arr[j] += 1
        i += 1
    return arr

def allocate_banks(input, allocation): 
    return [a + b for a, b in zip(input, allocation)]

def main(input):
    # Allocation cycle first
    print(input)
    count = 0
    input_history = []
    new_input = input[:]
    while (new_input not in input_history):
        input_history.append(new_input)
        count += 1
        
        allocation = make_allocation(max(new_input), new_input.index(max(new_input)), len(new_input))
        new_input = allocate_banks(new_input, allocation)
        print(new_input)
    print(count)
        
    

if __name__ == '__main__':
    #input = [0, 2, 7, 0]
    input = [0, 5, 10, 0, 11,  14,  13,  4,   11,  8,   8,   7,   1,   4,   12,  11]
    main(input)