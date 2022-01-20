import sys


def main():
    if len(sys.argv) != 2:
        sys.exit("Please provide a file name for input data")

    goal = (None, None)
    filename = sys.argv[1]
    with open(filename, "r") as inputfile:
        while True:
            line = inputfile.readline()
            if not line:
                break
            tmp = line.strip()
            #print(f"{tmp}")
            words = tmp.replace('.', '').replace(',', '').split()
            r_goal = int(words[words.index('row')+1])
            c_goal = int(words[words.index('column')+1])
            goal = (r_goal, c_goal)

    print(f"Goal is at {goal}")
    code = 20151125
    for i in diagonal_counter():
        if i == goal:
            print(i, code)
            break
        code = (code * 252533) % 33554393


def diagonal_counter():
    r, c = 1, 1
    yield r, c
    while True:
        if r == 1:
            r, c = c + 1, 1
        else:
            r, c = r - 1, c + 1
        yield r, c


if __name__ == '__main__':
    main()
