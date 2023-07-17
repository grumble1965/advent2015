
class Advent:
    def __init__(self):
        self.name = 'Unknown'

    def parse(self):
        raise NotImplementedError

    def partA(self):
        raise NotImplementedError

    def partB(self):
        raise NotImplementedError


class Runner:
    def __init__(self, advent):
        self.advent = advent

    def run(self):
        name = self.advent.name
        print(f"Day {name}")
        self.advent.parse()
        print("Part A: ", end='')
        self.advent.partA()
        print("Part B: ", end='')
        self.advent.partB()


def File_to_String(fname):
    input_lines = []
    with open(fname, "r") as inputfile:
        while True:
            line = inputfile.readline()
            if not line:
                break
            input_lines.append(line.strip())
    return input_lines
