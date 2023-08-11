""" Solution for Day 8 """

from advent import Advent, Runner, file_to_string


class Day08(Advent):
    """ class for Day 8 solution """

    def __init__(self, input_text):
        super().__init__()
        self.name = "8"
        self.lines = input_text

    def parse(self):
        pass

    def part_one(self):
        total_code, total_memory = 0, 0

        for line in self.lines:
            tmp = line.strip()
            this_code, this_memory = len(tmp), None

            # strip leading/trailing "
            string = tmp[1:-1]

            # handle \
            stripped, seen_backslash, idx = '', False, 0
            while idx < len(string):
                char = string[idx]
                if seen_backslash and char == '\\':
                    stripped += char
                    idx += 1
                    seen_backslash = False
                elif seen_backslash and char == '"':
                    stripped += char
                    idx += 1
                    seen_backslash = False
                elif seen_backslash and char == 'x':
                    stripped += 'Z'
                    idx += 3
                    seen_backslash = False
                elif seen_backslash:
                    seen_backslash = False
                    idx += 1
                elif not seen_backslash and char == '\\':
                    seen_backslash = True
                    idx += 1
                else:
                    stripped += char
                    idx += 1

            this_memory = len(stripped)
            # print(f" {tmp} = {this_code} {this_memory}")
            total_code += this_code
            total_memory += this_memory

        print(f"Total code = {total_code}  ", end='')
        print(f"Total memory = {total_memory} :", end='')
        print(f"difference = {total_code-total_memory}")
        return total_code - total_memory

    def part_two(self):
        total_original, total_encoded = 0, 0
        this_original, this_encoded = 0, 0

        for line in self.lines:
            tmp = line.strip()

            original = tmp
            this_original = len(original)

            encoded = ''
            for char in original:
                if char == '\\':
                    encoded += '\\'
                    encoded += '\\'
                elif char == '"':
                    encoded += '\\'
                    encoded += '"'
                else:
                    encoded += char
            encoded = '"' + encoded + '"'

            this_encoded = len(encoded)
            # print(f"  {this_original} {this_encoded}")
            total_original += this_original
            total_encoded += this_encoded

        print(f"Total encoded strings {total_original}   ", end='')
        print(f"Total original strings {total_encoded} : ", end='')
        print(f"difference = {total_encoded-total_original}")
        return total_encoded - total_original


def main():
    """ stub for main() """
    aoc1 = Day08(file_to_string("day08-live.txt"))
    runner = Runner(aoc1)
    runner.run()


if __name__ == '__main__':
    main()
