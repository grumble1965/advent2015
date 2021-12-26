import sys
import hashlib


def main():
    if len(sys.argv) != 2:
        sys.exit("Please provide a file name for input data")

    nice_strings = 0
    filename = sys.argv[1]
    with open(filename, "r") as inputfile:
        while True:
            line = inputfile.readline()
            if not line:
                break
            tmp = line.strip()

            rule1 = False
            for i in range(len(tmp)-1):
                pair, rest = tmp[i:i+2], tmp[i+2:]
                # print(f"{pair} + {rest}")
                if rest.count(pair) > 0:
                    rule1 = True
                    break
            # if not rule1:
            #     print(f"fails rule 1: {tmp}")

            rule2 = False
            for i in range(len(tmp)-2):
                ch1, _, ch2 = tmp[i], tmp[i+1], tmp[i+2]
                if ch1 == ch2:
                    rule2 = True
                    break
            # if not rule2:
            #     print(f"fails rule 2: {tmp}")

            if rule1 and rule2:
                print(f"{tmp} is nice")
                nice_strings += 1
            else:
                print(f"{tmp} is naughty")

    print(f"Seen {nice_strings} nice strings")


if __name__ == '__main__':
    main()
