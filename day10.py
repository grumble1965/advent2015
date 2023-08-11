""" Solution for Day 10 """

from itertools import groupby
from advent import Advent, Runner, file_to_string


class Day10(Advent):
    """ class for Day 10 solution """

    def __init__(self, input_text):
        super().__init__()
        self.name = "10"
        self.line = input_text[0]

    def parse(self):
        pass

    def look_and_say(self, word):
        """ create a look and say string from an input word """
        result = ""
        # groupby will split the word into runs of matching chars, returning
        # the char and an iterator for the run
        # making my own state machine for splitting the word was *much* slower
        # using a regex to break up the string proved tricky, but a re.sub() was workable
        # this way was both fast and understandable
        for k, group in groupby(word):
            result += str(len(list(group))) + k
        return result

    def part_one(self):
        line = self.line
        iters = 40
        for i in range(iters):
            _ = i
            new_ll = self.look_and_say(line)
            line = new_ll
        print(f"After {iters} iterations, length = {len(line)}")
        return len(line)

    def part_two(self):
        line = self.line
        iters = 50
        for i in range(iters):
            _ = i
            new_ll = self.look_and_say(line)
            line = new_ll
        print(f"After {iters} iterations, length = {len(line)}")
        return len(line)


def main():
    """ stub for main() """
    aoc1 = Day10(file_to_string("day10-live.txt"))
    runner = Runner(aoc1)
    runner.run()


if __name__ == '__main__':
    main()
