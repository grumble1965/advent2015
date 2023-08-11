""" Solution for Day 17 """

from itertools import combinations
from advent import Advent, Runner, file_to_string


class Day17(Advent):
    """ class for Day 17 solution """

    def __init__(self, input_text):
        super().__init__()
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
            for comb in iter_list:
                sum_ = 0
                for idx in comb:
                    sum_ += self.containers[idx]
                if sum_ == total_eggnog:
                    # cc = [self.containers[jdx]
                    #       for jdx in range(len(self.containers)) if jdx in comb]
                    # print(cc, sum_)
                    self.working_perms.add(comb)
        print(f"total working permutations = {len(self.working_perms)}")
        return len(self.working_perms)

    def part_two(self, total_eggnog=150):
        if len(self.working_perms) == 0:
            self.part_one(total_eggnog=total_eggnog)
        len_count = {}
        for perm in self.working_perms:
            perm_len = len(perm)
            if perm_len in len_count:
                len_count[perm_len] += 1
            else:
                len_count[perm_len] = 1
        min_perm = min(list(len_count.keys()))
        print(
            f"smallest permutation is length {min_perm} with {len_count[min_perm]} possible")
        return len_count[min_perm]


def main():
    """ stub for main() """
    aoc1 = Day17(file_to_string("day17-live.txt"))
    runner = Runner(aoc1)
    runner.run()


if __name__ == '__main__':
    main()
