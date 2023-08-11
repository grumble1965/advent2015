from advent import Advent, Runner, file_to_string
from itertools import combinations
import sys


class Day17(Advent):
    def __init__(self, input_text):
        self.name = "17"
        self.lines = input_text
        self.containers = []
        self.working_perms = set()

    def parse(self):
        for line in self.lines:
            tmp = line.strip()
            self.containers.append(int(tmp))

    def part_one(self, total_eggnog=150):
        for num_containers in range(len(self.containers)):
            iter_list = combinations(
                range(len(self.containers)), num_containers+1)
            for pp in iter_list:
                sum = 0
                for idx in pp:
                    sum += self.containers[idx]
                if sum == total_eggnog:
                    cc = [self.containers[jdx]
                          for jdx in range(len(self.containers)) if jdx in pp]
                    # print(cc, sum)
                    self.working_perms.add(pp)
        print(f"total working permutations = {len(self.working_perms)}")
        return len(self.working_perms)

    def part_two(self, total_eggnog=150):
        if len(self.working_perms) == 0:
            self.part_one(total_eggnog=total_eggnog)
        len_count = {}
        for p in self.working_perms:
            ll = len(p)
            if ll in len_count:
                len_count[ll] += 1
            else:
                len_count[ll] = 1
        min_perm = min(list(len_count.keys()))
        print(
            f"smallest permutation is length {min_perm} with {len_count[min_perm]} possible")
        return len_count[min_perm]


def main():
    aoc1 = Day17(file_to_string("day17-live.txt"))
    runner = Runner(aoc1)
    runner.run()


if __name__ == '__main__':
    main()
