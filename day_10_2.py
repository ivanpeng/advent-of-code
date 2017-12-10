def convert_string_to_ascii_codes(input):
    res = []
    for char in input:
        res.append(ord(char))
    # Now we have that, add the "salt" character
    res.extend([17, 31, 73, 47, 23])
    return res

def run_multiple_rounds(l, num_repeat):
    current_idx = 0
    current_skip = 0
    for i in range(num_repeat):
        for elem in l:
            sublist = []
            for absolute_index in range(current_idx, current_idx + elem):
                relative_index = absolute_index % len(l)
                sublist.append(l[relative_index])
            sublist = list(reversed(sublist))
            # merge this sublist to the original list
            j = 0
            for absolute_index in range(current_idx, current_idx + elem):
                relative_index = absolute_index % len(l)
                l[relative_index] = sublist[j]
                j += 1
            # Now move
            current_idx += elem + current_skip
            current_idx = current_idx % len(l)
            # Increment skip
            current_skip += 1
    return l

def dense_hash(l):
    dl = [0]*16
    for i in range(16):
        # Initialize stuff
        dl[i] = l[i*16]
        for j in range(i*16+1, i*16 + 16):
            dl[i] ^= l[j]
    print(dl)
    return dl

def knot_hash(dl):
    # Finally, write hex decimal
    output = ""
    for e in dl:
        s = hex(e)[2:]
        if (len(s) > 2):
            output += s
        else:
            output += "0" + s
    return output


def main(input, set_size = 256):
    # Generate list first
    l = [x for x in range(set_size)]
    new_l = run_multiple_rounds(l, 64)
    dl = dense_hash(new_l)
    output = knot_hash(dl)
    print(input)
    print(new_l)
    print(dl)
    print(output)


if __name__ == '__main__':
    input = "120,93,0,90,5,80,129,74,1,165,204,255,254,2,50,113"
    
    main(convert_string_to_ascii_codes(input))