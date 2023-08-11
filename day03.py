from advent import Advent, Runner, file_to_string
import sys


class Day03(Advent):
    def __init__(self, input_text):
        self.name = "3"
        self.line = input_text[0]

    def parse(self):
        pass

    def calc_new_location(self, x, y, dir):
        x_new, y_new = 0, 0
        if dir == '^':
            x_new, y_new = x, y+1
        elif dir == 'v':
            x_new, y_new = x, y-1
        elif dir == '<':
            x_new, y_new = x-1, y+0
        elif dir == '>':
            x_new, y_new = x+1, y+0
        else:
            print(f"Unknown direction {dir}")
        return (x_new, y_new)

    def part_one(self):
        houses = {}
        x, y = 0, 0
        houses[(x, y)] = 1
        for ch in self.line:
            location = self.calc_new_location(x, y, ch)
            x, y = location
            if location in houses:
                houses[location] += 1
            else:
                houses[location] = 1

        visits = len(houses.keys())
        print(f"Houses receiving a present = {visits}")
        return visits

    def part_two(self):
        houses = {}
        x, y = [0, 0], [0, 0]
        houses[(0, 0)] = 2
        turn = 0
        houses[(x[turn], y[turn])] = 1
        for ch in self.line:
            location = self.calc_new_location(x[turn], y[turn], ch)
            x[turn], y[turn] = location
            if (location) in houses:
                houses[location] += 1
            else:
                houses[location] = 1

            turn += 1
            if turn == 2:
                turn = 0

        visits = len(houses.keys())
        print(f"Houses receiving a present = {visits}")
        return visits


def main():
    aoc1 = Day03(file_to_string("day03-live.txt"))
    runner = Runner(aoc1)
    runner.run()


if __name__ == '__main__':
    main()
