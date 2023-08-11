""" Solution for Day 24 """

from itertools import accumulate, chain, combinations, filterfalse
import operator
from advent import Advent, Runner, file_to_string


class Day24(Advent):
    """ class for Day 24 solution """

    def __init__(self, input_text):
        super().__init__()
        self.name = "24"
        self.lines = input_text
        self.packages = set()

    def parse(self):
        for line in self.lines:
            tmp = line.strip()
            # print(f"{tmp}")
            self.packages.add(int(tmp))

    def part_one(self):
        total = sum(self.packages)
        # print(f"Total sum = {total}, Group sum = {total // 3}")

        candidates = []
        package_set = set(self.packages)
        for group_length in range(1, len(self.packages) - 1):
            for front in filterfalse(
                    lambda ss: sum(ss) != total // 3, combinations(self.packages, r=group_length)):
                remaining_set = package_set - set(front)
                remaining = list(remaining_set)
                left_iter = filterfalse(
                    lambda ss: sum(ss) != total // 3,
                    chain.from_iterable(
                        [combinations(remaining, r=ll) for ll in range(1, len(remaining))]))
                for _ in left_iter:
                    # any valid packing for left side implies a valid right side exists
                    # thus, the front packing is valid
                    front_group = sorted(front)
                    if front_group not in candidates:
                        candidates.append(front_group)
                    break

            # if any candidates have been found, don't make a longer packing
            if candidates:
                break

        # print(candidates)
        best = sorted(candidates,
                      key=lambda cc: list(accumulate(cc, operator.mul))[-1])[0]
        first_qe = list(accumulate(best, operator.mul))[-1]
        print('Part A: ', best, ' QE =', first_qe)

        return first_qe

    def part_two(self):
        total = sum(self.packages)
        # print(f"Total sum = {total}, Group sum = {total // 4}")

        candidates = []
        package_set = set(self.packages)
        for group_length in range(1, len(self.packages) - 2):
            for front in filterfalse(
                    lambda ss: sum(ss) != total // 4, combinations(self.packages, r=group_length)):
                remaining_set = package_set - set(front)
                remaining = list(remaining_set)
                trunk_iter = filterfalse(
                    lambda ss: sum(ss) != total // 4,
                    chain.from_iterable(
                        [combinations(remaining, r=ll) for ll in range(1, len(remaining) - 1)]))
                for trunk in trunk_iter:
                    early_exit = False
                    side_remaining_set = remaining_set - set(trunk)
                    side_remaining = list(side_remaining_set)
                    left_iter = filterfalse(
                        lambda ss: sum(ss) != total // 4,
                        chain.from_iterable([combinations(side_remaining, r=ll) for ll in
                                             range(1, len(side_remaining) - 1)]))
                    for _ in left_iter:
                        # any valid packing for left side implies a valid right side exists
                        # thus, the front packing is valid
                        front_group = sorted(front)
                        if front_group not in candidates:
                            candidates.append(front_group)
                        early_exit = True
                        break

                    if early_exit:
                        break

            # if any candidates have been found, don't make a longer packing
            if candidates:
                break

        # print(candidates)
        best = sorted(candidates,
                      key=lambda cc: list(accumulate(cc, operator.mul))[-1])[0]
        first_qe = list(accumulate(best, operator.mul))[-1]
        print('Part B: ', best, ' QE =', first_qe)
        return first_qe


def main():
    """ stub for main() """
    aoc1 = Day24(file_to_string("day24-live.txt"))
    runner = Runner(aoc1)
    runner.run()


if __name__ == '__main__':
    main()
