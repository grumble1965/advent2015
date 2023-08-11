""" Day 2 Solution """

from advent import Advent, Runner, file_to_string


class Day02(Advent):
    """ Day 2 solution class """

    def __init__(self, input_text):
        super().__init__()
        self.name = "2"
        self.lines = input_text

    def parse(self):
        pass

    def part_one(self):
        total_area = 0
        for tmp in self.lines:
            l_str, w_str, h_str = tmp.split('x')
            length, width, height = int(l_str), int(w_str), int(h_str)
            base_area = 2*length*width + 2*width*height + 2*height*length
            slack_area = min([length*width, width*height, height*length])
            box_area = base_area + slack_area
            # print(f"Area for this box = {box_area}")
            total_area += box_area
        print(f"Total Area = {total_area}")
        return total_area

    def part_two(self):
        total_length = 0
        for tmp in self.lines:
            l_str, w_str, h_str = tmp.split('x')
            length, width, height = int(l_str), int(w_str), int(h_str)
            sides = [length, width, height]
            sides.sort()
            short_a, short_b = sides[0], sides[1]
            ribbon_length = 2 * short_a + 2 * short_b
            bow_length = length * width * height
            box_length = ribbon_length + bow_length
            # print(f"Length for this box = {box_length}")
            total_length += box_length
        print(f"Total Length = {total_length}")
        return total_length


def main():
    """ stub for main() """
    aoc1 = Day02(file_to_string("day02-live.txt"))
    runner = Runner(aoc1)
    runner.run()


if __name__ == '__main__':
    main()
