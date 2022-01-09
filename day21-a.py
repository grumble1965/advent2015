import sys
from itertools import permutations, product

weapons = [('Dagger', 8, 4, 0), ('Shortsword', 10, 5, 0), ('Warhammer', 25, 6, 0), ('Longsword', 40, 7, 0),
           ('Greataxe', 74, 8, 0)]
armor = [('none', 0, 0, 0), ('Leather', 13, 0, 1), ('Chainmail', 31, 0, 2), ('Splitmail', 53, 0, 3),
         ('Bandedmail', 75, 0, 4), ('Platemail', 102, 0, 5)]
rings = [('none1', 0, 0, 0), ('none2', 0, 0, 0), ('Damage +1', 25, 1, 0), ('Damage +2', 50, 2, 0),
         ('Damage +3', 100, 3, 0), ('Defense +1', 20, 0, 1), ('Defense +2', 40, 0, 2), ('Defense +3', 80, 0, 3)]


def main():
    if len(sys.argv) != 2:
        sys.exit("Please provide a file name for input data")

    filename = sys.argv[1]
    boss_hp, boss_damage, boss_armor = None, None, None
    with open(filename, "r") as inputfile:
        while True:
            line = inputfile.readline()
            if not line:
                break
            tmp = line.strip()
            # print(f"{tmp}")
            words = tmp.split(':')
            if words[0] == 'Hit Points':
                boss_hp = int(words[1])
            elif words[0] == 'Damage':
                boss_damage = int(words[1])
            elif words[0] == 'Armor':
                boss_armor = int(words[1])
            else:
                print(f"Couldn't parse {words}")

    winning_configs = set()
    winning_costs = []
    total_configs = 0
    for config in product(permutations(weapons, 1),
                          permutations(armor, 1),
                          permutations(rings, 2)):
        total_configs += 1
        w_tmp, a_tmp, (r1_tmp, r2_tmp) = config
        ww, aa, rr1, rr2 = w_tmp[0], a_tmp[0], r1_tmp, r2_tmp
        # print(f"{ww} {aa} {rr1}, {rr2}")
        player = (100, ww[2]+aa[2]+rr1[2]+rr2[2], ww[3]+aa[3]+rr1[3]+rr2[3])
        # print(f"{player}")
        boss = (boss_hp, boss_damage, boss_armor)
        if battle(player, boss) == 'player':
            winning_configs.add(config)
            winning_costs.append(ww[1]+aa[1]+rr1[1]+rr2[1])

    print(f"There are {total_configs} configurations and {len(winning_configs)} win")
    print(f"Lowest cost wining configuration is {min(winning_costs)}")



def battle(player, boss):
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


if __name__ == '__main__':
    main()
