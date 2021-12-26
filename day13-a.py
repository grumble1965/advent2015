import sys
from itertools import permutations


def main():
    if len(sys.argv) != 2:
        sys.exit("Please provide a file name for input data")

    costs = {}
    family = set()
    filename = sys.argv[1]
    with open(filename, "r") as inputfile:
        while True:
            line = inputfile.readline()
            if not line:
                break
            tmp = line.strip().replace('.', '')
            words = tmp.split()
            p0, direction, amount, p1 = words[0], words[2], int(words[3]), words[10]
            if direction == 'lose':
                amount = -amount
            # print(f"{p0}->{p1} = {amount}")
            costs[(p0, p1)] = amount
            family.add(p0)
            family.add(p1)
        # print(costs)
        # print(family)

    # for f in family:
    #     costs[(f, 'me')] = 0
    #     costs[('me', f)] = 0
    # family.add('me')

    best_score, best_permutation = None, None
    for combo in permutations(family):
        # print(combo)
        score = 0
        for p0 in family:
            combo_list = list(combo)
            p0_idx = combo_list.index(p0)
            p_left_idx, p_right_idx = p0_idx-1, p0_idx+1
            if p_left_idx < 0:
                p_left_idx += len(combo_list)
            if p_right_idx >= len(combo_list):
                p_right_idx -= len(combo_list)
            p_left, p_right = combo_list[p_left_idx], combo_list[p_right_idx]
            # print(f"{p_left} <- {p0} = {costs[(p0, p_left)]}")
            # print(f"{p0} -> {p_right} = {costs[(p0, p_right)]}")
            score += costs[(p0, p_left)]
            score += costs[(p0, p_right)]

        if best_score is None or score > best_score:
            best_score = score
            best_permutation = combo

    print(f"best combo = {best_permutation} with happiness = {best_score}")


if __name__ == '__main__':
    main()


