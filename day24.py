""" Solution for Day 24 """

from advent import Advent, Runner, file_to_string


class Day24(Advent):
    """ class for Day 24 solution """

    def __init__(self, input_text):
        super().__init__()
        self.name = "24"
        self.lines = input_text

    def parse(self):
        pass

    def part_one(self):
        return None

    def part_two(self):
        return None


def main():
    """ stub for main() """
    aoc1 = Day24(file_to_string("day24-live.txt"))
    runner = Runner(aoc1)
    runner.run()


if __name__ == '__main__':
    main()
