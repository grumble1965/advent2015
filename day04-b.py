import sys
import hashlib


def main():
    if len(sys.argv) != 2:
        sys.exit("Please provide a file name for input data")

    filename = sys.argv[1]
    with open(filename, "r") as inputfile:
        while True:
            line = inputfile.readline()
            if not line:
                break
            tmp = line.strip()

            key = tmp
            number = 1
            while True:
                target = f"{key}{number}"
                hash_obj = hashlib.md5(bytes(target, 'utf-8'))
                if hash_obj.hexdigest().startswith('000000'):
                    break
                number += 1
            print(f"For key {key}, the lowest positive integer is {number}")


if __name__ == '__main__':
    main()
