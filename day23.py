""" Solution for Day 23 """

from advent import Advent, Runner, file_to_string


class Day23(Advent):
    """ class for Day 23 solution """

    def __init__(self, input_text):
        super().__init__()
        self.name = "23"
        self.lines = input_text

    def parse(self):
        pass

    def part_one(self):
        return None

    def part_two(self):
        return None


def main():
    """ stub for main() """
    aoc1 = Day23(file_to_string("day23-live.txt"))
    runner = Runner(aoc1)
    runner.run()


if __name__ == '__main__':
    main()
