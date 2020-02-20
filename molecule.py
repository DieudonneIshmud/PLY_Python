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
    print("Illegal character '%s'" % t.value[0])
    global error_occured
    error_occured = True
    t.lexer.skip(1)

        
# Build the lexer
lexer = lex.lex()

def main():
    #getting user input
    data = []
    global error_occured
    print("Input from keyboard:")
    while True:
        text = input()
        if text == "#":
            break
        else:
            data.append(text)

    for item in data:
        print("processing ", item)
        #Give the lexer user input
        lexer.input(item)
        sum = 0
        for tok in iter(lex.token, None):
            if error_occured: break
            sum = sum + repr(tok.value)
        if error_occured:
            print("Error in formula")
        else: print (sum)
        error_occured = False
        
if __name__ == "__main__":
    main()