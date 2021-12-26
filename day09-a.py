import sys
from graph import Graph
from itertools import permutations


def main():
    if len(sys.argv) != 2:
        sys.exit("Please provide a file name for input data")

    g = Graph()

    filename = sys.argv[1]
    with open(filename, "r") as inputfile:
        while True:
            line = inputfile.readline()
            if not line:
                break
            tmp = line.strip()
            node1, _, node2, _, distance_str = tmp.split()
            distance = int(distance_str)
            # print(f"{node1} {node2} {distance}")

            if node1 not in g:
                g.add_node(node1)
            if node2 not in g:
                g.add_node(node2)
            g.add_edge(node1, node2, distance, bidirectional=True)
        # print(g)

        # compute all shortest paths
        foo = g.all_pairs_shortest_paths()
        # print(foo)

        # compute all paths
        shortest_distance, shortest_path = 999999, None
        for path in permutations(g.nodes()):
            # print(list(path))
            distance = 0
            for idx in range(1,len(path)) :
                c1, c2 = path[idx-1], path[idx]
                # print(f"   {c1} -> {c2}")
                distance += foo[c1][c2]
            if distance < shortest_distance:
                shortest_distance = distance
                shortest_path = path

        print(f"{shortest_path} = {shortest_distance}")

if __name__ == '__main__':
    main()
