""" Solution for Day 25 """

from advent import Advent, Runner, file_to_string


class Day25(Advent):
    """ class for day 25 solution """

    def __init__(self, input_text):
        super().__init__()
        self.name = "25"
        self.lines = input_text
        self.goal = (None, None)

    def parse(self):
        for line in self.lines:
            tmp = line.strip()
            # print(f"{tmp}")
            words = tmp.replace('.', '').replace(',', '').split()
            r_goal = int(words[words.index('row')+1])
            c_goal = int(words[words.index('column')+1])
            self.goal = (r_goal, c_goal)

    def diagonal_counter(self):
        """ generate the r,c indexes in sequence """
        row, col = 1, 1
        yield row, col
        while True:
            if row == 1:
                row, col = col + 1, 1
            else:
                row, col = row - 1, col + 1
            yield row, col

    def part_one(self):
        # print(f"Goal is at {self.goal}")
        code = 20151125
        for i in self.diagonal_counter():
            if i == self.goal:
                print(i, code)
                break
            code = (code * 252533) % 33554393
        return code

    def part_two(self):
        print("All done!")
        return None


def main():
    """ stub for main() """
    aoc1 = Day25(file_to_string("day25-live.txt"))
    runner = Runner(aoc1)
    runner.run()


if __name__ == '__main__':
    main()
