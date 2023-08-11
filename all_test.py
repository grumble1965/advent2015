""" Code to unit test Advent of Code 2015 solutions """

import unittest
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
# from day16 import Day16  - no unit tests for Day 16 :(
from day17 import Day17
from day18 import Day18
from day19 import Day19
from day20 import Day20
from day21 import Day21
from day22 import Day22
from day22 import EasyGame
# from day22 import HardGame - no unit tests using the HardGame
from day23 import Day23
from day24 import Day24
from day25 import Day25


class Day01Tests(unittest.TestCase):
    """ day 1 tests """

    def test_part_one(self):
        """ part one """
        cases = [(['(())'],     0),
                 (['()()'],     0),
                 (['((('],      3),
                 (['(()(()('],  3),
                 (['))((((('],  3),
                 (['())'],     -1),
                 (['))('],     -1),
                 ([')))'],     -3),
                 ([')())())'], -3)
                 ]
        for test_input, test_result in cases:
            with self.subTest():
                day = Day01(test_input)
                day.parse()
                self.assertEqual(test_result, day.part_one())

    def test_part_two(self):
        """ part two """
        cases = [([')'],     1),
                 (['()())'], 5)
                 ]
        for test_input, test_result in cases:
            with self.subTest():
                day = Day01(test_input)
                day.parse()
                self.assertEqual(test_result, day.part_two())


class Day02Tests(unittest.TestCase):
    """ day 2 tests """

    def test_part_one(self):
        """ part one """
        cases = [(['2x3x4'],    58),
                 (['1x1x10'],   43)
                 ]
        for test_input, test_result in cases:
            with self.subTest():
                day = Day02(test_input)
                day.parse()
                self.assertEqual(test_result, day.part_one())

    def test_part_two(self):
        """ part two """
        cases = [(['2x3x4'],    34),
                 (['1x1x10'],   14)
                 ]
        for test_input, test_result in cases:
            with self.subTest():
                day = Day02(test_input)
                day.parse()
                self.assertEqual(test_result, day.part_two())


class Day03Tests(unittest.TestCase):
    """ day 3 tests """

    def test_part_one(self):
        """ part one """
        cases = [(['>'],          2),
                 (['^>v<'],       4),
                 (['^v^v^v^v^v'], 2)
                 ]
        for test_input, test_result in cases:
            with self.subTest():
                day = Day03(test_input)
                day.parse()
                self.assertEqual(test_result, day.part_one())

    def test_part_two(self):
        """ part two """
        cases = [(['^v'], 3),
                 (['^>v<'], 3),
                 (['^v^v^v^v^v'], 11)
                 ]
        for test_input, test_result in cases:
            with self.subTest():
                day = Day03(test_input)
                day.parse()
                self.assertEqual(test_result, day.part_two())


class Day04Tests(unittest.TestCase):
    """ day 4 tests """

    def test_part_one_a(self):
        """ part one a """
        day = Day04(['abcdef'])
        day.parse()
        self.assertEqual(609043, day.part_one())

    def test_part_one_b(self):
        """ part one b """
        day = Day04(['pqrstuv'])
        day.parse()
        self.assertEqual(1048970, day.part_one())


class Day05Tests(unittest.TestCase):
    """ day 5 tests """

    def test_part_one(self):
        """ part one """
        day = Day05([''])
        self.assertEqual(True, day.check_nice_oldway('ugknbfddgicrmopn'))
        self.assertEqual(True, day.check_nice_oldway('aaa'))
        self.assertEqual(False, day.check_nice_oldway('jchzalrnumimnmhp'))
        self.assertEqual(False, day.check_nice_oldway('haegwjzuvuyypxyu'))
        self.assertEqual(False, day.check_nice_oldway('dvszwmarrgswjxmb'))

    def test_part_two(self):
        """ part two """
        day = Day05([''])
        self.assertEqual(True, day.check_nice_newway('qjhvhtzxzqqjkmpb'))
        self.assertEqual(True, day.check_nice_newway('xxyxx'))
        self.assertEqual(False, day.check_nice_newway('uurcxstgmygtbstg'))
        self.assertEqual(False, day.check_nice_newway('ieodomkazucvgmuy'))


class Day06Tests(unittest.TestCase):
    """ day 6 tests """

    def test_part_one(self):
        """ part one """
        day = Day06(['turn on 0,0 through 1,1',
                     'toggle 0,0 through 999,999'])
        day.parse()
        self.assertEqual(999996, day.part_one())

    def test_part_two(self):
        """ part two """
        day = Day06(['turn on 0,0 through 1,1',
                     'toggle 0,0 through 999,999'])
        day.parse()
        self.assertEqual(2000004, day.part_two())


class Day07Tests(unittest.TestCase):
    """ day 7 tests """

    def test_part_one(self):
        """ part one """
        day = Day07(['123 -> x',
                     '456 -> y',
                     'x AND y -> d',
                     'x OR y -> e',
                     'x LSHIFT 2 -> f',
                     'y RSHIFT 2 -> g',
                     'NOT x -> h',
                     'NOT y -> i'])
        day.parse()
        day.part_one()
        self.assertEqual(72, day.store['d'])
        self.assertEqual(507, day.store['e'])
        self.assertEqual(492, day.store['f'])
        self.assertEqual(114, day.store['g'])
        self.assertEqual(65412, day.store['h'])
        self.assertEqual(65079, day.store['i'])
        self.assertEqual(123, day.store['x'])
        self.assertEqual(456, day.store['y'])


class Day08Tests(unittest.TestCase):
    """ day 8 tests """

    def test_part_one(self):
        """ part one """
        day = Day08(['""',
                     '"abc"',
                     '"aaa\\"aaa"',
                     '"\\x27"'])
        day.parse()
        self.assertEqual(12, day.part_one())

    def test_part_two(self):
        """ part two """
        day = Day08(['""',
                     '"abc"',
                     '"aaa\\"aaa"',
                     '"\\x27"'])
        day.parse()
        self.assertEqual(19, day.part_two())


class Day09Tests(unittest.TestCase):
    """ day 9 tests """

    def test_part_one(self):
        """ part one """
        day = Day09(['London to Dublin = 464',
                     'London to Belfast = 518',
                     'Dublin to Belfast = 141'])
        day.parse()
        self.assertEqual(605, day.part_one())

    def test_part_two(self):
        """ part two """
        day = Day09(['London to Dublin = 464',
                     'London to Belfast = 518',
                     'Dublin to Belfast = 141'])
        day.parse()
        self.assertEqual(982, day.part_two())


class Day10Tests(unittest.TestCase):
    """ day 10 tests """

    def test_part_one(self):
        """ part one """
        cases = [(['1'], '11'),
                 (['11'], '21'),
                 (['21'], '1211'),
                 (['1211'], '111221'),
                 (['111221'], '312211'),
                 ]
        for test_input, test_result in cases:
            with self.subTest():
                day = Day10(test_input)
                self.assertEqual(test_result, day.look_and_say(test_input[0]))


class Day11Tests(unittest.TestCase):
    """ day 11 tests """

    def test_increment(self):
        """ increment a string """
        day = Day11(['abcdefgh'])
        day.parse()
        self.assertEqual('abcdefgj', day.increment('abcdefgh'))
        self.assertEqual('ghijklmp', day.increment('ghijklmn'))

    def test_valid(self):
        ''' 
            Check if a string is valid 
            hijklmmn
            abbceffg
            abbcegjk
        '''
        day = Day11(['abcdefgh'])
        day.parse()
        self.assertEqual(True, day.valid1('hijklmmn'))
        self.assertEqual(False, day.valid2('hijklmmn'))

        self.assertEqual(True, day.valid3('abbceffg'))
        self.assertEqual(False, day.valid1('abbceffg'))

        self.assertEqual(False, day.valid3('abbcegjk'))

    def test_next_valid(self):
        """ find the next valid string """
        day = Day11(['abcdefgh'])
        day.parse()
        self.assertEqual('abcdffaa', day.part_one())

        day = Day11(['ghijklmn'])
        day.parse()
        self.assertEqual('ghjaabcc', day.part_one())


class Day12Tests(unittest.TestCase):
    """ day 12 tests """

    def test_part_one(self):
        """ part one """
        cases = [
            (['[1,2,3]'], 6),
            (['{"a":2,"b":4}'], 6),
            (['[[[3]]]', 3]),
            (['{"a":{"b":4},"c":-1}'], 3),
            (['{"a":[-1,1]}'], 0),
            (['[-1,{"a":1}]'], 0),
            (['[]'], 0),
            (['{}'], 0)
        ]
        for test_input, test_result in cases:
            with self.subTest():
                day = Day12(test_input)
                self.assertEqual(test_result, day.part_one())

    def test_part_two(self):
        """ part two """
        cases = [
            (['[1,2,3]'], 6),
            (['[1,{"c":"red","b":2},3]'], 4),
            (['{"d":"red","e":[1,2,3,4],"f":5}'], 0),
            (['[1,"red",5]'], 6),
        ]
        for test_input, test_result in cases:
            with self.subTest():
                day = Day12(test_input)
                self.assertEqual(test_result, day.part_two())


class Day13Tests(unittest.TestCase):
    """ day 13 tests """

    def test_part_one(self):
        """ part one """
        test_input = ["Alice would gain 54 happiness units by sitting next to Bob.",
                      "Alice would lose 79 happiness units by sitting next to Carol.",
                      "Alice would lose 2 happiness units by sitting next to David.",
                      "Bob would gain 83 happiness units by sitting next to Alice.",
                      "Bob would lose 7 happiness units by sitting next to Carol.",
                      "Bob would lose 63 happiness units by sitting next to David.",
                      "Carol would lose 62 happiness units by sitting next to Alice.",
                      "Carol would gain 60 happiness units by sitting next to Bob.",
                      "Carol would gain 55 happiness units by sitting next to David.",
                      "David would gain 46 happiness units by sitting next to Alice.",
                      "David would lose 7 happiness units by sitting next to Bob.",
                      "David would gain 41 happiness units by sitting next to Carol."]
        day = Day13(test_input)
        day.parse()
        self.assertEqual(330, day.part_one())


class Day14Tests(unittest.TestCase):
    """ day 14 tests """

    def test_part_one(self):
        """ part one """
        test_input = ['Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.',
                      'Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.']
        day = Day14(test_input)
        day.parse()
        self.assertEqual(1120, day.run_race_old(1000))

    def test_part_two(self):
        """ part two """
        test_input = ['Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.',
                      'Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.']
        day = Day14(test_input)
        day.parse()
        self.assertEqual(689, day.run_race_new(1000))


class Day15Tests(unittest.TestCase):
    """ day 15 tests """

    def test_part_one(self):
        """ part one """
        day = Day15(['Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8',
                     'Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3'])
        day.parse()
        self.assertEqual(62842880, day.part_one())

    def test_part_two(self):
        """ part two """
        day = Day15(['Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8',
                     'Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3'])
        day.parse()
        self.assertEqual(57600000, day.part_two())


class Day16Tests(unittest.TestCase):
    """ day 16 tests - not defined """


class Day17Tests(unittest.TestCase):
    """ day 17 tests """

    def test_part_one(self):
        """ part one """
        day = Day17(['20', '15', '10', '5', '5'])
        day.parse()
        self.assertEqual(4, day.part_one(total_eggnog=25))

    def test_part_two(self):
        """ part two """
        day = Day17(['20', '15', '10', '5', '5'])
        day.parse()
        self.assertEqual(3, day.part_two(total_eggnog=25))


class Day18Tests(unittest.TestCase):
    """ day 18 tests """

    def test_part_one(self):
        """ part one """
        day = Day18(['.#.#.#\n',
                     '...##.\n',
                     '#....#\n',
                     '..#...\n',
                     '#.#..#\n',
                     '####..\n'])
        day.parse()
        self.assertEqual(4, day.part_one(limit=4, output=True))

    def test_part_two(self):
        """ part two """
        day = Day18(['##.#.#\n',
                     '...##.\n',
                     '#....#\n',
                     '..#...\n',
                     '#.#..#\n',
                     '####.#\n'])
        day.parse()
        self.assertEqual(17, day.part_two(limit=5, output=True))


class Day19Tests(unittest.TestCase):
    """ day 19 tests """

    def test_part_one_a(self):
        """ part one a """
        day = Day19(['e => H\n',
                     'e => O\n',
                     'H => HO\n',
                     'H => OH\n',
                     'O => HH\n',
                     '\n',
                     'HOH\n'])
        day.parse()
        self.assertEqual(4, day.part_one())

    def test_part_one_b(self):
        """ part one b """
        day = Day19(['e => H\n',
                     'e => O\n',
                     'H => HO\n',
                     'H => OH\n',
                     'O => HH\n',
                     '\n',
                     'HOHOHO\n'])
        day.parse()
        self.assertEqual(7, day.part_one())

    def test_part_two_a(self):
        """ part two a """
        day = Day19(['e => H\n',
                     'e => O\n',
                     'H => HO\n',
                     'H => OH\n',
                     'O => HH\n',
                     '\n',
                     'HOH\n'])
        day.parse()
        self.assertEqual(3, day.part_two())

    def test_part_two_b(self):
        """ part two b """
        day = Day19(['e => H\n',
                     'e => O\n',
                     'H => HO\n',
                     'H => OH\n',
                     'O => HH\n',
                     '\n',
                     'HOHOHO\n'])
        day.parse()
        self.assertEqual(6, day.part_two())


class Day20Tests(unittest.TestCase):
    """ day 20 tests """

    def test_part_one(self):
        """ part one """
        # search for a house with at least 500 presents, 15 elves to deliver
        day = Day20(['500'], 15)
        day.parse()
        day.part_one(search_limit=15)
        self.assertEqual(10, day.get_house(1))
        self.assertEqual(30, day.get_house(2))
        self.assertEqual(40, day.get_house(3))
        self.assertEqual(70, day.get_house(4))
        self.assertEqual(60, day.get_house(5))
        self.assertEqual(120, day.get_house(6))
        self.assertEqual(80, day.get_house(7))
        self.assertEqual(150, day.get_house(8))
        self.assertEqual(130, day.get_house(9))

    def test_part_two(self):
        """ part two """
        # search for a house with at least 500 presents, 60 elves to deliver
        day = Day20(['500'], 60)
        day.parse()
        day.part_two()
        self.assertEqual(11, day.get_house(1))
        self.assertEqual(33, day.get_house(2))
        self.assertEqual(53*11, day.get_house(53))


class Day21Tests(unittest.TestCase):
    """ day 21 tests """

    def test_part_one_a(self):
        """ part one a """
        day = Day21(['Hit Points: 12\n',
                     'Damage: 7\n',
                     'Armor: 2\n'])
        day.parse()
        self.assertEqual(12, day.boss_hp)
        self.assertEqual(7, day.boss_damage)
        self.assertEqual(2, day.boss_armor)

    def test_part_one_b(self):
        """ part one b """
        day = Day21(['Hit Points: 12\n',
                     'Damage: 7\n',
                     'Armor: 2\n'])
        day.parse()
        player = (8, 5, 5)
        boss = (12, 7, 2)
        self.assertEqual("player", day.battle(player, boss))


class Day22Tests(unittest.TestCase):
    """ day 22 tests """

    def test_part_one_a(self):
        """ part one a """
        day = Day22(['Hit Points: 14\n',
                     'Damage: 8\n'])
        day.parse()
        game = EasyGame(10, 250, 13, 8)
        for spell in ["Poison", "Magic Missile"]:
            game.player_turn(spell)
            game.boss_turn()
        self.assertEqual("Player", game.winner())

    def test_part_one_b(self):
        """ part one b """
        day = Day22(['Hit Points: 14\n',
                     'Damage: 8\n'])
        day.parse()
        game = EasyGame(10, 250, 14, 8)
        for spell in ["Recharge", "Shield", "Drain", "Poison", "Magic Missile"]:
            game.player_turn(spell)
            game.boss_turn()
        self.assertEqual("Player", game.winner())


class Day23Tests(unittest.TestCase):
    """ day 23 tests """

    def test_part_one(self):
        """ part one """
        day = Day23(['inc a\n',
                     'jio a, +2\n',
                     'tpl a\n',
                     'inc a\n'])
        day.parse()
        regs = day.part_one()
        self.assertEqual(2, regs['a'])


class Day24Tests(unittest.TestCase):
    """ day 24 tests """

    def test_part_one(self):
        """ part one """
        day = Day24(['1\n', '2\n', '3\n', '4\n', '5\n',
                     '7\n', '8\n', '9\n', '10\n', '11\n'])
        day.parse()
        self.assertEqual(99, day.part_one())

    def test_part_two(self):
        """ part two """
        day = Day24(['1\n', '2\n', '3\n', '4\n', '5\n',
                     '7\n', '8\n', '9\n', '10\n', '11\n'])
        day.parse()
        self.assertEqual(44, day.part_two())


class Day25Tests(unittest.TestCase):
    """ day 25 tests """

    def test_part_one(self):
        """ part one """
        _ = Day25(['turn on 0,0 through 1,1',
                   'toggle 0,0 through 999,999'])
        # d.parse()
        # self.assertEqual(999996, d.part_one())
        self.fail("not implemented")

    def test_part_two(self):
        """ part two """
        # d = Day25(['turn on 0,0 through 1,1',
        #            'toggle 0,0 through 999,999'])
        # d.parse()
        # self.assertEqual(2000004, d.part_two())
        self.fail("not implemented")


if __name__ == '__main__':
    unittest.main()
