def main(data):
    s = {}
    parents = []
    for record in data:
        info = record.split("->")
        if (len(info) > 1):
            # It's not a leaf node
            parent = info[0].strip().split(" ")[0]
            children = info[1].strip().split(",")
            for child in children:
                s[child.strip()] = 1
            # Check if parent exists or not
            # Can't check until all parents have been scraped. One of these will be the one which doesn't exist in the map
            parents.append(parent.strip())
        else:
            # leaf node
            program = record.split(" ")[0].strip()
            s[program] = 1
    print(parents)
    print(s)
    for parent in parents:
        if parent not in s:
            print("We have the parent: " + parent)
            break

if __name__ == '__main__':
    input = []
    with open('day_7.txt', 'r') as f:
        for line in f:
            input.append(line.strip())
    main(input)
