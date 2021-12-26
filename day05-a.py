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

            count_vowels = tmp.count('a') + tmp.count('e') + tmp.count('i') + tmp.count('o') + tmp.count('u')
            count_dupes = len([i for i in range(len(tmp)-1) if tmp[i] == tmp[i+1]])
            count_bad = tmp.count('ab') + tmp.count('cd') + tmp.count('pq') + tmp.count('xy')

            if count_vowels >= 3 and count_dupes > 0 and count_bad == 0:
                nice_strings += 1
            else:
                print(f"{tmp} is naughty")

    print(f"Seen {nice_strings} nice strings")


if __name__ == '__main__':
    main()
