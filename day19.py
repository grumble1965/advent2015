from advent import Advent, Runner, File_to_String
from collections import deque
import sys


class Day19(Advent):
    def __init__(self, input_text):
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
                tt = (lhs, rhs)
                self.rules.append(tt)

    def partA(self):
        molecules = set()
        for lhs, rhs in self.rules:
            # print(f"rule {lhs} -> {rhs}")
            idx = 0
            while True:
                next = self.start.find(lhs, idx)
                if next == -1:
                    break
                molecules.add(self.start[:next] +
                              rhs +
                              self.start[next+len(lhs):])
                # print(f"{start[:next]} *{rhs}* {start[next+len(lhs):]}")
                idx = next+1
        print(f"Yields {len(molecules)} unique molecules")
        return len(molecules)

    def partB(self):
        q = deque()
        q.append((self.start, 0))

        solutions = []
        seen = {}
        for ll in range(len(self.start) * 2):
            seen[ll] = set()
        iteration_ctr = 0

        while q:
            if iteration_ctr % 10000 == 0:
                sum_seen = sum([len(seen[ll]) for ll in seen])
                # print(f"{iteration_ctr}: Queue = {len(q)}  Seen = {sum_seen}")
            iteration_ctr += 1

            seed, steps = q.pop()
            if seed == 'e':
                # print(f"solution!  {steps}")
                solutions.append(steps)
                if len(solutions) > 3:
                    break
            else:
                next_steps = set()
                for lhs, rhs in self.rules:
                    new_str, d_steps = seed, 0
                    while rhs in new_str:
                        new_str = new_str.replace(rhs, lhs, 1)
                        d_steps += 1
                    if new_str not in seen[len(new_str)]:
                        next_steps.add((new_str, steps+d_steps))

                for ns, st in next_steps:
                    tt = (ns, st)
                    q.append(tt)

                seen[len(seed)].add(seed)

        print(f"Best solution:  {min(solutions)}")
        return min(solutions)


def main():
    aoc1 = Day19(File_to_String("day19-live.txt"))
    runner = Runner(aoc1)
    runner.run()


if __name__ == '__main__':
    main()
