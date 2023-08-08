""" Day 19 solution """

from advent import Advent, Runner, File_to_String


class PriorityQueue:
    def __init__(self):
        self.items = []

    def append(self, item):
        self.items.append(item)
        self.items.sort(key=lambda tt: len(tt[0]))

    def pop(self):
        return self.items.pop(0)

    def empty(self):
        return len(self.items) == 0

    def length(self):
        return len(self.items)


class Day19(Advent):
    """ The class for Day 19 solution """

    def __init__(self, input_text):
        super().__init__()
        self.name = "19"
        self.lines = input_text
        self.rules = []
        self.start = None

    def parse(self):
        for line in self.lines:
            tmp = line.strip()
            if tmp != '' and tmp.find('=>') == -1:
                self.start = tmp
            elif tmp.find('=>') >= 0:
                words = tmp.split('=>')
                lhs = words[0].strip()
                rhs = words[1].strip()
                self.rules.append((lhs, rhs))

    def partA(self):
        molecules = set()
        for lhs, rhs in self.rules:
            # print(f"rule {lhs} -> {rhs}")
            idx = 0
            while True:
                next_idx = self.start.find(lhs, idx)
                if next_idx == -1:
                    break
                molecules.add(self.start[:next_idx] +
                              rhs +
                              self.start[next_idx+len(lhs):])
                # print(f"{start[:next]} *{rhs}* {start[next+len(lhs):]}")
                idx = next_idx + 1
        print(f"Yields {len(molecules)} unique molecules")
        return len(molecules)

    def partB(self):
        # sort the rules
        self.rules.sort(key=lambda a: len(a[1]) - len(a[0]), reverse=True)

        queue = PriorityQueue()
        queue.append((self.start, 0))

        solutions = []
        seen = set()
        iteration_ctr = 0

        while not queue.empty():
            if iteration_ctr % 100 == 0:
                sum_seen = len(seen)
                # print(f"{iteration_ctr}: Queue = {queue.length()}  Seen = {sum_seen}")
            iteration_ctr += 1

            molecule, steps = queue.pop()
            if molecule == 'e':
                # print(f"solution!  {steps}")
                solutions.append(steps)
                if len(solutions) > 3:
                    break
            else:
                for lhs, rhs in self.rules:
                    occurances = molecule.count(rhs)
                    if lhs == 'e' and rhs == molecule:
                        # print(" last step")
                        queue.append(('e', steps+1))
                    elif lhs != 'e' and occurances > 0:
                        # print(f" {occurances} match")
                        locations = []
                        start_location = 0
                        while len(locations) < occurances:
                            locations.append(
                                molecule.find(rhs, start_location))
                            start_location += len(rhs)
                        for start_location in locations:
                            new_str = molecule[:start_location] + \
                                lhs + molecule[start_location+len(rhs):]
                            # print(f"  At {start_location}, {molecule} -> {new_str}")
                            queue.append((new_str, steps+1))
                    else:
                        # print(" no match")
                        pass

                seen.add(molecule)

        if len(solutions) > 0:
            print(f"Best solution is {min(solutions)} steps")
            return min(solutions)

        print("No solutions found!")
        return None


def main():
    """ stub for main() """
    aoc1 = Day19(File_to_String("day19-live.txt"))
    runner = Runner(aoc1)
    runner.run()


if __name__ == '__main__':
    main()
