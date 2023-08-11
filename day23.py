""" Solution for Day 23 """

from advent import Advent, Runner, file_to_string


class Day23(Advent):
    """ class for Day 23 solution """

    def __init__(self, input_text):
        super().__init__()
        self.name = "23"
        self.lines = input_text
        self.code = []

    def parse(self):
        for line in self.lines:
            tmp = line.strip()
            # print(f"{tmp}")
            tmp = tmp.replace(',', '')
            tmp = tmp.replace('+', '')
            words = tmp.split()
            self.code.append(words)

    def cpu(self, a_start=0, b_start=0):
        """ run the CPU to completion with the provided inputs """
        reg = {'a': a_start, 'b': b_start}
        prog_ctr = 0
        while prog_ctr in range(len(self.code)):
            opc = self.code[prog_ctr][0]
            if opc == 'hlf':
                reg_idx = self.code[prog_ctr][1]
                reg[reg_idx] //= 2
                prog_ctr += 1
            elif opc == 'tpl':
                reg_idx = self.code[prog_ctr][1]
                reg[reg_idx] *= 3
                prog_ctr += 1
            elif opc == 'inc':
                reg_idx = self.code[prog_ctr][1]
                reg[reg_idx] += 1
                prog_ctr += 1
            elif opc == 'jmp':
                off = int(self.code[prog_ctr][1])
                prog_ctr += off
            elif opc == 'jie':
                reg_idx = self.code[prog_ctr][1]
                off = int(self.code[prog_ctr][2])
                if reg[reg_idx] % 2 == 0:
                    prog_ctr += off
                else:
                    prog_ctr += 1
            elif opc == 'jio':
                reg_idx = self.code[prog_ctr][1]
                off = int(self.code[prog_ctr][2])
                if reg[reg_idx] == 1:
                    prog_ctr += off
                else:
                    prog_ctr += 1
            else:
                print(f"Invalid instruction {opc}")
                break
        return prog_ctr, reg

    def part_one(self):
        prog_ctr, reg = self.cpu()
        print(f"Program ended with pc = {prog_ctr} and {reg}")
        return reg

    def part_two(self):
        prog_ctr, reg = self.cpu(a_start=1)
        print(f"Program ended with pc = {prog_ctr} and {reg}")
        return reg


def main():
    """ stub for main() """
    aoc1 = Day23(file_to_string("day23-live.txt"))
    runner = Runner(aoc1)
    runner.run()


if __name__ == '__main__':
    main()
