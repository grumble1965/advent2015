import sys


def main():
    if len(sys.argv) != 2:
        sys.exit("Please provide a file name for input data")

    houses = {}
    filename = sys.argv[1]
    with open(filename, "r") as inputfile:
        while True:
            line = inputfile.readline()
            if not line:
                break
            tmp = line.strip()

            x, y = 0, 0
            location = (x, y)
            houses[location] = 1
            for ch in tmp:
                if ch == '^':
                    x, y = x, y+1
                elif ch == 'v':
                    x, y = x, y-1
                elif ch == '<':
                    x, y = x-1, y+0
                elif ch == '>':
                    x, y = x+1, y+0
                else:
                    print(f"Unknown direction {ch}")

                location = (x, y)
                if location in houses:
                    houses[location] += 1
                else:
                    houses[location] = 1

    print(houses)
    visits = len(houses.keys())
    print(f"Santa visited {visits} unique houses")


if __name__ == '__main__':
    main()
