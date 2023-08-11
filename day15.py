from advent import Advent, Runner, file_to_string
from itertools import product
import sys


class Day15(Advent):
    def __init__(self, input_text):
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
            # print(f"{name}: Capacity = {capacity} Durability = {durability} Flavor = {flavor} Texture = {texture} Calories = {calories}")
            tt = (name, capacity, durability, flavor, texture, calories)
            self.cookies.append(tt)

    def calc_score(self, cook, quants):
        sum_c, sum_d, sum_f, sum_t, sum_kcal = 0, 0, 0, 0, 0
        for idx in range(len(cook)):
            (name, c, d, f, t, kcal) = cook[idx]
            # print(f"{name}: {c} {d} {f} {t} {kcal}")
            sum_c += quants[idx]*c
            sum_d += quants[idx]*d
            sum_f += quants[idx]*f
            sum_t += quants[idx]*t
            sum_kcal += quants[idx]*kcal
        score = (0 if sum_c < 0 else sum_c)
        score *= (0 if sum_d < 0 else sum_d)
        score *= (0 if sum_f < 0 else sum_f)
        score *= (0 if sum_t < 0 else sum_t)
        # score += (0 if sum_kcal < 0 else sum_kcal)
        # print(f"{quants} -> {score}")
        return score

    def part_one(self):
        best_score = None
        best_recipe = None
        for (a, b, c) in product(range(101), range(101), range(101)):
            if a+b <= 100 and a+b+c <= 100:
                d = 100 - (a+b+c)
                if d >= 0:
                    ratio = [a, b, c, d]
                    # print(f"  {ratio} = {sum(ratio)}")
                    score = self.calc_score(self.cookies, ratio)
                    if best_score is None or score > best_score:
                        best_score = score
                        best_recipe = ratio

        print(f"Best score is {best_score} with recipe {best_recipe}")
        return best_score

    def calc_score_kcal(self, cook, quants):
        sum_c, sum_d, sum_f, sum_t, sum_kcal = 0, 0, 0, 0, 0
        for idx in range(len(cook)):
            (name, c, d, f, t, kcal) = cook[idx]
            # print(f"{name}: {c} {d} {f} {t} {kcal}")
            sum_c += quants[idx]*c
            sum_d += quants[idx]*d
            sum_f += quants[idx]*f
            sum_t += quants[idx]*t
            sum_kcal += quants[idx]*kcal
        score = (0 if sum_c < 0 else sum_c)
        score *= (0 if sum_d < 0 else sum_d)
        score *= (0 if sum_f < 0 else sum_f)
        score *= (0 if sum_t < 0 else sum_t)
        score = (0 if sum_kcal != 500 else score)
        # print(f"{quants} -> {score}")
        return score

    def part_two(self):
        best_score = None
        best_recipe = None
        for (a, b, c) in product(range(101), range(101), range(101)):
            if a+b <= 100 and a+b+c <= 100:
                d = 100 - (a+b+c)
                if d >= 0:
                    ratio = [a, b, c, d]
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
    aoc1 = Day15(file_to_string("day15-live.txt"))
    runner = Runner(aoc1)
    runner.run()


if __name__ == '__main__':
    main()
