from advent import Advent, Runner, File_to_String
import ply.lex as lex
import ply.yacc as yacc
import re
import sys

parser = None

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


class Day12(Advent):
    def __init__(self, input_text):
        global parser
        self.name = "12"
        self.lexer = lex.lex()
        self.parser = yacc.yacc()
        parser = self.parser
        self.lines = input_text

    def parse(self):
        pass

    def partA(self):
        file_sum = 0
        for line in self.lines:
            tmp = line.strip()
            numbers = re.findall("-?\d+", tmp)
            line_sum = 0
            for num in numbers:
                line_sum += int(num)
            # print(f"{tmp} -> {line_sum}")
            file_sum += line_sum
        print(f"File sum = {file_sum}")
        return file_sum

    def partB(self):
        file_sum = 0
        for line in self.lines:
            tmp = line.strip()
            foo = self.parser.parse(tmp, lexer=self.lexer)
            if foo is None:
                line_sum = 0
            else:
                line_sum = foo
            # print(f"{tmp} -> {line_sum}")
            file_sum += line_sum
        print(f"File sum = {file_sum}")
        return file_sum


def main():
    aoc1 = Day12(File_to_String("day12-live.txt"))
    runner = Runner(aoc1)
    runner.run()


if __name__ == '__main__':
    main()
