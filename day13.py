from advent import Advent, Runner, file_to_string
from itertools import permutations
import sys


class Day13(Advent):
    def __init__(self, input_text):
        self.name = "13"
        self.lines = input_text
        self.costs = {}
        self.family = set()

    def parse(self):
        for line in self.lines:
            tmp = line.strip().replace('.', '')
            words = tmp.split()
            p0, direction, amount, p1 = words[0], words[2], int(
                words[3]), words[10]
            if direction == 'lose':
                amount = -amount
            # print(f"{p0}->{p1} = {amount}")
            self.costs[(p0, p1)] = amount
            self.family.add(p0)
            self.family.add(p1)

    def findBestPermutation(self):
        best_score, best_permutation = None, None
        for combo in permutations(self.family):
            # print(combo)
            score = 0
            for p0 in self.family:
                combo_list = list(combo)
                p0_idx = combo_list.index(p0)
                p_left_idx, p_right_idx = p0_idx-1, p0_idx+1
                if p_left_idx < 0:
                    p_left_idx += len(combo_list)
                if p_right_idx >= len(combo_list):
                    p_right_idx -= len(combo_list)
                p_left, p_right = combo_list[p_left_idx], combo_list[p_right_idx]
                # print(f"{p_left} <- {p0} = {costs[(p0, p_left)]}")
                # print(f"{p0} -> {p_right} = {costs[(p0, p_right)]}")
                score += self.costs[(p0, p_left)]
                score += self.costs[(p0, p_right)]

            if best_score is None or score > best_score:
                best_score = score
                best_permutation = combo
        return (best_permutation, best_score)

    def part_one(self):
        best_permutation, best_score = self.findBestPermutation()
        print(f"best combo = {best_permutation} with happiness = {best_score}")
        return best_score

    def part_two(self):
        for f in self.family:
            self.costs[(f, 'me')] = 0
            self.costs[('me', f)] = 0
        self.family.add('me')

        best_permutation, best_score = self.findBestPermutation()
        print(f"best combo = {best_permutation} with happiness = {best_score}")
        return best_score


def main():
    aoc1 = Day13(file_to_string("day13-live.txt"))
    runner = Runner(aoc1)
    runner.run()


if __name__ == '__main__':
    main()
