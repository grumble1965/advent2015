from advent import Advent, Runner, File_to_String
import sys


class Day20(Advent):
    def __init__(self, input_text, elves=1000000):
        self.name = "20"
        self.lines = input_text
        self.presents_total = None
        self.houses = {}
        self.elf_limit = elves

    def parse(self):
        for line in self.lines:
            tmp = line.strip()
            # print(f"{tmp}")
            if self.presents_total is None:
                self.presents_total = int(tmp)

    def get_house(self, addr):
        if addr in self.houses:
            return self.houses[addr]
        else:
            return None

    def partA(self, search_limit=None):
        # print("Initialize houses")
        self.houses = {}
        for ee in range(1, self.elf_limit+1):
            self.houses[ee] = 0

        # print("Fill houses")
        for ee in range(1, self.elf_limit+1):
            limit = self.elf_limit + 1
            for hh in range(ee, limit, ee):
                self.houses[hh] += 10 * ee

        # print("Find house")
        if search_limit is not None:
            final_limit = search_limit
        else:
            final_limit = self.presents_total
        found = False
        for elf in range(1, final_limit):
            presents = self.houses[elf]
            if presents >= self.presents_total:
                print(f"House {elf} has {presents} presents")
                return elf
        return None

    def partB(self, search_limit=None):
        # print("Initialize houses")
        self.houses = {}
        for ee in range(1, self.elf_limit+1):
            self.houses[ee] = 0

        # print("Fill houses")
        for ee in range(1, self.elf_limit+1):
            limit = min(self.elf_limit + 1, ee * 50)
            for hh in range(ee, limit, ee):
                self.houses[hh] += 11 * ee

        # print("Find house")
        if search_limit is not None:
            final_limit = search_limit
        else:
            final_limit = self.presents_total
        found = False
        for elf in range(1, final_limit):
            presents = self.houses[elf]
            if presents >= self.presents_total:
                print(f"House {elf} has {presents} presents")
                return elf
        return None


def main():
    aoc1 = Day20(File_to_String("day20-live.txt"))
    runner = Runner(aoc1)
    runner.run()


if __name__ == '__main__':
    main()
