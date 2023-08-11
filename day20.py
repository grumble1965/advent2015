""" Solution for Day 20 """

from advent import Advent, Runner, file_to_string


class Day20(Advent):
    """ class for Day 20 solution """

    def __init__(self, input_text, elves=1000000):
        super().__init__()
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
        """ get the number of presents at a house """
        if addr in self.houses:
            return self.houses[addr]
        else:
            return None

    def part_one(self, search_limit=None):
        # print("Initialize houses")
        self.houses = {}
        for addr in range(1, self.elf_limit+1):
            self.houses[addr] = 0

        # print("Fill houses")
        for addr in range(1, self.elf_limit+1):
            limit = self.elf_limit + 1
            for next_addr in range(addr, limit, addr):
                self.houses[next_addr] += 10 * addr

        # print("Find house")
        if search_limit is not None:
            final_limit = search_limit
        else:
            final_limit = self.presents_total
        for elf in range(1, final_limit):
            presents = self.houses[elf]
            if presents >= self.presents_total:
                print(f"House {elf} has {presents} presents")
                return elf
        return None

    def part_two(self, search_limit=None):
        # print("Initialize houses")
        self.houses = {}
        for addr in range(1, self.elf_limit+1):
            self.houses[addr] = 0

        # print("Fill houses")
        for addr in range(1, self.elf_limit+1):
            limit = min(self.elf_limit + 1, addr * 50)
            for next_addr in range(addr, limit, addr):
                self.houses[next_addr] += 11 * addr

        # print("Find house")
        if search_limit is not None:
            final_limit = search_limit
        else:
            final_limit = self.presents_total
        for elf in range(1, final_limit):
            presents = self.houses[elf]
            if presents >= self.presents_total:
                print(f"House {elf} has {presents} presents")
                return elf
        return None


def main():
    """ stub for main() """
    aoc1 = Day20(file_to_string("day20-live.txt"))
    runner = Runner(aoc1)
    runner.run()


if __name__ == '__main__':
    main()
