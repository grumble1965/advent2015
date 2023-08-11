""" Solution for Day 11 """

from advent import Advent, Runner, file_to_string


class Day11(Advent):
    """ class for Day 11 solution """

    def __init__(self, input_text):
        super().__init__()
        self.name = "11"
        self.line = input_text[0]
        self.part_one_result = None
        self.table = {'a': 'b', 'b': 'c', 'c': 'd', 'd': 'e', 'e': 'f', 'f': 'g', 'g': 'h',
                      'h': 'j', 'i': 'j', 'j': 'k', 'k': 'm', 'l': 'm', 'm': 'n', 'n': 'p',
                      'o': 'p', 'p': 'q', 'q': 'r', 'r': 's', 's': 't', 't': 'u', 'u': 'v',
                      'v': 'w', 'w': 'x', 'x': 'y', 'y': 'z', 'z': 'a'}
        self.rule1 = ['abc', 'bcd', 'cde', 'def', 'efg', 'fgh', 'ghi', 'hij', 'ijk', 'jkl',
                      'klm', 'lmn', 'mno', 'nop', 'pqr', 'qrs', 'rst', 'stu', 'tuv', 'uvw',
                      'vwx', 'wxy', 'xyz']
        self.rule3 = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'jj', 'kk', 'mm', 'nn',
                      'pp', 'qq', 'rr', 'ss', 'tt', 'uu', 'vv', 'ww', 'xx', 'yy', 'zz']

    def inc_letter(self, char):
        """ increment a letter in the password, return new character and true if we wrapped """
        new_char = self.table[char]
        return (new_char == 'a'), new_char

    def increment(self, password):
        """ increment a password """
        carry, index, password_chars = True, 7, list(password)
        while carry and index >= 0:
            carry, password_chars[index] = self.inc_letter(password[index])
            index -= 1

        return "".join(password_chars)

    def valid1(self, password):
        """ rule one for password validation """
        if len([seq for seq in self.rule1 if seq in password]) > 0:
            return True
        else:
            # print("fails rule 1")
            return False

    def valid2(self, password):
        """ rule two for password validation """
        if 'i' not in password and 'o' not in password and 'l' not in password:
            return True
        else:
            # print("fails rule 2")
            return False

    def valid3(self, password):
        """ rule three for password validation """
        if len([pair for pair in self.rule3 if pair in password]) > 1:
            return True
        else:
            # print("fails rule 3")
            return False

    def valid(self, password):
        """ overall password validation """
        rule_1 = self.valid1(password)
        rule_2 = self.valid2(password)
        rule_3 = self.valid3(password)
        return len(password) == 8 and rule_1 and rule_2 and rule_3

    def parse(self):
        pass

    def part_one(self):
        passwd = self.increment(self.line)
        # print(f"{tmp} -> {passwd}", end='')
        while not self.valid(passwd):
            # print(" bad")
            temp_password = self.increment(passwd)
            # print(f"{passwd} -> {temp_password}", end='')
            passwd = temp_password

        print(f"From {self.line}, new password is {passwd}")
        self.part_one_result = passwd
        return passwd

    def part_two(self):
        passwd = self.increment(self.part_one_result)
        # print(f"{tmp} -> {passwd}", end='')
        while not self.valid(passwd):
            # print(" bad")
            temp_password = self.increment(passwd)
            # print(f"{passwd} -> {temp_password}", end='')
            passwd = temp_password

        print(f"From {self.part_one_result}, new password is {passwd}")
        return passwd


def main():
    """ stub for main() """
    aoc1 = Day11(file_to_string("day11-live.txt"))
    runner = Runner(aoc1)
    runner.run()


if __name__ == '__main__':
    main()
