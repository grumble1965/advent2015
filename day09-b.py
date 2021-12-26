import sys


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

            for i in range(50):
                output_str = iterator(tmp)
                print(f"{i+1}: {len(output_str)}")
                tmp = output_str


def iterator(tmp):
    output_str, last_character, counter = '', None, 0
    for ch in tmp:
        print(ch, end='')
        if last_character is not None and ch == last_character:
            counter += 1
        elif last_character is None:
            last_character = ch
            counter = 1
        elif last_character != ch:
            output_str = output_str + str(counter) + last_character
            last_character = ch
            counter = 1
        else:
            print("What?")
    print()
    output_str = output_str + str(counter) + last_character
    return output_str


if __name__ == '__main__':
    main()
