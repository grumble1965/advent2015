""" Solution for Day 21 """

from itertools import permutations, product
from advent import Advent, Runner, file_to_string


class Day21(Advent):
    """ class for Day 21 solution """

    def __init__(self, input_text):
        super().__init__()
        self.name = "21"
        self.lines = input_text
        self.weapons = [('Dagger', 8, 4, 0),
                        ('Shortsword', 10, 5, 0),
                        ('Warhammer', 25, 6, 0),
                        ('Longsword', 40, 7, 0),
                        ('Greataxe', 74, 8, 0)]
        self.armor = [('none', 0, 0, 0),
                      ('Leather', 13, 0, 1),
                      ('Chainmail', 31, 0, 2),
                      ('Splitmail', 53, 0, 3),
                      ('Bandedmail', 75, 0, 4),
                      ('Platemail', 102, 0, 5)]
        self.rings = [('none1', 0, 0, 0),
                      ('none2', 0, 0, 0),
                      ('Damage +1', 25, 1, 0),
                      ('Damage +2', 50, 2, 0),
                      ('Damage +3', 100, 3, 0),
                      ('Defense +1', 20, 0, 1),
                      ('Defense +2', 40, 0, 2),
                      ('Defense +3', 80, 0, 3)]
        self.boss_hp = None
        self.boss_damage = None
        self.boss_armor = None

    def parse(self):
        for line in self.lines:
            tmp = line.strip()
            # print(f"{tmp}")
            words = tmp.split(':')
            if words[0] == 'Hit Points':
                self.boss_hp = int(words[1])
            elif words[0] == 'Damage':
                self.boss_damage = int(words[1])
            elif words[0] == 'Armor':
                self.boss_armor = int(words[1])
            else:
                print(f"Couldn't parse {words}")

    def battle(self, player, boss):
        """ run a battle """
        p_hp, p_damage, p_armor = player
        b_hp, b_damage, b_armor = boss

        while True:
            p_hit = max([p_damage - b_armor, 1])
            b_hp -= p_hit
            # print(f"The player deals {p_hit} damage; the boss goes down to {b_hp} hit points")
            if b_hp <= 0:
                # print("Player wins")
                return "player"

            b_hit = max([b_damage - p_armor, 1])
            p_hp -= b_hit
            # print(f"The boss deals {b_hit} damage; the player goes down to {p_hp} hit points")
            if p_hp <= 0:
                # print("Boss wins")
                return "boss"

    def part_one(self):
        winning_configs = set()
        winning_costs = []
        total_configs = 0
        for config in product(permutations(self.weapons, 1),
                              permutations(self.armor, 1),
                              permutations(self.rings, 2)):
            total_configs += 1
            w_tmp, a_tmp, (r1_tmp, r2_tmp) = config
            weap, armor, rr1, rr2 = w_tmp[0], a_tmp[0], r1_tmp, r2_tmp
            # print(f"{ww} {aa} {rr1}, {rr2}")
            player = (100, weap[2]+armor[2]+rr1[2]+rr2[2],
                      weap[3]+armor[3]+rr1[3]+rr2[3])
            # print(f"{player}")
            boss = (self.boss_hp, self.boss_damage, self.boss_armor)
            if self.battle(player, boss) == 'player':
                winning_configs.add(config)
                winning_costs.append(weap[1]+armor[1]+rr1[1]+rr2[1])

        # print(f"There are {total_configs} configurations and {len(winning_configs)} win")
        print(f"Lowest cost winning configuration is {min(winning_costs)}")
        return min(winning_costs)

    def part_two(self):
        winning_configs = set()
        winning_costs = []
        losing_costs = []
        total_configs = 0
        for config in product(permutations(self.weapons, 1),
                              permutations(self.armor, 1),
                              permutations(self.rings, 2)):
            total_configs += 1
            w_tmp, a_tmp, (r1_tmp, r2_tmp) = config
            weapon, armor, rr1, rr2 = w_tmp[0], a_tmp[0], r1_tmp, r2_tmp
            # print(f"{ww} {aa} {rr1}, {rr2}")
            player = (100, weapon[2]+armor[2]+rr1[2]+rr2[2],
                      weapon[3]+armor[3]+rr1[3]+rr2[3])
            # print(f"{player}")
            boss = (self.boss_hp, self.boss_damage, self.boss_armor)
            cost = weapon[1]+armor[1]+rr1[1]+rr2[1]
            if self.battle(player, boss) == 'player':
                winning_configs.add(config)
                winning_costs.append(cost)
            else:
                losing_costs.append(cost)

        # print(f"There are {total_configs} configurations and {len(winning_configs)} win")
        # print(f"Lowest cost winning configuration is {min(winning_costs)}")
        print(f"Highest cost losing configuration is {max(losing_costs)}")
        return max(losing_costs)


def main():
    """ stub for main() """
    aoc1 = Day21(file_to_string("day21-live.txt"))
    runner = Runner(aoc1)
    runner.run()


if __name__ == '__main__':
    main()
