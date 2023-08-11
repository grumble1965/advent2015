from advent import Advent, Runner, file_to_string
import sys
import hashlib


class Day07(Advent):
    def __init__(self, input_text):
        self.name = "7"
        self.lines = input_text
        self.rules = []
        self.store = {}
        self.sensitivity = []
        self.outputs = []

    def parse(self):
        for tmp in self.lines:
            lhs, rhs = tmp.split(' -> ')
            lops = lhs.split(' ')

            if len(lops) == 1:
                input = lops[0]
                if not str(input).islower():
                    input = int(input)
                self.rules.append(([input], 'ASSIGN', rhs))
            elif len(lops) == 2:
                self.rules.append(([lops[1]], 'NOT', rhs))
            elif len(lops) == 3:
                if lops[1] in ['AND', 'OR']:
                    self.rules.append(([lops[0], lops[2]], lops[1], rhs))
                elif lops[1] in ['LSHIFT', 'RSHIFT']:
                    self.rules.append(([lops[0], int(lops[2])], lops[1], rhs))
            else:
                print(f"Bad parse {lhs} {rhs}")

    def initialize(self, override=False, value=None):
        self.sensitivity = []
        self.outputs = []
        for rule in self.rules:
            (sens_list, command, output) = rule
            for var in sens_list:
                if str(var).islower() and var not in self.sensitivity:
                    self.sensitivity.append(var)
            if output not in self.outputs:
                self.outputs.append(output)

        for vv in self.outputs:
            self.store[vv] = None

        if override:
            self.store['b'] = value

    def run(self, override=False, value=None):
        while len([var for var in self.store.values() if var is None]) > 0:
            for rule in self.rules:
                (sens_list, command, output) = rule
                arg_list = []
                for vv in sens_list:
                    if str(vv).islower():
                        arg_list.append(self.store[vv])
                    else:
                        arg_list.append(int(vv))
                if None not in arg_list:
                    result = None
                    if command == 'ASSIGN':
                        result = arg_list[0]
                    elif command == 'NOT':
                        result = ~arg_list[0]
                    elif command == 'AND':
                        result = arg_list[0] & arg_list[1]
                    elif command == 'OR':
                        result = arg_list[0] | arg_list[1]
                    elif command == 'LSHIFT':
                        result = arg_list[0] << arg_list[1]
                    elif command == 'RSHIFT':
                        result = arg_list[0] >> arg_list[1]
                    else:
                        print(f"INVALID COMMAND {command}")
                    while result < 0:
                        result += 65536
                    self.store[output] = result
                    if override:
                        self.store['b'] = value

    def part_one(self):
        # init the store and sensistivity lists
        self.initialize()
        # run all of the rules
        self.run()

        if 'a' in self.store:
            print(f"Wire a = {self.store['a']}")
            return self.store['a']
        else:
            return None

    def part_two(self):
        self.initialize()
        self.run()
        override = self.store['a']

        self.initialize(override=True, value=override)
        self.run(override=True, value=override)

        if 'a' in self.store:
            print(f"With wire b overridden, Wire a = {self.store['a']}")
            return self.store['a']
        else:
            return None


def main():
    aoc1 = Day07(file_to_string("day07-live.txt"))
    runner = Runner(aoc1)
    runner.run()


if __name__ == '__main__':
    main()
