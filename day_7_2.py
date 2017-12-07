root_parent = "uownj" # figured out from 1st part of program

def map_sum(parent, weights, structure):
    # A recursive function to determine the weights of the programs
    totals = 0
    if parent in structure:
        children = structure[parent]
        for child in children:
            totals += map_sum(child, weights, structure)
        # Need to add the current parent's weight
        totals += weights[parent]
        #if parent == root_parent or parent in structure[root_parent]:
        print("Parent " + str(parent) + " with children " + str(children) + " has total " + str(totals))
    else:
        # Leaf node; parent has no children
        totals = weights[parent]
    return totals

def main(data):
    weights = {}
    names = []
    structure = {}
    for record in data:
        info = record.split("->")
        if (len(info) > 1):
            # It's not a leaf node
            # continue for now, we'll process it later
            # for now, save the data
            program = info[0].strip().split(" ")[0]
            weight = int(info[0].strip().split(" ")[1][1:-1].strip())
            weights[program] = weight
            parent = program
            children = [x.strip() for x in info[1].strip().split(",")]
            structure[parent] = children
        else:
            # leaf node
            leaf_node_info = record.split(" ")
            program = leaf_node_info[0].strip()
            weights[program] = int(leaf_node_info[1][1:-1].strip())
        names.append(program)

    # Now that we have the structure, we should do a manual group
    map_sum(root_parent, weights, structure)
    print(weights)
    


if __name__ == '__main__':
    input = []
    with open('day_7.txt', 'r') as f:
        for line in f:
            input.append(line.strip())
    main(input)
