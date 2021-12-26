import sys


def inc_letter(ch):
    table = {'a': 'b', 'b': 'c', 'c': 'd', 'd': 'e', 'e': 'f', 'f': 'g', 'g': 'h', 'h': 'j', 'i': 'j', 'j': 'k',
             'k': 'm', 'l': 'm', 'm': 'n', 'n': 'p', 'o': 'p', 'p': 'q', 'q': 'r', 'r': 's', 's': 't', 't': 'u',
             'u': 'v', 'v': 'w', 'w': 'x', 'x': 'y', 'y': 'z', 'z': 'a'}
    new_ch = table[ch]
    return (new_ch == 'a'), new_ch


def increment(password):
    p0, p1, p2, p3 = password[0], password[1], password[2], password[3]
    p4, p5, p6, p7 = password[4], password[5], password[6], password[7]

    carry, p7 = inc_letter(p7)
    if carry:
        carry, p6 = inc_letter(p6)
    if carry:
        carry, p5 = inc_letter(p5)
    if carry:
        carry, p4 = inc_letter(p4)
    if carry:
        carry, p3 = inc_letter(p3)
    if carry:
        carry, p2 = inc_letter(p2)
    if carry:
        carry, p1 = inc_letter(p1)
    if carry:
        carry, p0 = inc_letter(p0)

    return "".join([p0, p1, p2, p3, p4, p5, p6, p7])


def valid1(password):
    rule1 = ['abc', 'bcd', 'cde', 'def', 'efg', 'fgh',
             'pqr', 'qrs', 'rst', 'stu', 'tuv', 'uvw', 'vwx', 'wxy', 'xyz']

    if len([seq for seq in rule1 if seq in password]) > 0:
        return True
    else:
        # print("fails rule 1")
        return False


def valid2(password):
    if 'i' not in password and 'o' not in password and 'l' not in password:
        return True
    else:
        # print("fails rule 2")
        return False


def valid3(password):
    rule3 = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'jj', 'kk', 'mm',
             'nn', 'pp', 'qq', 'rr', 'ss', 'tt', 'uu', 'vv', 'ww', 'xx', 'yy', 'zz']

    if len([pair for pair in rule3 if pair in password]) > 1:
        return True
    else:
        # print("fails rule 3")
        return False


def valid(password):
    v1 = valid1(password)
    v2 = valid2(password)
    v3 = valid3(password)
    return len(password) == 8 and v1 and v2 and v3


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

            passwd = increment(tmp)
            # print(f"{tmp} -> {passwd}", end='')
            while not valid(passwd):
                # print(" bad")
                foo = increment(passwd)
                # print(f"{passwd} -> {foo}", end='')
                passwd = foo

            print(f" GOOD\nFrom {tmp}, new password is {passwd}")

            passwd = increment(passwd)
            # print(f"{tmp} -> {passwd}", end='')
            while not valid(passwd):
                # print(" bad")
                foo = increment(passwd)
                # print(f"{passwd} -> {foo}", end='')
                passwd = foo

            print(f" GOOD\nFrom {tmp}, 2nd new password is {passwd}")


if __name__ == '__main__':
    main()


