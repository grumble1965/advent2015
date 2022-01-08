import sys
import queue
import ply.lex as lex
import ply.yacc as yacc

lexer, parser = None, None

#  Tokenizer  #
tokens = (
    'O_TOKEN', 'H_TOKEN'
)

t_O_TOKEN = r'O'
t_H_TOKEN = r'H'


def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)


#   Parser   #
def p_e(p):
    ''' e : h_rule
          | o_rule'''
    p[0] = 1 + p[1]


def p_h_rule(p):
    ''' h_rule : H_TOKEN
               | h_rule o_rule
               | o_rule h_rule'''
    if len(p) < 3:
        p[0] = 1
    else:
        p[0] = p[1] + p[2]


def p_o_rule(p):
    ''' o_rule : O_TOKEN
               | h_rule h_rule'''
    if len(p) < 3:
        p[0] = 1
    else:
        p[0] = p[1] + p[2]


def p_error(p):
    if p:
        print("Syntax error at token", p.type)
        # Just discard the token and tell the parser it's okay.
        parser.errok()
    else:
        print("Syntax error at EOF")


#   Main   #
def parse_molecule(molecule_str):
    global lexer, parser
    # lexer.input(molecule_str)
    # for tok in lexer:
    #     print(tok)
    res = parser.parse(molecule_str)
    print(res)
    return res


def main():
    global lexer, parser
    if len(sys.argv) != 2:
        sys.exit("Please provide a file name for input data")

    lexer = lex.lex()
    parser = yacc.yacc()

    filename = sys.argv[1]
    rules = []
    goal = None
    with open(filename, "r") as inputfile:
        while True:
            line = inputfile.readline()
            if not line:
                break
            tmp = line.strip()
            # print(f"{tmp}")
            if tmp != '' and tmp.find('=>') == -1:
                goal = tmp
            elif tmp.find('=>') >= 0:
                words = tmp.split('=>')
                lhs = words[0].strip()
                rhs = words[1].strip()
                tt = (lhs, rhs)
                rules.append(tt)

    # print(f"goal is {len(goal)} long")
    # longest_rhs = [len(rhs) for lhs, rhs in rules]
    #
    # longest_rhs.sort(reverse=True)
    #
    # print(len(rules), rules)
    #
    # ss = sorted(rules, key=lambda rr: len(rr[1]), reverse=True)
    # print(len(ss), ss)

    parse_molecule(goal)
    exit()

    sorted_rules = []
    for ll in longest_rhs:
        for rule in [(lhs, rhs) for lhs, rhs in rules if len(rhs) == ll]:
            sorted_rules.append(rule)
    print(f"{len(sorted_rules)} {sorted_rules}")

    exit()

    # for lhs, rhs in sorted_rules:
    #     matches = find_matches(rhs, goal)
    #     if matches:
    #         print(f"{lhs}->{rhs}  {matches}")
    #         break

    start, goal = goal, 'e'
    print(f"Starting with {start}, goal is {goal}")
    print(f"{rules}")

    q = queue.PriorityQueue()
    q.put((len(start), start, 0))

    solutions = []
    seen = set()
    ctr = 0
    while not q.empty():
        if ctr % 1000 == 0:
            print(f"Queue has {q.qsize()}, Seen has {len(seen)}, Solutions has {len(solutions)}")
        ctr += 1
        (_, target, steps) = q.get()
        # print("  ", target, steps)
        if target == goal:
            solutions.append(steps)
        # elif target in seen:
        #     pass
        else:
            seen.add(target)
            for lhs, rhs in sorted_rules:
                mm = find_matches(rhs, target)
                for idx in mm:
                    new_str = target[:idx] + lhs + target[idx + len(rhs):]
                    if new_str not in seen:
                        tt = (len(new_str), new_str, steps + 1)
                        q.put(tt)

    solutions.sort()
    print(f"best solutions were {solutions[:3]} steps")


def find_matches(rhs, target):
    matches = []
    idx = 0
    while True:
        next = target.find(rhs, idx)
        if next == -1:
            break
        matches.append(idx)
        idx = next + 1
    return matches


if __name__ == '__main__':
    main()
