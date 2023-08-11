""" Python code to support Advent of Code problems """


class Advent:
    """ case class for Advent of Code daily solutions """

    def __init__(self):
        self.name = 'Unknown'

    def parse(self):
        """ parse the input data """
        raise NotImplementedError

    def part_one(self):
        """ code for the first part of the daily challenge """
        raise NotImplementedError

    def part_two(self):
        """ code for the second part of the daily challenge """
        raise NotImplementedError


class Runner:
    """ code to run a daily challenge class """

    def __init__(self, advent):
        self.advent = advent

    def run(self):
        """ run a daily challenge: parse, part A, part B """
        name = self.advent.name
        print(f"Day {name}")
        self.advent.parse()
        print("Part 1: ", end='')
        self.advent.part_one()
        print("Part 2: ", end='')
        self.advent.part_two()


def file_to_string(fname):
    """ utility function to read file contents into a string """
    input_lines = []
    with open(fname, mode="r", encoding="utf_8") as inputfile:
        while True:
            line = inputfile.readline()
            if not line:
                break
            input_lines.append(line.strip())
    return input_lines
