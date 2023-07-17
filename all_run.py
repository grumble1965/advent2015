from advent import *
from day01 import Day01
from day02 import Day02
from day03 import Day03
from day04 import Day04
from day05 import Day05
from day06 import Day06
from day07 import Day07
from day08 import Day08
from day09 import Day09
from day10 import Day10
from day11 import Day11
from day12 import Day12
from day13 import Day13
from day14 import Day14


def main():
    runner = Runner(Day01(File_to_String("day01-live.txt"))).run()
    runner = Runner(Day02(File_to_String("day02-live.txt"))).run()
    runner = Runner(Day03(File_to_String("day03-live.txt"))).run()
    runner = Runner(Day04(File_to_String("day04-live.txt"))).run()
    runner = Runner(Day05(File_to_String("day05-live.txt"))).run()
    runner = Runner(Day06(File_to_String("day06-live.txt"))).run()
    runner = Runner(Day07(File_to_String("day07-live.txt"))).run()
    runner = Runner(Day08(File_to_String("day08-live.txt"))).run()
    runner = Runner(Day09(File_to_String("day09-live.txt"))).run()
    runner = Runner(Day10(File_to_String("day10-live.txt"))).run()
    runner = Runner(Day11(File_to_String("day11-live.txt"))).run()
    runner = Runner(Day12(File_to_String("day12-live.txt"))).run()
    runner = Runner(Day13(File_to_String("day13-live.txt"))).run()
    runner = Runner(Day14(File_to_String("day14-live.txt"))).run()


if __name__ == '__main__':
    main()
