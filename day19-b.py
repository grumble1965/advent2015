import sys
from collections import deque


def main():
    if len(sys.argv) != 2:
        sys.exit("Please provide a file name for input data")

    filename = sys.argv[1]
    medicine = None
    rules = []
    with open(filename, "r") as inputfile:
        while True:
            line = inputfile.readline()
            if not line:
                break
            tmp = line.strip()
            # print(f"{tmp}")
            if tmp != '' and tmp.find('=>') == -1:
                medicine = tmp
            elif tmp.find('=>') >= 0:
                words = tmp.split('=>')
                lhs = words[0].strip()
                rhs = words[1].strip()
                tt = (lhs, rhs)
                rules.append(tt)

    q = deque()
    q.append((medicine, 0))

    solutions = []
    seen = {}
    for ll in range(len(medicine) * 2):
        seen[ll] = set()
    iteration_ctr = 0

    while q:
        if iteration_ctr % 10000 == 0:
            sum_seen = sum([len(seen[ll]) for ll in seen])
            print(f"{iteration_ctr}: Queue = {len(q)}  Seen = {sum_seen}")
        iteration_ctr += 1

        seed, steps = q.pop()
        if seed == 'e':
            print(f"solution!  {steps}")
            solutions.append(steps)
            if len(solutions) > 3:
                break
        else:
            next_steps = set()
            for lhs, rhs in rules:
                new_str, d_steps = seed, 0
                while rhs in new_str:
                    new_str = new_str.replace(rhs, lhs, 1)
                    d_steps += 1
                if new_str not in seen[len(new_str)]:
                    next_steps.add((new_str, steps+d_steps))

            for ns, st in next_steps:
                tt = (ns, st)
                q.append(tt)

            seen[len(seed)].add(seed)

    print(f"Best solution:  {min(solutions)}")


if __name__ == '__main__':
    main()
