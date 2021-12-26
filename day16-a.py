import sys


def main():
    if len(sys.argv) != 2:
        sys.exit("Please provide a file name for input data")

    filename = sys.argv[1]
    inventory = {'children': {}, 'cats': {}, 'samoyeds': {}, 'pomeranians': {}, 'akitas': {},
                 'vizslas': {}, 'goldfish': {}, 'trees': {}, 'cars': {}, 'perfumes': {}}
    with open(filename, "r") as inputfile:
        while True:
            line = inputfile.readline()
            if not line:
                break
            tmp = line.strip()
            # print(f"{tmp}")
            words = tmp.replace(':', '').replace(',', '').split()
            name = words[0] + words[1]
            key1, value1 = words[2], words[3]
            key2, value2 = words[4], words[5]
            key3, value3 = words[6], words[7]
            # print(f"{name}  {key1}{value1}  {key2}{value2}  {key3}{value3}")
            inventory[key1][name] = int(value1)
            inventory[key2][name] = int(value2)
            inventory[key3][name] = int(value3)

    scene = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0, 'vizslas': 0, 'goldfish': 5,
             'trees': 3, 'cars': 2, 'perfumes': 1}

    all_sues = set()
    for k, v_dict in inventory.items():
        all_sues.update(v_dict.keys())

    for k, v in scene.items():
        to_remove = []
        for sue in all_sues:
            if sue in inventory[k] and inventory[k][sue] != v:
                to_remove.append(sue)
        for x in to_remove:
            all_sues.remove(x)
    print(f"Remainining Sues: {all_sues}")

if __name__ == '__main__':
    main()