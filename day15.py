""" Solution for Day 15 """

from itertools import product
from advent import Advent, Runner, file_to_string


class Day15(Advent):
    """ class for Day 15 solution """

    def __init__(self, input_text):
        super().__init__()
        self.name = "15"
        self.lines = input_text
        self.cookies = []

    def parse(self):
        for line in self.lines:
            tmp = line.strip()

            name, attributes = tmp.split(':')
            cap, dur, fla, tex, cal = attributes.split(',')
            capacity = int(cap.split()[1])
            durability = int(dur.split()[1])
            flavor = int(fla.split()[1])
            texture = int(tex.split()[1])
            calories = int(cal.split()[1])
            # print(f"{name}: Capacity = {capacity} Durability = {durability}
            # Flavor = {flavor} Texture = {texture} Calories = {calories}")
            this_tuple = (name, capacity, durability,
                          flavor, texture, calories)
            self.cookies.append(this_tuple)

    def calc_score(self, cook, quants):
        """ calculate the score of this cookie """
        sum_cap, sum_dur, sum_flav, sum_text, sum_kcal = 0, 0, 0, 0, 0
        for idx, (_, cap, dur, flav, text, kcal) in enumerate(cook):
            # (_, c, d, f, t, kcal) = cook[idx]
            # # print(f"{name}: {c} {d} {f} {t} {kcal}")
            sum_cap += quants[idx]*cap
            sum_dur += quants[idx]*dur
            sum_flav += quants[idx]*flav
            sum_text += quants[idx]*text
            sum_kcal += quants[idx]*kcal
        score = (0 if sum_cap < 0 else sum_cap)
        score *= (0 if sum_dur < 0 else sum_dur)
        score *= (0 if sum_flav < 0 else sum_flav)
        score *= (0 if sum_text < 0 else sum_text)
        # score += (0 if sum_kcal < 0 else sum_kcal)
        # print(f"{quants} -> {score}")
        return score

    def part_one(self):
        best_score = None
        best_recipe = None
        for (ing_a, ing_b, ing_c) in product(range(101), range(101), range(101)):
            if ing_a+ing_b <= 100 and ing_a+ing_b+ing_c <= 100:
                ing_d = 100 - (ing_a+ing_b+ing_c)
                if ing_d >= 0:
                    ratio = [ing_a, ing_b, ing_c, ing_d]
                    # print(f"  {ratio} = {sum(ratio)}")
                    score = self.calc_score(self.cookies, ratio)
                    if best_score is None or score > best_score:
                        best_score = score
                        best_recipe = ratio

        print(f"Best score is {best_score} with recipe {best_recipe}")
        return best_score

    def calc_score_kcal(self, cook, quants):
        """ calculate score including calories """
        sum_cap, sum_dur, sum_flav, sum_text, sum_kcal = 0, 0, 0, 0, 0
        for idx, (_, cap, dur, flav, text, kcal) in enumerate(cook):
            # print(f"{name}: {c} {d} {f} {t} {kcal}")
            sum_cap += quants[idx]*cap
            sum_dur += quants[idx]*dur
            sum_flav += quants[idx]*flav
            sum_text += quants[idx]*text
            sum_kcal += quants[idx]*kcal
        score = (0 if sum_cap < 0 else sum_cap)
        score *= (0 if sum_dur < 0 else sum_dur)
        score *= (0 if sum_flav < 0 else sum_flav)
        score *= (0 if sum_text < 0 else sum_text)
        score = (0 if sum_kcal != 500 else score)
        # print(f"{quants} -> {score}")
        return score

    def part_two(self):
        best_score = None
        best_recipe = None
        for (ing_a, ing_b, ing_c) in product(range(101), range(101), range(101)):
            if ing_a+ing_b <= 100 and ing_a+ing_b+ing_c <= 100:
                ing_d = 100 - (ing_a+ing_b+ing_c)
                if ing_d >= 0:
                    ratio = [ing_a, ing_b, ing_c, ing_d]
                    # print(f"  {ratio} = {sum(ratio)}")
                    score = self.calc_score_kcal(
                        self.cookies, ratio)
                    if best_score is None or score > best_score:
                        best_score = score
                        best_recipe = ratio

        print(
            f"Best 500 calories score is {best_score} with recipe {best_recipe}")
        return best_score


def main():
    """ stub for main() """
    aoc1 = Day15(file_to_string("day15-live.txt"))
    runner = Runner(aoc1)
    runner.run()


if __name__ == '__main__':
    main()
