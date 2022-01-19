from itertools import accumulate, chain, combinations, filterfalse
import operator
import sys


def main():
    if len(sys.argv) != 2:
        sys.exit("Please provide a file name for input data")

    packages = set()
    filename = sys.argv[1]
    with open(filename, "r") as inputfile:
        while True:
            line = inputfile.readline()
            if not line:
                break
            tmp = line.strip()
            # print(f"{tmp}")
            packages.add(int(tmp))

    total = sum(packages)
    print(f"Total sum = {total}, Group sum = {total // 4}")

    candidates = []
    package_set = set(packages)
    for ll in range(1, len(packages) - 2):
        for front in filterfalse(lambda ss: sum(ss) != total // 4, combinations(packages, r=ll)):
            remaining_set = package_set - set(front)
            remaining = list(remaining_set)
            trunk_iter = filterfalse(lambda ss: sum(ss) != total // 4,
                                     chain.from_iterable(
                                         [combinations(remaining, r=ll) for ll in range(1, len(remaining) - 1)]))
            for trunk in trunk_iter:
                early_exit = False
                side_remaining_set = remaining_set - set(trunk)
                side_remaining = list(side_remaining_set)
                left_iter = filterfalse(lambda ss: sum(ss) != total // 4,
                                        chain.from_iterable([combinations(side_remaining, r=ll) for ll in
                                                             range(1, len(side_remaining) - 1)]))
                for left in left_iter:
                    # any valid packing for left side implies a valid right side exists
                    # thus, the front packing is valid
                    ft = sorted(front)
                    if ft not in candidates:
                        candidates.append(ft)
                    early_exit = True
                    break

                if early_exit:
                    break

        # if any candidates have been found, don't make a longer packing
        if candidates:
            break

    print(candidates)
    best = sorted(candidates, key=lambda cc: list(accumulate(cc, operator.mul))[-1])[0]
    print('Part B: ', best, ' QE =', list(accumulate(best, operator.mul))[-1])


if __name__ == '__main__':
    main()
