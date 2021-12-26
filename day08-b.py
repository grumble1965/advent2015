import sys


def main():
    if len(sys.argv) != 2:
        sys.exit("Please provide a file name for input data")

    total_original, total_encoded = 0, 0
    this_original, this_encoded = 0, 0

    filename = sys.argv[1]
    with open(filename, "r") as inputfile:
        while True:
            line = inputfile.readline()
            if not line:
                break
            tmp = line.strip()
            # print(tmp)

            original = tmp
            this_original = len(original)

            encoded = ''
            for ch in original:
                if ch == '\\':
                    encoded += '\\'
                    encoded += '\\'
                elif ch == '"':
                    encoded += '\\'
                    encoded += '"'
                else:
                    encoded += ch
            encoded = '"' + encoded + '"'

            this_encoded = len(encoded)
            print(f"  {this_original} {this_encoded}")
            total_original += this_original
            total_encoded += this_encoded
    print(f"{total_original} {total_encoded} : {total_encoded-total_original}")


if __name__ == '__main__':
    main()
