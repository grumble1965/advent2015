from advent import Advent, Runner, file_to_string
import sys


class Day11(Advent):
    def __init__(self, input_text):
        self.name = "11"
        self.line = input_text[0]
        self.partAResult = None
        self.table = {'a': 'b', 'b': 'c', 'c': 'd', 'd': 'e', 'e': 'f', 'f': 'g', 'g': 'h', 'h': 'j', 'i': 'j', 'j': 'k',
                      'k': 'm', 'l': 'm', 'm': 'n', 'n': 'p', 'o': 'p', 'p': 'q', 'q': 'r', 'r': 's', 's': 't', 't': 'u',
                      'u': 'v', 'v': 'w', 'w': 'x', 'x': 'y', 'y': 'z', 'z': 'a'}
        self.rule1 = ['abc', 'bcd', 'cde', 'def', 'efg', 'fgh', 'ghi', 'hij', 'ijk', 'jkl', 'klm', 'lmn', 'mno', 'nop', 'pqr',
                      'qrs', 'rst', 'stu', 'tuv', 'uvw', 'vwx', 'wxy', 'xyz']
        self.rule3 = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'jj', 'kk', 'mm',
                      'nn', 'pp', 'qq', 'rr', 'ss', 'tt', 'uu', 'vv', 'ww', 'xx', 'yy', 'zz']

    def inc_letter(self, ch):
        new_ch = self.table[ch]
        return (new_ch == 'a'), new_ch

    def increment(self, password):
        carry, index, p = True, 7, list(password)
        while carry and index >= 0:
            carry, p[index] = self.inc_letter(password[index])
            index -= 1

        return "".join(p)

    def valid1(self, password):
        if len([seq for seq in self.rule1 if seq in password]) > 0:
            return True
        else:
            # print("fails rule 1")
            return False

    def valid2(self, password):
        if 'i' not in password and 'o' not in password and 'l' not in password:
            return True
        else:
            # print("fails rule 2")
            return False

    def valid3(self, password):
        if len([pair for pair in self.rule3 if pair in password]) > 1:
            return True
        else:
            # print("fails rule 3")
            return False

    def valid(self, password):
        v1 = self.valid1(password)
        v2 = self.valid2(password)
        v3 = self.valid3(password)
        return len(password) == 8 and v1 and v2 and v3

    def parse(self):
        pass

    def part_one(self):
        passwd = self.increment(self.line)
        # print(f"{tmp} -> {passwd}", end='')
        while not self.valid(passwd):
            # print(" bad")
            foo = self.increment(passwd)
            # print(f"{passwd} -> {foo}", end='')
            passwd = foo

        print(f"From {self.line}, new password is {passwd}")
        self.partAResult = passwd
        return passwd

    def part_two(self):
        passwd = self.increment(self.partAResult)
        # print(f"{tmp} -> {passwd}", end='')
        while not self.valid(passwd):
            # print(" bad")
            foo = self.increment(passwd)
            # print(f"{passwd} -> {foo}", end='')
            passwd = foo

        print(f"From {self.partAResult}, new password is {passwd}")
        return passwd


def main():
    aoc1 = Day11(file_to_string("day11-live.txt"))
    runner = Runner(aoc1)
    runner.run()


if __name__ == '__main__':
    main()
