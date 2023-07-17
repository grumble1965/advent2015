from advent import Advent, Runner, File_to_String
import sys


class Day08(Advent):
    def __init__(self, input_text):
        self.name = "8"
        self.lines = input_text

    def parse(self):
        pass

    def partA(self):
        total_code, total_memory = 0, 0

        for line in self.lines:
            tmp = line.strip()
            this_code, this_memory = len(tmp), None

            # strip leading/trailing "
            string = tmp[1:-1]

            # handle \
            stripped, seen_backslash, idx = '', False, 0
            while idx < len(string):
                ch = string[idx]
                if seen_backslash and ch == '\\':
                    stripped += ch
                    idx += 1
                    seen_backslash = False
                elif seen_backslash and ch == '"':
                    stripped += ch
                    idx += 1
                    seen_backslash = False
                elif seen_backslash and ch == 'x':
                    stripped += 'Z'
                    idx += 3
                    seen_backslash = False
                elif seen_backslash:
                    seen_backslash = False
                    idx += 1
                elif not seen_backslash and ch == '\\':
                    seen_backslash = True
                    idx += 1
                else:
                    stripped += ch
                    idx += 1

            this_memory = len(stripped)
            # print(f" {tmp} = {this_code} {this_memory}")
            total_code += this_code
            total_memory += this_memory

        print(
            f"Total code = {total_code}  Total memory = {total_memory} : difference = {total_code-total_memory}")
        return total_code - total_memory

    def partB(self):
        total_original, total_encoded = 0, 0
        this_original, this_encoded = 0, 0

        for line in self.lines:
            tmp = line.strip()

            original = tmp
            this_original = len(original)

            encoded = ''
            for ch in original:
                if ch == '\\':
                    encoded += '\\'
                    encoded += '\\'
                elif ch == '"':
                    encoded += '\\'
                    encoded += '"'
                else:
                    encoded += ch
            encoded = '"' + encoded + '"'

            this_encoded = len(encoded)
            # print(f"  {this_original} {this_encoded}")
            total_original += this_original
            total_encoded += this_encoded

        print(
            f"Total encoded strings {total_original}   Total original strings {total_encoded} : difference = {total_encoded-total_original}")
        return total_encoded - total_original


def main():
    aoc1 = Day08(File_to_String("day08-live.txt"))
    runner = Runner(aoc1)
    runner.run()


if __name__ == '__main__':
    main()
