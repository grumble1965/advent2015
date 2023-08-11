from advent import Advent, Runner, file_to_string
import re
import sys
import json


class Day12(Advent):
    def __init__(self, input_text):
        self.name = "12"
        self.lines = input_text

    def parse(self):
        pass

    def evalJson(self, j):
        if isinstance(j, str):
            return 0
        elif isinstance(j, int):
            return j
        elif isinstance(j, list):
            return sum([self.evalJson(x) for x in j])
        elif isinstance(j, dict):
            return sum([self.evalJson(x) for x in j.values()])
        else:
            raise TypeError()

    def part_one(self):
        file_sum = 0
        for line in self.lines:
            try:
                file_sum += self.evalJson(json.loads(line))
            except:
                pass
        print(f"File sum = {file_sum}")
        return file_sum

    def evalJson_red(self, j):
        if isinstance(j, str):
            return 0
        elif isinstance(j, int):
            return j
        elif isinstance(j, list):
            return sum([self.evalJson_red(x) for x in j])
        elif isinstance(j, dict):
            if 'red' in j.values():
                return 0
            else:
                return sum([self.evalJson_red(x) for x in j.values()])
        else:
            raise TypeError()

    def part_two(self):
        file_sum = 0
        for line in self.lines:
            try:
                file_sum += self.evalJson_red(json.loads(line))
            except:
                pass
        print(f"File sum = {file_sum}")
        return file_sum


def main():
    aoc1 = Day12(file_to_string("day12-live.txt"))
    runner = Runner(aoc1)
    runner.run()


if __name__ == '__main__':
    main()
