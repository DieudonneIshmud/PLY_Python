import ply.lex as lex

tokens = ("SYMBOL","COUNT")

t_SYMBOL = (
    r"C[laroudsemf]?|Os?|N[eaibdpos]?|S[icernbmg]?|P[drmtboau]?|"
    r"H[eofgas]?|A[lrsgutcm]|B[eraik]?|Dy|E[urs]|F[erm]?|G[aed]|"
    r"I[nr]?|Kr?|L[iaur]|M[gnodt]|R[buhenaf]|T[icebmalh]|"
    r"U|V|W|Xe|Yb?|Z[nr]"
)
def t_COUNT(t):
    r"\d+"
    t.value = int(t.value)
    return t

error_occured = False

def t_error(t):
    print("here")
    global error_occured
    error_occured = True
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

#beginning of the parser
import ply.yacc as yacc

count = 0

def p_expression_count(p):
    'expression : SYMBOL COUNT expression'
    global count
    count = count + p[2]

def p_expression_symbol(p):
    'expression : SYMBOL expression'
    global count
    count = count + 1

def p_expression_symbCount(p):
    'expression : '
    pass

# Error rule for syntax errors
def p_error(p):
    global error_occured
    error_occured = True


parser = yacc.yacc(debug=False,errorlog=yacc.NullLogger())

def main():
    #getting user input
    data = []
    global count, error_occured
    while True:
        text = input()
        if text == "#":
            break
        else:
            data.append(text)

    for item in data:
        count = 0
        #Give the lexer user input
        parser.parse(item)
        if error_occured:
            print("Error in formula")
        else: print (count)
        error_occured = False
        
if __name__ == "__main__":
    main()