""" Solution for Day 5 """

from advent import Advent, Runner, file_to_string


class Day05(Advent):
    """ Class for Day 5 solution """

    def __init__(self, input_text):
        super().__init__()
        self.name = "5"
        self.lines = input_text

    def parse(self):
        pass

    def check_nice_oldway(self, tmp):
        """ Check if a name is nice the old fashioned way """
        count_vowels = tmp.count('a') + tmp.count('e') + \
            tmp.count('i') + tmp.count('o') + tmp.count('u')
        count_dupes = len([i for i in range(len(tmp)-1) if tmp[i] == tmp[i+1]])
        count_bad = tmp.count('ab') + tmp.count('cd') + \
            tmp.count('pq') + tmp.count('xy')

        return count_vowels >= 3 and count_dupes > 0 and count_bad == 0

    def check_nice_newway(self, tmp):
        """ Check if a name is nice the new fashioned way """
        rule1 = False
        for i in range(len(tmp)-1):
            pair, rest = tmp[i:i+2], tmp[i+2:]
            if rest.count(pair) > 0:
                rule1 = True
                break

        rule2 = False
        for i in range(len(tmp)-2):
            ch1, _, ch2 = tmp[i], tmp[i+1], tmp[i+2]
            if ch1 == ch2:
                rule2 = True
                break

        return rule1 and rule2

    def part_one(self):
        nice = 0
        for tmp in self.lines:
            if self.check_nice_oldway(tmp):
                nice += 1

        print(f"Nice strings under old rules = {nice}")
        return nice

    def part_two(self):
        nice = 0
        for tmp in self.lines:
            if self.check_nice_newway(tmp):
                nice += 1

        print(f"Nice strings under new rules = {nice}")
        return nice


def main():
    """ stub for main() """
    aoc1 = Day05(file_to_string("day05-live.txt"))
    runner = Runner(aoc1)
    runner.run()


if __name__ == '__main__':
    main()
