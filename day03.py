""" Day 3 Solution """

from advent import Advent, Runner, file_to_string


class Day03(Advent):
    """ class for day 3 solution """

    def __init__(self, input_text):
        super().__init__()
        self.name = "3"
        self.line = input_text[0]

    def parse(self):
        pass

    def calc_new_location(self, x_old, y_old, direction):
        """ given a direction, calculate new x,y position """
        x_new, y_new = 0, 0
        if direction == '^':
            x_new, y_new = x_old, y_old+1
        elif direction == 'v':
            x_new, y_new = x_old, y_old-1
        elif direction == '<':
            x_new, y_new = x_old-1, y_old+0
        elif direction == '>':
            x_new, y_new = x_old+1, y_old+0
        else:
            print(f"Unknown direction {direction}")
        return (x_new, y_new)

    def part_one(self):
        houses = {}
        x_loc, y_loc = 0, 0
        houses[(x_loc, y_loc)] = 1
        for char in self.line:
            location = self.calc_new_location(x_loc, y_loc, char)
            x_loc, y_loc = location
            if location in houses:
                houses[location] += 1
            else:
                houses[location] = 1

        visits = len(houses.keys())
        print(f"Houses receiving a present = {visits}")
        return visits

    def part_two(self):
        houses = {}
        x_loc, y_loc = [0, 0], [0, 0]
        houses[(0, 0)] = 2
        turn = 0
        houses[(x_loc[turn], y_loc[turn])] = 1
        for char in self.line:
            location = self.calc_new_location(x_loc[turn], y_loc[turn], char)
            x_loc[turn], y_loc[turn] = location
            if location in houses:
                houses[location] += 1
            else:
                houses[location] = 1

            turn += 1
            if turn == 2:
                turn = 0

        visits = len(houses.keys())
        print(f"Houses receiving a present = {visits}")
        return visits


def main():
    """ stub for main() """
    aoc1 = Day03(file_to_string("day03-live.txt"))
    runner = Runner(aoc1)
    runner.run()


if __name__ == '__main__':
    main()
