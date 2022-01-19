import sys


def main():
    if len(sys.argv) != 2:
        sys.exit("Please provide a file name for input data")

    code = []
    filename = sys.argv[1]
    with open(filename, "r") as inputfile:
        while True:
            line = inputfile.readline()
            if not line:
                break
            tmp = line.strip()
            # print(f"{tmp}")
            tmp = tmp.replace(',', '')
            tmp = tmp.replace('+', '')
            words = tmp.split()
            code.append(words)

    reg = {'a': 1, 'b': 0}
    pc = 0
    while pc in range(len(code)):
        opc = code[pc][0]
        if opc == 'hlf':
            rr = code[pc][1]
            reg[rr] //= 2
            pc += 1
        elif opc == 'tpl':
            rr = code[pc][1]
            reg[rr] *= 3
            pc += 1
        elif opc == 'inc':
            rr = code[pc][1]
            reg[rr] += 1
            pc += 1
        elif opc == 'jmp':
            off = int(code[pc][1])
            pc += off
        elif opc == 'jie':
            rr = code[pc][1]
            off = int(code[pc][2])
            if reg[rr] % 2 == 0:
                pc += off
            else:
                pc += 1
        elif opc == 'jio':
            rr = code[pc][1]
            off = int(code[pc][2])
            if reg[rr] == 1:
                pc += off
            else:
                pc += 1
        else:
            print(f"Invalid instruction {opc}")
            break
    print(f"Program ended with pc = {pc} and {reg}")


if __name__ == '__main__':
    main()
