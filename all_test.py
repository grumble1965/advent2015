from unittest import TestCase
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


class Test_Day01(TestCase):
    def test_partOne(self):
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
        for testInput, testResult in cases:
            with self.subTest():
                d = Day01(testInput)
                d.parse()
                self.assertEqual(testResult, d.partA())

    def test_partTwo(self):
        cases = [([')'],     1),
                 (['()())'], 5)
                 ]
        for testInput, testResult in cases:
            with self.subTest():
                d = Day01(testInput)
                d.parse()
                self.assertEqual(testResult, d.partB())


class Test_Day02(TestCase):
    def test_partOne(self):
        cases = [(['2x3x4'],    58),
                 (['1x1x10'],   43)
                 ]
        for testInput, testResult in cases:
            with self.subTest():
                d = Day02(testInput)
                d.parse()
                self.assertEqual(testResult, d.partA())

    def test_partTwo(self):
        cases = [(['2x3x4'],    34),
                 (['1x1x10'],   14)
                 ]
        for testInput, testResult in cases:
            with self.subTest():
                d = Day02(testInput)
                d.parse()
                self.assertEqual(testResult, d.partB())


class Test_Day03(TestCase):
    def test_partOne(self):
        cases = [(['>'],          2),
                 (['^>v<'],       4),
                 (['^v^v^v^v^v'], 2)
                 ]
        for testInput, testResult in cases:
            with self.subTest():
                d = Day03(testInput)
                d.parse()
                self.assertEqual(testResult, d.partA())

    def test_partTwo(self):
        cases = [(['^v'], 3),
                 (['^>v<'], 3),
                 (['^v^v^v^v^v'], 11)
                 ]
        for testInput, testResult in cases:
            with self.subTest():
                d = Day03(testInput)
                d.parse()
                self.assertEqual(testResult, d.partB())


class Test_Day04(TestCase):
    def test_partOne1(self):
        d = Day04(['abcdef'])
        d.parse()
        self.assertEqual(609043, d.partA())

    def test_partOne2(self):
        d = Day04(['pqrstuv'])
        d.parse()
        self.assertEqual(1048970, d.partA())


class Test_Day05(TestCase):
    def test_partOne1(self):
        d = Day05([''])
        self.assertEqual(True, d.check_nice_oldway('ugknbfddgicrmopn'))
        self.assertEqual(True, d.check_nice_oldway('aaa'))
        self.assertEqual(False, d.check_nice_oldway('jchzalrnumimnmhp'))
        self.assertEqual(False, d.check_nice_oldway('haegwjzuvuyypxyu'))
        self.assertEqual(False, d.check_nice_oldway('dvszwmarrgswjxmb'))

    def test_partTwo(self):
        d = Day05([''])
        self.assertEqual(True, d.check_nice_newway('qjhvhtzxzqqjkmpb'))
        self.assertEqual(True, d.check_nice_newway('xxyxx'))
        self.assertEqual(False, d.check_nice_newway('uurcxstgmygtbstg'))
        self.assertEqual(False, d.check_nice_newway('ieodomkazucvgmuy'))


class Test_Day06(TestCase):
    def test_partOne(self):
        d = Day06(['turn on 0,0 through 1,1',
                   'toggle 0,0 through 999,999'])
        d.parse()
        self.assertEqual(999996, d.partA())

    def test_partTwo(self):
        d = Day06(['turn on 0,0 through 1,1',
                   'toggle 0,0 through 999,999'])
        d.parse()
        self.assertEqual(2000004, d.partB())


class Test_Day07(TestCase):
    def test_partOne1(self):
        d = Day07(['123 -> x',
                   '456 -> y',
                   'x AND y -> d',
                   'x OR y -> e',
                   'x LSHIFT 2 -> f',
                   'y RSHIFT 2 -> g',
                   'NOT x -> h',
                   'NOT y -> i'])
        d.parse()
        d.partA()
        self.assertEqual(72, d.store['d'])
        self.assertEqual(507, d.store['e'])
        self.assertEqual(492, d.store['f'])
        self.assertEqual(114, d.store['g'])
        self.assertEqual(65412, d.store['h'])
        self.assertEqual(65079, d.store['i'])
        self.assertEqual(123, d.store['x'])
        self.assertEqual(456, d.store['y'])


class Test_Day08(TestCase):
    def test_partOne(self):
        d = Day08(['""',
                   '"abc"',
                   '"aaa\\"aaa"',
                   '"\\x27"'])
        d.parse()
        self.assertEqual(12, d.partA())

    def test_partTwo(self):
        d = Day08(['""',
                   '"abc"',
                   '"aaa\\"aaa"',
                   '"\\x27"'])
        d.parse()
        self.assertEqual(19, d.partB())


class Test_Day09(TestCase):
    def test_partOne(self):
        d = Day09(['London to Dublin = 464',
                   'London to Belfast = 518',
                   'Dublin to Belfast = 141'])
        d.parse()
        self.assertEqual(605, d.partA())

    def test_partTwo(self):
        d = Day09(['London to Dublin = 464',
                   'London to Belfast = 518',
                   'Dublin to Belfast = 141'])
        d.parse()
        self.assertEqual(982, d.partB())


class Test_Day10(TestCase):
    def test_partOne(self):
        cases = [(['1'], '11'),
                 (['11'], '21'),
                 (['21'], '1211'),
                 (['1211'], '111221'),
                 (['111221'], '312211'),
                 ]
        for testInput, testResult in cases:
            with self.subTest():
                d = Day10(testInput)
                self.assertEqual(testResult, d.lookAndSay(testInput[0]))


class Test_Day11(TestCase):
    def test_increment(self):
        d = Day11(['abcdefgh'])
        d.parse()
        self.assertEqual('abcdefgj', d.increment('abcdefgh'))
        self.assertEqual('ghijklmp', d.increment('ghijklmn'))

    def test_valid(self):
        ''' 
            hijklmmn
            abbceffg
            abbcegjk
        '''
        d = Day11(['abcdefgh'])
        d.parse()
        self.assertEqual(True, d.valid1('hijklmmn'))
        self.assertEqual(False, d.valid2('hijklmmn'))

        self.assertEqual(True, d.valid3('abbceffg'))
        self.assertEqual(False, d.valid1('abbceffg'))

        self.assertEqual(False, d.valid3('abbcegjk'))

    def test_nextValid(self):
        d = Day11(['abcdefgh'])
        d.parse()
        self.assertEqual('abcdffaa', d.partA())

        e = Day11(['ghijklmn'])
        d.parse()
        self.assertEqual('ghjaabcc', e.partA())


class Test_Day12(TestCase):
    def test_partOne(self):
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
        for testInput, testResult in cases:
            with self.subTest():
                d = Day12(testInput)
                self.assertEqual(testResult, d.partA())

    def test_partTwo(self):
        cases = [
            (['[1,2,3]'], 6),
            (['[1,{"c":"red","b":2},3]'], 4),
            (['{"d":"red","e":[1,2,3,4],"f":5}'], 0),
            (['[1,"red",5]'], 6),
        ]
        for testInput, testResult in cases:
            with self.subTest():
                d = Day12(testInput)
                self.assertEqual(testResult, d.partB())


class Test_Day13(TestCase):
    def test_partOne(self):
        testInput = ["Alice would gain 54 happiness units by sitting next to Bob.",
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
        d = Day13(testInput)
        d.parse()
        self.assertEqual(330, d.partA())


class Test_Day14(TestCase):
    def test_partOne(self):
        testInput = ['Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.',
                     'Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.']
        d = Day14(testInput)
        d.parse()
        self.assertEqual(1120, d.runRaceOld(1000))

    def test_partTwo(self):
        testInput = ['Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.',
                     'Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.']
        d = Day14(testInput)
        d.parse()
        self.assertEqual(689, d.runRaceNew(1000))


class Test_Day15(TestCase):
    def test_partOne(self):
        d = Day15(['Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8',
                   'Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3'])
        d.parse()
        self.assertEqual(62842880, d.partA())

    def test_partTwo(self):
        d = Day15(['Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8',
                   'Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3'])
        d.parse()
        self.assertEqual(57600000, d.partB())


class Test_Day16(TestCase):
    def test_partOne(self):
        d = Day16(['turn on 0,0 through 1,1',
                   'toggle 0,0 through 999,999'])
        d.parse()
        self.assertEqual(999996, d.partA())

    def test_partTwo(self):
        d = Day16(['turn on 0,0 through 1,1',
                   'toggle 0,0 through 999,999'])
        d.parse()
        self.assertEqual(2000004, d.partB())


class Test_Day17(TestCase):
    def test_partOne(self):
        d = Day17(['turn on 0,0 through 1,1',
                   'toggle 0,0 through 999,999'])
        d.parse()
        self.assertEqual(999996, d.partA())

    def test_partTwo(self):
        d = Day17(['turn on 0,0 through 1,1',
                   'toggle 0,0 through 999,999'])
        d.parse()
        self.assertEqual(2000004, d.partB())


class Test_Day18(TestCase):
    def test_partOne(self):
        d = Day18(['turn on 0,0 through 1,1',
                   'toggle 0,0 through 999,999'])
        d.parse()
        self.assertEqual(999996, d.partA())

    def test_partTwo(self):
        d = Day18(['turn on 0,0 through 1,1',
                   'toggle 0,0 through 999,999'])
        d.parse()
        self.assertEqual(2000004, d.partB())


class Test_Day19(TestCase):
    def test_partOne(self):
        d = Day19(['turn on 0,0 through 1,1',
                   'toggle 0,0 through 999,999'])
        d.parse()
        self.assertEqual(999996, d.partA())

    def test_partTwo(self):
        d = Day19(['turn on 0,0 through 1,1',
                   'toggle 0,0 through 999,999'])
        d.parse()
        self.assertEqual(2000004, d.partB())


class Test_Day20(TestCase):
    def test_partOne(self):
        d = Day20(['turn on 0,0 through 1,1',
                   'toggle 0,0 through 999,999'])
        d.parse()
        self.assertEqual(999996, d.partA())

    def test_partTwo(self):
        d = Day20(['turn on 0,0 through 1,1',
                   'toggle 0,0 through 999,999'])
        d.parse()
        self.assertEqual(2000004, d.partB())


if __name__ == '__main__':
    unittest.main()
