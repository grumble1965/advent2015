""" Solution for Day 6 """

import numpy as np
from advent import Advent, Runner, file_to_string


class Day06(Advent):
    """ Class for Day 6 solution """

    def __init__(self, input_text):
        super().__init__()
        self.name = "6"
        self.lines = input_text
        self.commands = []
        self.lights = None

    def parse(self):
        for tmp in self.lines:
            spaces = tmp.count(' ')
            words = tmp.split()
            command, topleft, bottomright = None, None, None
            if spaces == 3:
                # toggle
                command, topleft, bottomright = words[0], words[1], words[3]
                # print(f"{command}, {topleft}, {bottomright}")
            elif spaces == 4:
                # turn on/off
                command, topleft, bottomright = words[1], words[2], words[4]
                # print(f"{command}, {topleft}, {bottomright}")

            tmp = topleft.split(',')
            x_0, y_0 = int(tmp[0]), int(tmp[1])
            tmp = bottomright.split(',')
            x_n, y_n = int(tmp[0]), int(tmp[1])
            self.commands.append((command, x_0, y_0, x_n, y_n))
            # print(f"{command} from ({x_0},{y_0}) to ({x_n},{y_n})")

    def handle_old_command(self, command, x_0, y_0, x_n, y_n):
        """ handle commands the old way """
        d_y = y_n - y_0
        ystep = 1 if d_y > 0 else -1

        d_x = x_n - x_0
        xstep = 1 if d_x > 0 else -1

        if command == 'on':
            self.lights[min([y_0, y_n]):max([y_0, y_n])+ystep:ystep,
                        min([x_0, x_n]):max([x_0, x_n])+xstep:xstep] = \
                np.full((d_y+ystep, d_x+xstep), True, dtype=bool)
        elif command == 'off':
            self.lights[min([y_0, y_n]):max([y_0, y_n])+ystep:ystep,
                        min([x_0, x_n]):max([x_0, x_n])+xstep:xstep] = \
                np.full((d_y+ystep, d_x+xstep), False, dtype=bool)
        elif command == 'toggle':
            subrange = self.lights[min([y_0, y_n]):max([y_0, y_n])+ystep:ystep,
                                   min([x_0, x_n]):max([x_0, x_n])+xstep:xstep].copy()
            self.lights[min([y_0, y_n]):max([y_0, y_n])+ystep:ystep,
                        min([x_0, x_n]):max([x_0, x_n])+xstep:xstep] = np.logical_not(subrange)
        else:
            print(f"Unknown command {command}")

    def handle_new_command(self, command, x_0, y_0, x_n, y_n):
        """ handle commands the new way """
        d_y = y_n - y_0
        ystep = 1 if d_y > 0 else -1

        d_x = x_n - x_0
        xstep = 1 if d_x > 0 else -1

        if command == 'on':
            self.lights[min([y_0, y_n]):max([y_0, y_n])+ystep:ystep,
                        min([x_0, x_n]):max([x_0, x_n])+xstep:xstep] += \
                np.ones((d_y+ystep, d_x+xstep), dtype=self.lights.dtype)
        elif command == 'off':
            self.lights[min([y_0, y_n]):max([y_0, y_n])+ystep:ystep,
                        min([x_0, x_n]):max([x_0, x_n])+xstep:xstep] -= \
                np.ones((d_y+ystep, d_x+xstep), dtype=self.lights.dtype)
            self.lights = np.where(self.lights < 0, 0, self.lights)
        elif command == 'toggle':
            self.lights[min([y_0, y_n]):max([y_0, y_n])+ystep:ystep,
                        min([x_0, x_n]):max([x_0, x_n])+xstep:xstep] += \
                np.full((d_y+ystep, d_x+xstep), 2, dtype=self.lights.dtype)
        else:
            print(f"Unknown command {command}")

    def part_one(self):
        self.lights = np.full((1000, 1000), False, dtype=bool)
        for command in self.commands:
            cmd, x_0, y_0, x_n, y_n = command
            self.handle_old_command(cmd, x_0, y_0, x_n, y_n)
        lights_on = np.count_nonzero(self.lights)
        print(f"Total lights on: {lights_on}")
        return lights_on

    def part_two(self):
        self.lights = np.zeros((1000, 1000), dtype=np.int16)
        for command in self.commands:
            cmd, x_0, y_0, x_n, y_n = command
            self.handle_new_command(cmd, x_0, y_0, x_n, y_n)
        brightness = self.lights.sum()
        print(f"Total brightness: {brightness}")
        return brightness


def main():
    """ stub for main() """
    aoc1 = Day06(file_to_string("day06-live.txt"))
    runner = Runner(aoc1)
    runner.run()


if __name__ == '__main__':
    main()
