import sys
import re


def main():
    if len(sys.argv) != 2:
        sys.exit("Please provide a file name for input data")

    file_sum = 0
    filename = sys.argv[1]
    with open(filename, "r") as inputfile:
        while True:
            line = inputfile.readline()
            if not line:
                break
            tmp = line.strip()
            numbers = re.findall("-?\d+", tmp)
            line_sum = 0
            for num in numbers:
                line_sum += int(num)
            print(f"{tmp} -> {line_sum}")
            file_sum += line_sum
    print(f"File sum = {file_sum}")


if __name__ == '__main__':
    main()


