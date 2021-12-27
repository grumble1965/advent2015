import sys


def main():
    if len(sys.argv) != 2:
        sys.exit("Please provide a file name for input data")

    filename = sys.argv[1]
    rules = []
    start = None
    with open(filename, "r") as inputfile:
        while True:
            line = inputfile.readline()
            if not line:
                break
            tmp = line.strip()
            #print(f"{tmp}")
            if tmp != '' and tmp.find('=>') == -1:
                start = tmp
            elif tmp.find('=>') >= 0:
                words = tmp.split('=>')
                lhs = words[0].strip()
                rhs = words[1].strip()
                tt = (lhs, rhs)
                rules.append(tt)

    print(f"Starting with {start}")
    print(f"{rules}")

    molecules = set()
    for lhs, rhs in rules:
        print(f"rule {lhs} -> {rhs}")
        idx = 0
        while True:
            next = start.find(lhs, idx)
            if next == -1:
                break
            molecules.add(start[:next] + rhs + start[next+len(lhs):])
            # print(f"{start[:next]} *{rhs}* {start[next+len(lhs):]}")
            idx = next+1
    print(f"Yields {len(molecules)} unique molecules")


if __name__ == '__main__':
    main()