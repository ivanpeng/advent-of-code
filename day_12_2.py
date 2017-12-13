
node_set = set()
node_set.add(0)
seen_nodes = {0}

def search_for_adjacent_nodes(node_list, m):
    if (len(node_list) > 0):
        for node in node_list:
            if node not in node_set and node not in seen_nodes:
                seen_nodes.add(node)
                node_set.add(node)
                search_for_adjacent_nodes(m[node], m)

    
def main(input):
    s = set()
    s.add(0)
    m = {}
    for line in input:
        root_node, branch_nodes = line.split(" <-> ")
        root_node = int(root_node)
        branch_nodes = [int(x.strip()) for x in branch_nodes.split(",")]
        m[root_node] = branch_nodes
    # 
    group_count = 0
    for key in m:
        prev_node_set_size = len(node_set)
        search_for_adjacent_nodes(m[key], m)
        post_node_set_size = len(node_set)
        if prev_node_set_size != post_node_set_size:
            group_count += 1
    print(group_count)

if __name__ == '__main__':
    # input = ["0 <-> 2", "1 <-> 1", "2 <-> 0, 3, 4", "3 <-> 2, 4", "4 <-> 2, 3, 6", "5 <-> 6", "6 <-> 4, 5"]
    # main(input)
    input = []
    with open('day_12.txt', 'r') as f:
        for line in f:
            input.append(line.strip())
        print(input)
        main(input)