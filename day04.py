from advent import Advent, Runner, File_to_String
import sys
import hashlib


class Day04(Advent):
    def __init__(self, input_text):
        self.name = "4"
        self.line = input_text[0]

    def parse(self):
        pass

    def hash_loop(self, key, prefix):
        number = 1
        while True:
            target = f"{key}{number}"
            hash_obj = hashlib.md5(bytes(target, 'utf-8'))
            if hash_obj.hexdigest().startswith(prefix):
                break
            number += 1
        return number

    def partA(self):
        key = self.line.strip()
        number = self.hash_loop(key, '00000')
        print(f"For key {key}, the lowest positive integer is {number}")
        return number

    def partB(self):
        key = self.line.strip()
        number = self.hash_loop(key, '000000')
        print(f"For key {key}, the lowest positive integer is {number}")
        return number


def main():
    aoc1 = Day04(File_to_String("day04-live.txt"))
    runner = Runner(aoc1)
    runner.run()


if __name__ == '__main__':
    main()
