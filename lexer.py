import ply.lex as lex

tokens = ('NAME','EQUALS','NUMBER', 'PLUS', 'LPAREN','RPAREN')
t_PLUS = r'\+'
t_LPAREN =r'\('
t_RPAREN = r'\)'
t_EQUALS= r'\='
literals = [ '+','-','*','/' ]

# RE rule to track numbers, digits
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Define a rule so we can track line numbers
def t_newline(t):
     r'\n+'
     t.lexer.lineno += len(t.value)

 # A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

#RE rule to track all variable names
def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.value = t.value
    return t

 # Error handling rule
 #The t_error() function is used to handle lexing errors that occur when illegal characters are detected
error_occured = False
def t_error(t):
     global error_occured
     error_occured = True
     t.lexer.skip(1)

#variable that holds input data
data = ""
while True:
    text = input()
    if text == "#":
        break
    else:
        data +=text +'\n'
# Build the lexer
lexer = lex.lex()
 #Give the lexer user input
lexer.input(data)


def getType(tokType):
    if tokType == 'EQUALS':
        return '='
    elif tokType == 'PLUS':
        return '+'
    elif tokType == 'LPAREN':
        return '('
    elif tokType == 'RPAREN':
        return ')'
    else: return tok.type
# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    type = getType(tok.type)
    if error_occured:
        print('Illegal character \'', tok.value,'\'', sep='')
    else:
        print('(\'',type,'\'', sep='', end=', ')
        if not type == 'NUMBER':
            print ('\'', tok.value, '\'', sep='', end=', ')
        else:
            print (tok.value,  end=', ')
        print( tok.lineno, tok.lexpos, sep=', ', end=')\n')
    error_occured = False
    #print(tok)
