""" Solution for Day 13 """

from itertools import permutations
from advent import Advent, Runner, file_to_string


class Day13(Advent):
    """ class for Day 13 solution """

    def __init__(self, input_text):
        super().__init__()
        self.name = "13"
        self.lines = input_text
        self.costs = {}
        self.family = set()

    def parse(self):
        for line in self.lines:
            tmp = line.strip().replace('.', '')
            words = tmp.split()
            p_0, direction, amount, p_1 = words[0], words[2], int(
                words[3]), words[10]
            if direction == 'lose':
                amount = -amount
            # print(f"{p_0}->{p_1} = {amount}")
            self.costs[(p_0, p_1)] = amount
            self.family.add(p_0)
            self.family.add(p_1)

    def find_best_permutation(self):
        """ check all permuations for the best """
        best_score, best_permutation = None, None
        for combo in permutations(self.family):
            # print(combo)
            score = 0
            for p_0 in self.family:
                combo_list = list(combo)
                p0_idx = combo_list.index(p_0)
                p_left_idx, p_right_idx = p0_idx-1, p0_idx+1
                if p_left_idx < 0:
                    p_left_idx += len(combo_list)
                if p_right_idx >= len(combo_list):
                    p_right_idx -= len(combo_list)
                p_left, p_right = combo_list[p_left_idx], combo_list[p_right_idx]
                # print(f"{p_left} <- {p0} = {costs[(p0, p_left)]}")
                # print(f"{p0} -> {p_right} = {costs[(p0, p_right)]}")
                score += self.costs[(p_0, p_left)]
                score += self.costs[(p_0, p_right)]

            if best_score is None or score > best_score:
                best_score = score
                best_permutation = combo
        return (best_permutation, best_score)

    def part_one(self):
        best_permutation, best_score = self.find_best_permutation()
        print(f"best combo = {best_permutation} with happiness = {best_score}")
        return best_score

    def part_two(self):
        for person in self.family:
            self.costs[(person, 'me')] = 0
            self.costs[('me', person)] = 0
        self.family.add('me')

        best_permutation, best_score = self.find_best_permutation()
        print(f"best combo = {best_permutation} with happiness = {best_score}")
        return best_score


def main():
    """ stub for main() """
    aoc1 = Day13(file_to_string("day13-live.txt"))
    runner = Runner(aoc1)
    runner.run()


if __name__ == '__main__':
    main()
