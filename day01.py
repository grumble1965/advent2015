from advent import Advent, Runner, File_to_String
import sys


class Day01(Advent):
    def __init__(self, input_text):
        self.name = "1"
        self.line = input_text[0]

    def parse(self):
        pass

    def partA(self):
        ll = self.line
        left_parens, right_parens = ll.count('('), ll.count(')')
        print(f"Ultimate Floor = {left_parens - right_parens}")
        return left_parens - right_parens

    def partB(self):
        ll = self.line
        floor, position = 0, 1
        for c in ll:
            if c == '(':
                floor += 1
            elif c == ')' and floor == 0:
                break
            elif c == ')' and floor > 0:
                floor -= 1
            position += 1
        print(f"Ultimate Position = {position}")
        return position


def main():
    aoc1 = Day01(File_to_String("day01-live.txt"))
    runner = Runner(aoc1)
    runner.run()


if __name__ == '__main__':
    main()