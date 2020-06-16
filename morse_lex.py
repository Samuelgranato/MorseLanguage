# ------------------------------------------------------------
# calclex.py
#
# tokenizer for a simple expression evaluator for
# numbers and +,-,*,/
# lex.py TEMPLATE FROM : https://www.dabeaz.com/ply/ply.html#ply_nn34
# ------------------------------------------------------------
import ply.lex as lex

tokens_value={
'.-'      : 'A', #morse table
'-...'    : 'B',
'-.-.'    : 'C',
'-..'     : 'D',
'.'       : 'E',
'..-.'    : 'F',
'--.'     : 'G',
'....'    : 'H',
'..'      : 'I',
'.---'    : 'J',
'-.-'     : 'K',
'.-..'    : 'L',
'--'      : 'M',
'-.'      : 'N',
'---'     : 'O',
'.--.'    : 'P',
'--.-'    : 'Q',
'.-.'     : 'R',
'...'     : 'S',
'-'       : 'T',
'..-'     : 'U',
'...-'    : 'V',
'.--'     : 'W',
'-..-'    : 'X',
'-.--'    : 'Y',
'--..'    : 'Z',

'-----'   : '0', #Numbers
'.----'   : '1',
'..---'   : '2',
'...--'   : '3',
'....-'   : '4',
'.....'   : '5',
'-....'   : '6',
'--...'   : '7',
'---..'   : '8',
'----.'   : '9',

'.-.-.-'  : '.', # Punctuation
'--..--'  : ',',
'..--..'  : '?',
'.----.'  : '\'',
'-.-.--'  : '!',
'-..-.'   : '/',
'-.--.'   : '(',
'-.--.-'  : ')',
'.-...'   : '&',
'---...'  : ':',
'-.-.-.'  : ';',
'-...-'   : '=',
'.-.-.'   : '+',
'-....-'  : '-',
'..--.-'  : '_',
'.-..-.'  : '"',
'...-..'  : '$',
'.--.-.'  : '@',
'..-.-'   : '¿',
'--...-'  : '¡'

}

# List of token names.   This is always required
reserved = {
    '.. ..-.' : 'IF',
    '. .-.. ... .' : 'ELSE',
    '.-- .... .. .-.. .' : 'WHILE',
    '. -.-. .... ---' : 'ECHO',
    '.-. . .- -.. .-.. .. -. . -.--. -.--.-' : 'READLINE',
    '--. .-. . .- - . .-.' : 'GREATER',
    '.-.. . ... ...' : 'LESS',
    '-.-. --- -. -.-. .- -' : 'CONCAT',
    '-- ..- .-.. -' : 'MULT',
    '--- .--. . -. .--. .-. --- --. .-. .- --' : 'OPEN_PROGRAM',
    '-.-. .-.. --- ... . .--. .-. --- --. .-. .- --' : 'CLOSE_PROGRAM',
    '--- .--. . -. -... .-.. --- -.-. -.-' : 'OPEN_BLOCK',
    '-.-. .-.. --- ... . -... .-.. --- -.-. -.-' : 'CLOSE_BLOCK',
    '- .-. ..- .' : 'TRUE',
    '..-. .- .-.. ... .' : 'FALSE',
    '..-. ..- -. -.-. - .. --- -.' : 'FUNCDEC',
    '.-. . - ..- .-. -.' : 'RETURN',

 }
 

tokens = [
    'INT',
    'PLUS',
    'MINUS',
    'DIV',
    'OPEN_PARENTHESES',
    'CLOSE_PARENTHESES',
    'ASSIGNMENT',
    'SEMI_COLLON',
    'OR',
    'AND',
    'NOT',
    'EQUALS',
    'NOTEQUALS',
    'STRING',
    'FUNCTION',
    'IDENTIFIER',
    'ID'] + list(reserved.values())



 # Regular expression rules for simple tokens
t_PLUS              = r'\.\-\.\-\.'
t_MINUS             = r'\-\.\.\.\.\-'
t_MULT              = r'\-\- \.\-\.\.'
t_DIV               = r'\-\.\.\-\.'
t_OPEN_PARENTHESES  = r'\-\.\-\-\.'
t_CLOSE_PARENTHESES = r'\-\.\-\-\.\-'
t_ASSIGNMENT        = r'\-\.\.\.\-'
t_SEMI_COLLON       = r'\-\-\-\.\.\.'
t_AND               = r'\.\-\.\.\.\ \.\-\.\.\.'
t_OR                = r'\.\-\-\.\ \.\-\-\.'
t_NOT               = r'\-\.\-\.\-\-'
t_EQUALS            = r'\-\.\.\.\-\ +\-\.\.\.\-'
t_NOTEQUALS         = r'\-\.\-\.\-\-\ +\-\.\.\.\-'
# t_CONCAT            = r'\-\.\-\.\ \-\-\-\ \-\.\ \-\.\-\.\ \.\-\ \-'


 
def t_ID(t):
    r'''((\.\-
    |\-\.\.\.
    |\-\.\-\.
    |\-\.\.
    |\.
    |\.\.\-\.
    |\-\-\.
    |\.\.\.\.
    |\.\.
    |\.\-\-\-
    |\-\.\-
    |\.\-\.\.
    |\-\-
    |\-\.
    |\-\-\-
    |\.\-\-\.
    |\-\-\.\-
    |\.\-\.
    |\.\.\.
    |\-
    |\.\.\-
    |\.\.\.\-
    |\.\-\-
    |\-\.\.\-
    |\-\.\-\-
    |\-\-\.\.)\ )+'''

    t.type = reserved.get(t.value.strip(),'ID')    # Check for reserved words

    if t.type == "ID":
        value = ''
        if ' ' in t.value:
            for tok in t.value.split(' '):
                if tok != '':
                    value += tokens_value[tok]
            t.value = value
        else:
            t.value = tokens_value[t.value] 
        t.type = "FUNCTION"
    return t


# A regular expression rule with some action code
def t_INT(t):
    r'''
    ((\-\-\-\-\-
    |\.\-\-\-\-
    |\.\.\-\-\-
    |\.\.\.\-\-
    |\.\.\.\.\-
    |\.\.\.\.\.
    |\-\.\.\.\.
    |\-\-\.\.\.
    |\-\-\-\.\.
    |\-\-\-\-\.)\ )+ '''

    #traducao do valor
    value = ''
    if ' ' in t.value:
        for tok in t.value.split(' '):
            if tok != '':
                value += tokens_value[tok]
        t.value = int(value)
    else:
        t.value = int(tokens_value[t.value])    
    return t

def t_STRING(t):
    r'''\.\-\.\.\-\.\ ((\.\-
    |\-\.\.\.
    |\-\.\-\.
    |\-\.\.
    |\.
    |\.\.\-\.
    |\-\-\.
    |\.\.\.\.
    |\.\.
    |\.\-\-\-
    |\-\.\-
    |\.\-\.\.
    |\-\-
    |\-\.
    |\-\-\-
    |\.\-\-\.
    |\-\-\.\-
    |\.\-\.
    |\.\.\.
    |\-
    |\.\.\-
    |\.\.\.\-
    |\.\-\-
    |\-\.\.\-
    |\-\.\-\-
    |\-\-\.\.
    |\-\-\-\-\-
    |\.\-\-\-\-
    |\.\.\-\-\-
    |\.\.\.\-\-
    |\.\.\.\.\-
    |\.\.\.\.\.
    |\-\.\.\.\.
    |\-\-\.\.\.
    |\-\-\-\.\.
    |\-\-\-\-\.)
    \ )+\.\-\.\.\-\. '''

    #traducao do valor
    value = ''
    if ' ' in t.value:
        for tok in t.value.split(' '):
            if tok != '':
                value += tokens_value[tok]
        t.value = value
    else:
        t.value = tokens_value[t.value] 
    

    return t

def t_IDENTIFIER(t):
    r'''\.\-\-\.\-\.\ (\.\-
    |\-\.\.\.
    |\-\.\-\.
    |\-\.\.
    |\.
    |\.\.\-\.
    |\-\-\.
    |\.\.\.\.
    |\.\.
    |\.\-\-\-
    |\-\.\-
    |\.\-\.\.
    |\-\-
    |\-\.
    |\-\-\-
    |\.\-\-\.
    |\-\-\.\-
    |\.\-\.
    |\.\.\.
    |\-
    |\.\.\-
    |\.\.\.\-
    |\.\-\-
    |\-\.\.\-
    |\-\.\-\-
    |\-\-\.\.)
    \ ((\.\-
    |\-\.\.\.
    |\-\.\-\.
    |\-\.\.|\.
    |\.\.\-\.
    |\-\-\.
    |\.\.\.\.
    |\.\.
    |\.\-\-\-
    |\-\.\-
    |\.\-\.\.
    |\-\-|\-\.
    |\-\-\-
    |\.\-\-\.
    |\-\-\.\-
    |\.\-\.
    |\.\.\.
    |\-
    |\.\.\-
    |\.\.\.\-
    |\.\-\-
    |\-\.\.\-
    |\-\.\-\-
    |\-\-\.\.
    |\-\-\-\-\-
    |\.\-\-\-\-
    |\.\.\-\-\-
    |\.\.\.\-\-
    |\.\.\.\.\-
    |\.\.\.\.\.
    |\-\.\.\.\.
    |\-\-\.\.\.
    |\-\-\-\.\.
    |\-\-\-\-\.)\ )* '''

    #traducao do valor
    value = ''
    if ' ' in t.value:
        for tok in t.value.split(' '):
            if tok != '':
                value += tokens_value[tok]
        t.value = value
    else:
        t.value = tokens_value[t.value] 
    

    return t
    
# def t_FUNCTION(t):
#     r'''\-\.\-\.\-\-((\.\-
#     |\-\.\.\.
#     |\-\.\-\.
#     |\-\.\.|\.
#     |\.\.\-\.
#     |\-\-\.
#     |\.\.\.\.
#     |\.\.
#     |\.\-\-\-
#     |\-\.\-
#     |\.\-\.\.
#     |\-\-|\-\.
#     |\-\-\-
#     |\.\-\-\.
#     |\-\-\.\-
#     |\.\-\.
#     |\.\.\.
#     |\-
#     |\.\.\-
#     |\.\.\.\-
#     |\.\-\-
#     |\-\.\.\-
#     |\-\.\-\-
#     |\-\-\.\.)
#     \ )+ '''

#     #traducao do valor
#     value = ''
#     if ' ' in t.value:
#         for tok in t.value.split(' '):
#             if tok != '':
#                 value += tokens_value[tok]
#         t.value = value
#     else:
#         t.value = tokens_value[t.value] 
    

#     return t

    
#     #traducao do valor
#     value = ''
#     if ' ' in t.value:
#         for tok in t.value.split(' '):
#             if tok != '':
#                 value += tokens_value[tok]
#         t.value = value
#     else:
#         t.value = tokens_value[t.value] 
    

#     return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = '/ \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)



def getTokens(data):
    toks = []
    # Build the lexer
    lexer = lex.lex()

    # Give the lexer some input
    lexer.input(data)

    # Tokenize
    while True:
        tok = lexer.token()
        if not tok: 
            break      # No more input
        toks.append(tok)

    return toks


# sourcefile = open('input_morse.php', 'r') 
# data = sourcefile.read() 
# if data[-1] != ' ':
#     data += ' '
# sourcefile.close()


# tks = getTokens(data)

# for t in tks:
#     print(t)