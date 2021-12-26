import sys


def main():
    if len(sys.argv) != 2:
        sys.exit("Please provide a file name for input data")

    total_code, total_memory = 0, 0
    this_code, this_memory = 0, 0

    filename = sys.argv[1]
    with open(filename, "r") as inputfile:
        while True:
            line = inputfile.readline()
            if not line:
                break
            tmp = line.strip()
            # print(tmp)

            this_code = len(tmp)

            # strip leading/trailing "
            string = tmp[1:-1]

            # handle \
            stripped, seen_backslash, idx = '', False, 0
            done = (idx >= len(string))
            while not done:
                ch = string[idx]
                if seen_backslash and ch == '\\':
                    stripped += ch
                    idx += 1
                    seen_backslash = False
                elif seen_backslash and ch == '"':
                    stripped += ch
                    idx += 1
                    seen_backslash = False
                elif seen_backslash and ch == 'x':
                    stripped += 'Z'
                    idx += 3
                    seen_backslash = False
                elif seen_backslash:
                    seen_backslash = False
                    idx += 1
                elif not seen_backslash and ch == '\\':
                    seen_backslash = True
                    idx += 1
                else:
                    stripped += ch
                    idx += 1

                done = idx >= len(string)

            this_memory = len(stripped)
            # print(f"  {this_code} {this_memory}")
            total_code += this_code
            total_memory += this_memory
    print(f"{total_code} {total_memory} : {total_code-total_memory}")


if __name__ == '__main__':
    main()
