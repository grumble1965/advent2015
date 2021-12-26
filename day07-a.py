import sys


def main():
    if len(sys.argv) != 2:
        sys.exit("Please provide a file name for input data")

    rules = []
    store = {}
    filename = sys.argv[1]
    with open(filename, "r") as inputfile:
        while True:
            line = inputfile.readline()
            if not line:
                break
            tmp = line.strip()

            lhs, rhs = tmp.split(' -> ')
            lops = lhs.split(' ')

            if len(lops) == 1:
                input = lops[0]
                if not str(input).islower():
                    input = int(input)
                rules.append(([input], 'ASSIGN', rhs))
            elif len(lops) == 2:
                rules.append(([lops[1]], 'NOT', rhs))
            elif len(lops) == 3:
                if lops[1] in ['AND', 'OR']:
                    rules.append(([lops[0], lops[2]], lops[1], rhs))
                elif lops[1] in ['LSHIFT', 'RSHIFT']:
                    rules.append(([lops[0], int(lops[2])], lops[1], rhs))
            else:
                print(f"Bad parse {lhs} {rhs}")

        # init sensitivity and outputs
        sensitivity = []
        outputs = []
        for rule in rules:
            (sens_list, command, output) = rule
            for var in sens_list:
                if str(var).islower() and var not in sensitivity:
                    sensitivity.append(var)
            if output not in outputs:
                outputs.append(output)

        print(f"{sensitivity}")
        print(f"{outputs}")

        for vv in outputs:
            store[vv] = None
        print(store)

        while len([var for var in store.values() if var is None]) > 0:
            for rule in rules:
                (sens_list, command, output) = rule
                arg_list = []
                for vv in sens_list:
                    if str(vv).islower():
                        arg_list.append(store[vv])
                    else:
                        arg_list.append(int(vv))
                if None not in arg_list:
                    result = None
                    if command == 'ASSIGN':
                        result = arg_list[0]
                    elif command == 'NOT':
                        result = ~arg_list[0]
                    elif command == 'AND':
                        result = arg_list[0] & arg_list[1]
                    elif command == 'OR':
                        result = arg_list[0] | arg_list[1]
                    elif command == 'LSHIFT':
                        result = arg_list[0] << arg_list[1]
                    elif command == 'RSHIFT':
                        result = arg_list[0] >> arg_list[1]
                    else:
                        print(f"INVALID COMMAND {command}")
                    while result < 0:
                        result += 65536
                    store[output] = result

    # for vv in sorted(store):
    #     print(f"{vv}: {store[vv]}")
    print(f"wire a: {store['a']}")


if __name__ == '__main__':
    main()
