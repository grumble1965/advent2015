from advent import Advent, Runner, File_to_String
from graph import Graph
from itertools import permutations
import sys


class Day09(Advent):
    def __init__(self, input_text):
        self.name = "9"
        self.lines = input_text
        self.g = Graph()

    def parse(self):
        for line in self.lines:
            tmp = line.strip()
            node1, _, node2, _, distance_str = tmp.split()
            distance = int(distance_str)
            # print(f"{node1} {node2} {distance}")

            if node1 not in self.g:
                self.g.add_node(node1)
            if node2 not in self.g:
                self.g.add_node(node2)
            self.g.add_edge(node1, node2, distance, bidirectional=True)

    def partA(self):
        # compute all paths
        shortest_distance, shortest_path = 999999, None
        for path in permutations(self.g.nodes()):
            # print(f"{path}")
            distance = self.g.distance_from_path(path)
            if distance < shortest_distance:
                shortest_distance = distance
                shortest_path = path

        print(f"{shortest_path} = {shortest_distance}")
        return shortest_distance

    def partB(self):
        # compute all paths
        longest_distance, longest_path = -1, None
        for path in permutations(self.g.nodes()):
            # print(f"{path}")
            distance = self.g.distance_from_path(path)
            if distance > longest_distance:
                longest_distance = distance
                longest_path = path

        print(f"{longest_path} = {longest_distance}")
        return longest_distance


def main():
    aoc1 = Day09(File_to_String("day09-live.txt"))
    runner = Runner(aoc1)
    runner.run()


if __name__ == '__main__':
    main()
