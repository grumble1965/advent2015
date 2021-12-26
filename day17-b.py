import sys
import itertools


def main():
    if len(sys.argv) != 2:
        sys.exit("Please provide a file name for input data")

    filename = sys.argv[1]
    containers = []
    with open(filename, "r") as inputfile:
        while True:
            line = inputfile.readline()
            if not line:
                break
            tmp = line.strip()
            containers.append(int(tmp))
            # print(f"{tmp}")

    working_perms = set()
    for num_containers in range(len(containers)):
        iter_list = itertools.combinations(range(len(containers)), num_containers+1)
        for pp in iter_list:
            sum = 0
            for idx in pp:
                sum += containers[idx]
            if sum == 150:
                cc = [containers[jdx] for jdx in range(len(containers)) if jdx in pp ]
                # print(cc, sum)
                working_perms.add(pp)
    print(f"total working permutations = {len(working_perms)}")

    len_count = {}
    for p in working_perms:
        ll = len(p)
        if ll in len_count:
            len_count[ll] += 1
        else:
            len_count[ll] = 1
    min_perm = min(list(len_count.keys()))
    print(f"smallest permutation is length {min_perm} with {len_count[min_perm]} possible")


if __name__ == '__main__':
    main()