from advent import Advent, Runner, File_to_String
import sys


class Day16(Advent):
    def __init__(self, input_text):
        self.name = "16"
        self.lines = input_text

    def parse(self):
        pass

    def partA(self):
        return None

    def partB(self):
        return None


def main():
    aoc1 = Day16(File_to_String("day16-live.txt"))
    runner = Runner(aoc1)
    runner.run()


if __name__ == '__main__':
    main()
