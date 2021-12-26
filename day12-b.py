import sys
import ply.lex as lex
import ply.yacc as yacc


lexer, parser = None, None

###  Tokenizer  ###
tokens = (
    'LCURLY', 'RCURLY',
    'LSQUARE', 'RSQUARE',
    'COLON', 'COMMA',
    'QUOTE', 'MINUS',
    'NUMBER',
    'NAME'
)

t_LCURLY, t_RCURLY = r'\{', r'\}'
t_LSQUARE, t_RSQUARE = r'\[', r'\]'
t_COLON, t_COMMA = r'\:', r'\,'
t_QUOTE, t_MINUS = r'\"', r'\-'
t_NAME = r'\w+'


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)


###  Parser  ###
def p_elem(p):
    '''elem : list
            | dict
            | number
            | name'''
    p[0] = p[1]

def p_empty(p):
    '''empty :'''
    p[0] = 0

def p_number(p):
    '''number : MINUS NUMBER
              | NUMBER'''
    if p[1] == '-':
        p[0] = -p[2]
    else:
        p[0] = p[1]

def p_name(p):
    '''name : QUOTE NAME QUOTE'''
    if p[2] == 'red':
        p[0] = -999
    else:
        p[0] = 0

def p_list(p):
    '''list : LSQUARE list_elem RSQUARE'''
    p[0] = p[2]

def p_list_elem(p):
    '''list_elem : empty
                 | elem
                 | elem COMMA list_elem'''
    if len(p) < 3:
        if p[1] == -999:
            p[0] = 0
        else:
            p[0] = p[1]
    else:
        if p[1] == -999 and p[3] == -999:
            p[0] = 0
        elif p[1] != -999 and p[3] == -999:
            p[0] = p[1]
        elif p[1] == -999 and p[3] != -999:
            p[0] = p[3]
        else:
            p[0] = p[1] + p[3]

def p_dict(p):
    '''dict : LCURLY dict_list RCURLY'''
    if p[2] == -999:
        p[0] = 0
    else:
        p[0] = p[2]

def p_dict_list(p):
    '''dict_list : empty
                 | dict_elem
                 | dict_elem COMMA dict_list'''
    if len(p) < 3:
        p[0] = p[1]
    else:
        if p[1] == -999 or p[3] == -999:
            p[0] = -999
        else:
            p[0] = p[1] + p[3]

def p_dict_elem(p):
    '''dict_elem : name COLON elem'''
    if p[1] == -999 or p[3] == -999:
        p[0] = -999
    else:
        p[0] = p[3]

def p_error(p):
    if p:
        print("Syntax error at token", p.type)
        # Just discard the token and tell the parser it's okay.
        parser.errok()
    else:
        print("Syntax error at EOF")


###  Main  ###
def parse_line(tmp):
    global lexer, parser
    # lexer.input(tmp)
    # for tok in lexer:
    #     print(tok)
    result = parser.parse(tmp)
    return result


def main():
    global lexer, parser
    if len(sys.argv) != 2:
        sys.exit("Please provide a file name for input data")

    file_sum = 0
    lexer = lex.lex()
    parser = yacc.yacc()
    filename = sys.argv[1]
    with open(filename, "r") as inputfile:
        while True:
            line = inputfile.readline()
            if not line:
                break
            tmp = line.strip()
            line_sum = parse_line(tmp)
            print(f"{tmp} -> {line_sum}")
            file_sum += line_sum
    print(f"File sum = {file_sum}")


if __name__ == '__main__':
    main()
