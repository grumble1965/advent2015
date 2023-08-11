""" Run all Advent of Code 2015 daily puzzles with live input """

from advent import Runner, file_to_string
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
from day15 import Day15
from day16 import Day16
from day17 import Day17
from day18 import Day18
from day19 import Day19
from day20 import Day20
from day21 import Day21
from day22 import Day22
from day23 import Day23
from day24 import Day24
from day25 import Day25


def main():
    """ stub for main() """
    Runner(Day01(file_to_string("day01-live.txt"))).run()
    Runner(Day02(file_to_string("day02-live.txt"))).run()
    Runner(Day03(file_to_string("day03-live.txt"))).run()
    Runner(Day04(file_to_string("day04-live.txt"))).run()
    Runner(Day05(file_to_string("day05-live.txt"))).run()
    Runner(Day06(file_to_string("day06-live.txt"))).run()
    Runner(Day07(file_to_string("day07-live.txt"))).run()
    Runner(Day08(file_to_string("day08-live.txt"))).run()
    Runner(Day09(file_to_string("day09-live.txt"))).run()
    Runner(Day10(file_to_string("day10-live.txt"))).run()
    Runner(Day11(file_to_string("day11-live.txt"))).run()
    Runner(Day12(file_to_string("day12-live.txt"))).run()
    Runner(Day13(file_to_string("day13-live.txt"))).run()
    Runner(Day14(file_to_string("day14-live.txt"))).run()
    Runner(Day15(file_to_string("day15-live.txt"))).run()
    Runner(Day16(file_to_string("day16-live.txt"))).run()
    Runner(Day17(file_to_string("day17-live.txt"))).run()
    Runner(Day18(file_to_string("day18-live.txt"))).run()
    Runner(Day19(file_to_string("day19-live.txt"))).run()
    Runner(Day20(file_to_string("day20-live.txt"))).run()
    Runner(Day21(file_to_string("day21-live.txt"))).run()
    Runner(Day22(file_to_string("day22-live.txt"))).run()
    Runner(Day23(file_to_string("day23-live.txt"))).run()
    Runner(Day24(file_to_string("day24-live.txt"))).run()
    Runner(Day25(file_to_string("day25-live.txt"))).run()


if __name__ == '__main__':
    main()
