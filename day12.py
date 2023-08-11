""" Solution for Day 12 """

import json
from advent import Advent, Runner, file_to_string


class Day12(Advent):
    """ class for Day 12 solution """

    def __init__(self, input_text):
        super().__init__()
        self.name = "12"
        self.lines = input_text

    def parse(self):
        pass

    def eval_json(self, j):
        """ evaluate a json string """
        if isinstance(j, str):
            return 0
        elif isinstance(j, int):
            return j
        elif isinstance(j, list):
            return sum([self.eval_json(x) for x in j])
        elif isinstance(j, dict):
            return sum([self.eval_json(x) for x in j.values()])
        else:
            raise TypeError()

    def part_one(self):
        file_sum = 0
        for line in self.lines:
            try:
                file_sum += self.eval_json(json.loads(line))
            except json.JSONDecodeError:
                pass
        print(f"File sum = {file_sum}")
        return file_sum

    def eval_json_red(self, j):
        """ evaluate a json string ignoring 'red' """
        if isinstance(j, str):
            return 0
        elif isinstance(j, int):
            return j
        elif isinstance(j, list):
            return sum([self.eval_json_red(x) for x in j])
        elif isinstance(j, dict):
            if 'red' in j.values():
                return 0
            else:
                return sum([self.eval_json_red(x) for x in j.values()])
        else:
            raise TypeError()

    def part_two(self):
        file_sum = 0
        for line in self.lines:
            try:
                file_sum += self.eval_json_red(json.loads(line))
            except TypeError:
                pass
        print(f"File sum = {file_sum}")
        return file_sum


def main():
    """ stub for main() """
    aoc1 = Day12(file_to_string("day12-live.txt"))
    runner = Runner(aoc1)
    runner.run()


if __name__ == '__main__':
    main()
