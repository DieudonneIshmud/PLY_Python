import ply.yacc as yacc

from lexer import tokens
import lexer

names = {}

def p_expression_plus(p):
    'expression : expression PLUS expression'
    p[0] = p[1] + p[3]

def p_expression_paren(p):
    'expression : LPAREN expression RPAREN'
    p[0] = (p[2])
    
def p_expression_equals(p):
    'expression : NAME EQUALS expression'
    names[p[1]] = p[3]
    p[1] = p[3]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

def p_expression_name(p):
    'expression : NAME'
    try:
        p[0] = names[p[1]]
    except LookupError:
        from lexer import error_occured
        lexer.error_occured = True
        p[0] = 0
  
    
# Error rule for syntax errors
def p_error(p):
    lexer.error_occured = True
 #the debug and errorlog arguments helps avoind warning, which cause problems with the automarker
parser = yacc.yacc(debug=False,errorlog=yacc.NullLogger())

x = []
def main():
    while (True):
        try:
            s = input()
        except EOFError:
            break
        if not s:
            continue
        if s == '#': 
            break
        x.append(s)
    for s in x:
        parser.parse(s)
        if lexer.error_occured: break
        #print(result)
    if lexer.error_occured:
        print('Error in input')
    else:
        print('Accepted')

if __name__ == '__main__':
    main()

