""" Solution for Day 9 """

from itertools import permutations
from graph import Graph
from advent import Advent, Runner, file_to_string


class Day09(Advent):
    """ class for Day 9 solution """

    def __init__(self, input_text):
        super().__init__()
        self.name = "9"
        self.lines = input_text
        self.graph = Graph()

    def parse(self):
        for line in self.lines:
            tmp = line.strip()
            node1, _, node2, _, distance_str = tmp.split()
            distance = int(distance_str)
            # print(f"{node1} {node2} {distance}")

            if node1 not in self.graph:
                self.graph.add_node(node1)
            if node2 not in self.graph:
                self.graph.add_node(node2)
            self.graph.add_edge(node1, node2, distance, bidirectional=True)

    def part_one(self):
        # compute all paths
        shortest_distance, shortest_path = 999999, None
        for path in permutations(self.graph.nodes()):
            # print(f"{path}")
            distance = self.graph.distance_from_path(path)
            if distance < shortest_distance:
                shortest_distance = distance
                shortest_path = path

        print(f"{shortest_path} = {shortest_distance}")
        return shortest_distance

    def part_two(self):
        # compute all paths
        longest_distance, longest_path = -1, None
        for path in permutations(self.graph.nodes()):
            # print(f"{path}")
            distance = self.graph.distance_from_path(path)
            if distance > longest_distance:
                longest_distance = distance
                longest_path = path

        print(f"{longest_path} = {longest_distance}")
        return longest_distance


def main():
    """ stub for main() """
    aoc1 = Day09(file_to_string("day09-live.txt"))
    runner = Runner(aoc1)
    runner.run()


if __name__ == '__main__':
    main()
