import ply.yacc as yacc

from lexer import tokens


names = {}
error_occured = False


def p_expression_plus(p):
    'expression : expression PLUS expression'
    p[0] = p[1] + p[3]

def p_expression_paren(p):
    'expression : LPAREN expression RPAREN'
    p[0] = (p[1])
    
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
        global error_occured
        error_occured = True
        p[0] = 0
  
    
# Error rule for syntax errors
def p_error(p):
    global error_occured
    error_occured = True
 
parser = yacc.yacc()

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
        result = parser.parse(s)
        if error_occured:
            break
    
    if error_occured:
        print('Error in input')
    else:
        print('Accepted')

if __name__ == '__main__':
    main()