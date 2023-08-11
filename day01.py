""" Day 1 Solution """

from advent import Advent, Runner, file_to_string


class Day01(Advent):
    """ Day 1 solution class """

    def __init__(self, input_text):
        super().__init__()
        self.name = "1"
        self.line = input_text[0]

    def parse(self):
        pass

    def part_one(self):
        line = self.line
        left_parens, right_parens = line.count('('), line.count(')')
        print(f"Ultimate Floor = {left_parens - right_parens}")
        return left_parens - right_parens

    def part_two(self):
        line = self.line
        floor, position = 0, 1
        for char in line:
            if char == '(':
                floor += 1
            elif char == ')' and floor == 0:
                break
            elif char == ')' and floor > 0:
                floor -= 1
            position += 1
        print(f"Ultimate Position = {position}")
        return position


def main():
    """ stub for main() """
    aoc1 = Day01(file_to_string("day01-live.txt"))
    runner = Runner(aoc1)
    runner.run()


if __name__ == '__main__':
    main()
