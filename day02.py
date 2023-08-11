from advent import Advent, Runner, file_to_string
import sys


class Day02(Advent):
    def __init__(self, input_text):
        self.name = "2"
        self.lines = input_text

    def parse(self):
        pass

    def part_one(self):
        total_area = 0
        for tmp in self.lines:
            l_str, w_str, h_str = tmp.split('x')
            l, w, h = int(l_str), int(w_str), int(h_str)
            base_area = 2*l*w + 2*w*h + 2*h*l
            slack_area = min([l*w, w*h, h*l])
            box_area = base_area + slack_area
            # print(f"Area for this box = {box_area}")
            total_area += box_area
        print(f"Total Area = {total_area}")
        return total_area

    def part_two(self):
        total_length = 0
        for tmp in self.lines:
            l_str, w_str, h_str = tmp.split('x')
            l, w, h = int(l_str), int(w_str), int(h_str)
            sides = [l, w, h]
            sides.sort()
            short_a, short_b = sides[0], sides[1]
            ribbon_length = 2 * short_a + 2 * short_b
            bow_length = l * w * h
            box_length = ribbon_length + bow_length
            # print(f"Length for this box = {box_length}")
            total_length += box_length
        print(f"Total Length = {total_length}")
        return total_length


def main():
    aoc1 = Day02(file_to_string("day02-live.txt"))
    runner = Runner(aoc1)
    runner.run()


if __name__ == '__main__':
    main()
