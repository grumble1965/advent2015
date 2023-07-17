from advent import Advent, Runner, File_to_String
from itertools import groupby
import sys


class Day10(Advent):
    def __init__(self, input_text):
        self.name = "10"
        self.line = input_text[0]

    def parse(self):
        pass

    def lookAndSay(self, word):
        result = ""
        # groupby will split the word into runs of matching chars, returning the char and an iterator for the run
        # making my own state machine for splitting the word was *much* slower
        # using a regex to break up the string proved tricky, but a re.sub() was workable
        # this way was both fast and understandable
        for k, g in groupby(word):
            result += str(len(list(g))) + k
        return result

    def partA(self):
        ll = self.line
        iters = 40
        for i in range(iters):
            new_ll = self.lookAndSay(ll)
            ll = new_ll
        print(f"After {iters} iterations, length = {len(ll)}")
        return len(ll)

    def partB(self):
        ll = self.line
        iters = 50
        for i in range(iters):
            new_ll = self.lookAndSay(ll)
            ll = new_ll
        print(f"After {iters} iterations, length = {len(ll)}")
        return len(ll)


def main():
    aoc1 = Day10(File_to_String("day10-live.txt"))
    runner = Runner(aoc1)
    runner.run()


if __name__ == '__main__':
    main()
