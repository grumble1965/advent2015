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

            x, y = [0, 0], [0, 0]
            houses[(0, 0)] = 2
            turn = 0
            houses[(x[turn], y[turn])] = 1
            for ch in tmp:
                if ch == '^':
                    x[turn], y[turn] = x[turn], y[turn]+1
                elif ch == 'v':
                    x[turn], y[turn] = x[turn], y[turn]-1
                elif ch == '<':
                    x[turn], y[turn] = x[turn]-1, y[turn]+0
                elif ch == '>':
                    x[turn], y[turn] = x[turn]+1, y[turn]+0
                else:
                    print(f"Unknown direction {ch}")

                if (x[turn], y[turn]) in houses:
                    houses[(x[turn], y[turn])] += 1
                else:
                    houses[(x[turn], y[turn])] = 1

                turn += 1
                if turn == 2:
                    turn = 0

    visits = len(houses.keys())
    print(f"Santa visited {visits} unique houses")


if __name__ == '__main__':
    main()
