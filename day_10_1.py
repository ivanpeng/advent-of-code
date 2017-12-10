
def main(input, set_size = 256):
    # Generate list first
    l = [x for x in range(set_size)]

    current_idx = 0
    current_skip = 0
    for elem in input:
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
        print(sublist)
        print(current_idx)
        print(l)
        print("=========")
    print(l[0]* l[1])



if __name__ == '__main__':
    #input = [3,4,1,5]
    #et_size = 5
    input = [120,93,0,90,5,80,129,74,1,165,204,255,254,2,50,113]
    main(input)