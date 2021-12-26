import sys


def main():
    if len(sys.argv) != 2:
        sys.exit("Please provide a file name for input data")

    dots = set()
    folds = []
    filename = sys.argv[1]
    with open(filename, "r") as inputfile:
        while True:
            line = inputfile.readline()
            if not line:
                break
            input_line = line.strip()
            # print(f"{input_line}")

            left_parens, right_parens = input_line.count('('), input_line.count(')')
            for basement in range(len(input_line) + 1):
                sub_line = input_line[0:basement]
                # print(f"{basement} {sub_line} {input_line}")
                lp, rp = sub_line.count('('), sub_line.count(')')
                if lp - rp == -1:
                    print(f"Enters the basement at position {basement}")
                    break

            print(f"Ultimate Floor = {left_parens - right_parens}")
            # testing commit

if __name__ == '__main__':
    main()
