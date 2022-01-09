import sys


def main():
    if len(sys.argv) != 2:
        sys.exit("Please provide a file name for input data")

    presents_total = None
    filename = sys.argv[1]
    with open(filename, "r") as inputfile:
        while True:
            line = inputfile.readline()
            if not line:
                break
            tmp = line.strip()
            # print(f"{tmp}")
            if presents_total is None:
                presents_total = int(tmp)

    print(f"Presents total = {presents_total}")

    elf_limit = 1000000

    print("Initialize houses")
    house = {}
    for ee in range(1, elf_limit+1):
        house[ee] = 0

    print("Fill houses")
    for ee in range(1, elf_limit+1):
        limit = elf_limit + 1
        for hh in range(ee, limit, ee):
            house[hh] += 10 * ee

    print("Find house")
    found = False
    for elf in range(1, elf_limit):
        presents = house[elf]
        if presents >= presents_total:
            print(f"House {elf} has {presents} presents")
            found = True
            break

    if not found:
        print("reached elf_limit without finding an answer")


if __name__ == '__main__':
    main()