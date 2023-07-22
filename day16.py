from advent import Advent, Runner, File_to_String
import sys


class Day16(Advent):
    def __init__(self, input_text):
        self.name = "16"
        self.lines = input_text
        self.inventory = {'children': {}, 'cats': {}, 'samoyeds': {}, 'pomeranians': {}, 'akitas': {},
                          'vizslas': {}, 'goldfish': {}, 'trees': {}, 'cars': {}, 'perfumes': {}}

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

    def partA(self):
        scene = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0, 'vizslas': 0, 'goldfish': 5,
                 'trees': 3, 'cars': 2, 'perfumes': 1}

        all_sues = set()
        for k, v_dict in self.inventory.items():
            all_sues.update(v_dict.keys())

        for k, v in scene.items():
            to_remove = []
            for sue in all_sues:
                if sue in self.inventory[k] and self.inventory[k][sue] != v:
                    to_remove.append(sue)
            for x in to_remove:
                all_sues.remove(x)
        print(f"Remainining Sues: {all_sues}")
        return all_sues

    def partB(self):
        scene_equals = {'children': 3, 'samoyeds': 2,
                        'akitas': 0, 'vizslas': 0, 'cars': 2, 'perfumes': 1}
        scene_greater = {'cats': 7, 'trees': 3}
        scene_less = {'pomeranians': 3, 'goldfish': 5}

        all_sues = set()
        for k, v_dict in self.inventory.items():
            all_sues.update(v_dict.keys())

        for k, v in scene_equals.items():
            to_remove = []
            for sue in all_sues:
                if sue in self.inventory[k] and self.inventory[k][sue] != v:
                    to_remove.append(sue)
            for x in to_remove:
                all_sues.remove(x)
        # print(f"Scene Equals Sues: {all_sues}")

        for k, v in scene_greater.items():
            to_remove = []
            for sue in all_sues:
                if sue in self.inventory[k] and self.inventory[k][sue] <= v:
                    to_remove.append(sue)
            for wrong_sue in to_remove:
                all_sues.remove(wrong_sue)
        # print(f"Scene Greater Sues: {all_sues}")

        for k, v in scene_less.items():
            to_remove = []
            for sue in all_sues:
                if sue in self.inventory[k] and self.inventory[k][sue] >= v:
                    to_remove.append(sue)
            for wrong_sue in to_remove:
                all_sues.remove(wrong_sue)
        # print(f"Scene Less Sues: {all_sues}")
        print(f"Remainining Sues: {all_sues}")
        return all_sues


def main():
    aoc1 = Day16(File_to_String("day16-live.txt"))
    runner = Runner(aoc1)
    runner.run()


if __name__ == '__main__':
    main()