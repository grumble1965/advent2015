""" Solution for Day 16 """

from advent import Advent, Runner, file_to_string


class Day16(Advent):
    """ class for Day 16 solution """

    def __init__(self, input_text):
        super().__init__()
        self.name = "16"
        self.lines = input_text
        self.inventory = {'children': {}, 'cats': {}, 'samoyeds': {}, 'pomeranians': {},
                          'akitas': {}, 'vizslas': {}, 'goldfish': {}, 'trees': {},
                          'cars': {}, 'perfumes': {}}

    def parse(self):
        for line in self.lines:
            tmp = line.strip()
            # print(f"{tmp}")
            words = tmp.replace(':', '').replace(',', '').split()
            name = words[0] + words[1]
            key1, value1 = words[2], words[3]
            key2, value2 = words[4], words[5]
            key3, value3 = words[6], words[7]
            # print(f"{name}  {key1}{value1}  {key2}{value2}  {key3}{value3}")
            self.inventory[key1][name] = int(value1)
            self.inventory[key2][name] = int(value2)
            self.inventory[key3][name] = int(value3)

    def part_one(self):
        scene = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0,
                 'vizslas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1}

        all_sues = set()
        for k, v_dict in self.inventory.items():
            all_sues.update(v_dict.keys())

        for k, count in scene.items():
            to_remove = []
            for sue in all_sues:
                if sue in self.inventory[k] and self.inventory[k][sue] != count:
                    to_remove.append(sue)
            for sue in to_remove:
                all_sues.remove(sue)
        print(f"Remainining Sues: {all_sues}")
        return all_sues

    def part_two(self):
        scene_equals = {'children': 3, 'samoyeds': 2,
                        'akitas': 0, 'vizslas': 0, 'cars': 2, 'perfumes': 1}
        scene_greater = {'cats': 7, 'trees': 3}
        scene_less = {'pomeranians': 3, 'goldfish': 5}

        all_sues = set()
        for k, v_dict in self.inventory.items():
            all_sues.update(v_dict.keys())

        for k, count in scene_equals.items():
            to_remove = []
            for sue in all_sues:
                if sue in self.inventory[k] and self.inventory[k][sue] != count:
                    to_remove.append(sue)
            for sue in to_remove:
                all_sues.remove(sue)
        # print(f"Scene Equals Sues: {all_sues}")

        for k, count in scene_greater.items():
            to_remove = []
            for sue in all_sues:
                if sue in self.inventory[k] and self.inventory[k][sue] <= count:
                    to_remove.append(sue)
            for wrong_sue in to_remove:
                all_sues.remove(wrong_sue)
        # print(f"Scene Greater Sues: {all_sues}")

        for k, count in scene_less.items():
            to_remove = []
            for sue in all_sues:
                if sue in self.inventory[k] and self.inventory[k][sue] >= count:
                    to_remove.append(sue)
            for wrong_sue in to_remove:
                all_sues.remove(wrong_sue)
        # print(f"Scene Less Sues: {all_sues}")
        print(f"Remainining Sues: {all_sues}")
        return all_sues


def main():
    """ stub for main() """
    aoc1 = Day16(file_to_string("day16-live.txt"))
    runner = Runner(aoc1)
    runner.run()


if __name__ == '__main__':
    main()
