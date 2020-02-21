import ply.yacc as yacc

from lexer import tokens

names = {}
#error_occured = False
# Error rule for syntax errors
def p_error(p):
    print("Error in input")


def p_expression_plus(p):
    'expression : expression PLUS NAME'
    p[0] = p[1] + p[3]
#def p_expression_plus_expression(p):
    #'expression : expression PLUS expression'
    #p[0] = p[1] + p[3]

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
        #print("Error in input")
        p[0] = 0
        #global error_occured
        #error_occured = True
      
    #global error_occured
    #error_occured = True
    
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
        result =parser.parse(s)
        #print(result)
        # if not result:
        #     print('Error in NOOO')
        # else:
        #     print('Accepted')

if __name__ == '__main__':
    main()

