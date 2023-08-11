from advent import Advent, Runner, file_to_string
import numpy as np
import sys


class Day06(Advent):
    def __init__(self, input_text):
        self.name = "6"
        self.lines = input_text
        self.commands = []

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

    def handle_old_command(self, command, x0, y0, xn, yn):
        dy = yn - y0
        ystep = 1 if dy > 0 else -1

        dx = xn - x0
        xstep = 1 if dx > 0 else -1

        if command == 'on':
            self.lights[min([y0, yn]):max([y0, yn])+ystep:ystep,
                        min([x0, xn]):max([x0, xn])+xstep:xstep] = np.full((dy+ystep, dx+xstep), True, dtype=bool)
        elif command == 'off':
            self.lights[min([y0, yn]):max([y0, yn])+ystep:ystep,
                        min([x0, xn]):max([x0, xn])+xstep:xstep] = np.full((dy+ystep, dx+xstep), False, dtype=bool)
        elif command == 'toggle':
            cc = self.lights[min([y0, yn]):max([y0, yn])+ystep:ystep,
                             min([x0, xn]):max([x0, xn])+xstep:xstep].copy()
            self.lights[min([y0, yn]):max([y0, yn])+ystep:ystep,
                        min([x0, xn]):max([x0, xn])+xstep:xstep] = np.logical_not(cc)
        else:
            print(f"Unknown command {command}")

    def handle_new_command(self, command, x0, y0, xn, yn):
        dy = yn - y0
        ystep = 1 if dy > 0 else -1

        dx = xn - x0
        xstep = 1 if dx > 0 else -1

        if command == 'on':
            self.lights[min([y0, yn]):max([y0, yn])+ystep:ystep,
                        min([x0, xn]):max([x0, xn])+xstep:xstep] += np.ones((dy+ystep, dx+xstep), dtype=self.lights.dtype)
        elif command == 'off':
            self.lights[min([y0, yn]):max([y0, yn])+ystep:ystep,
                        min([x0, xn]):max([x0, xn])+xstep:xstep] -= np.ones((dy+ystep, dx+xstep), dtype=self.lights.dtype)
            self.lights = np.where(self.lights < 0, 0, self.lights)
        elif command == 'toggle':
            self.lights[min([y0, yn]):max([y0, yn])+ystep:ystep,
                        min([x0, xn]):max([x0, xn])+xstep:xstep] += np.full((dy+ystep, dx+xstep), 2, dtype=self.lights.dtype)
        else:
            print(f"Unknown command {command}")

    def part_one(self):
        self.lights = np.full((1000, 1000), False, dtype=bool)
        for c in self.commands:
            cmd, x0, y0, xn, yn = c
            self.handle_old_command(cmd, x0, y0, xn, yn)
        on = np.count_nonzero(self.lights)
        print(f"Total lights on: {on}")
        return on

    def part_two(self):
        self.lights = np.zeros((1000, 1000), dtype=np.int16)
        for c in self.commands:
            cmd, x0, y0, xn, yn = c
            self.handle_new_command(cmd, x0, y0, xn, yn)
        brightness = self.lights.sum()
        print(f"Total brightness: {brightness}")
        return brightness


def main():
    aoc1 = Day06(file_to_string("day06-live.txt"))
    runner = Runner(aoc1)
    runner.run()


if __name__ == '__main__':
    main()
