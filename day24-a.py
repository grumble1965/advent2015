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
    print(f"Total sum = {total}, Group sum = {total // 3}")

    candidates = []
    package_set = set(packages)
    for ll in range(1, len(packages) - 1):
        for front in filterfalse(lambda ss: sum(ss) != total // 3, combinations(packages, r=ll)):
            remaining_set = package_set - set(front)
            remaining = list(remaining_set)
            left_iter = filterfalse(lambda ss: sum(ss) != total // 3,
                                    chain.from_iterable(
                                        [combinations(remaining, r=ll) for ll in range(1, len(remaining))]))
            for left in left_iter:
                # any valid packing for left side implies a valid right side exists
                # thus, the front packing is valid
                ft = sorted(front)
                if ft not in candidates:
                    candidates.append(ft)
                break

        # if any candidates have been found, don't make a longer packing
        if candidates:
            break

    print(candidates)
    best = sorted(candidates, key=lambda cc: list(accumulate(cc, operator.mul))[-1])[0]
    print('Part A: ', best, ' QE =', list(accumulate(best, operator.mul))[-1])


if __name__ == '__main__':
    main()
