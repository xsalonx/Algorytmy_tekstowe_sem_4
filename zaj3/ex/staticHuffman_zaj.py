

class Node:
    def __init__(self, a, w):
        pass

def huffman(letter_counts):
    nodes = []
    for a, weight in letter_counts.items():
        nodes.append(Node(a, weight))
    internal_nodes = []
    leafs = sorted(nodes, key=lambda n: n.weight)
    while(len(leafs) + len(internal_nodes) > 1):
        pass
        # element_1, element_2 = # elementy nodes i internal nodes o najniższym koszcie, usunięte z list
        # internal_nodes.append(Node(element_1, element_2, element_1.weight + element_2.weight)
    return internal_nodes[0]


if __name__ == '__main__':
    pass