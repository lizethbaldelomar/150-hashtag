#switch
class switch(object):
    value = None
    def __new__(class_, value):
        class_.value = value
        return True

def case(*args):
    return any((arg == switch.value for arg in args))

nextChar = 'a'
nextToken = 0
lexLen = 0
token = 0
a = 0
b = 0
c = 0
lexeme = []
charClass = "UNKNOWN"
#constant
LETTER =0
DIGIT =1
UNKNOWN =99
EOL =-2
EOF = -1
INT_LIT =10
IDENT =11
ASSIGN_OP =20
ADD_OP =21
SUB_OP =22
MULT_OP =23
DIV_OP =24
LEFT_PAREN =25
RIGHT_PAREN = 26
MOD = 27
COLON = 200

LEFT_BRACKET = 28
RIGHT_BRACKET = 29


#global

def getChar():
        global charClass
        global nextChar
        global nextToken
        global lexLen
        global token
        global a
        global b
        global c
        #print "pasok getChar"
        nextChar = f.read(1)
        #print nextChar
        if not nextChar:
            #print "hello"
            charClass = EOF
            #nextToken = EOF
            lexeme = []
            lexeme.append("EOF")
        if (nextChar.isalpha()):
            charClass = LETTER
        elif (nextChar.isdigit()):
            charClass = DIGIT
        else:
            charClass = UNKNOWN

def addChar():
    global charClass
    global nextChar
    global nextToken
    global lexLen
    global token
    global a
    global b
    global c
    global lexeme
    #print "pasok addChar"
    lexeme.append(nextChar)
    #print lexeme

def lookup(ch):
    global charClass
    global nextChar
    global nextToken
    global lexLen
    global token
    global a
    global b
    global c
    #print "lookup"
    while switch(ch):
        if case('('):
            addChar()
            nextToken = LEFT_PAREN
            break
        if case(')'):
            addChar()
            nextToken = RIGHT_PAREN
            break
        if case('+'):
            addChar()
            nextToken = ADD_OP
            break
        if case('-'):
            addChar()
            nextToken = SUB_OP
            break
        if case('*'):
            addChar()
            nextToken = MULT_OP
            break
        if case('/'):
            addChar()
            nextToken = DIV_OP
            break
        if case('%'):
            addChar()
            nextToken = MOD
            break
        if case(';'):
            addChar()
            nextToken = COLON
            break
        if case('='):
            addChar()
            nextToken = ASSIGN_OP
            break

        # implementation of own syntax

        if case('#{'):
            addChar()
            nextToken = LEFT_BRACKET
            break

        if case('}'):
            addChar()
            nextToken = RIGHT_BRACKET    
            break    

        if case('!='):
            addChar()
            nextToken = NOT_EQ
            break

        if case('>'):
            addChar()
            nextToken = LEFT_BRACKET
            break

        if case('<'):
            addChar()
            nextToken = LEFT_BRACKET
            break

        if case('>='):
            addChar()
            nextToken = LEFT_BRACKET
            break

        if case('<='):
            addChar()
            nextToken = LEFT_BRACKET
            break

        if case('=='):
            addChar()
            nextToken = EQUAL
            break

        if case('++'):
            addChar()
            nextToken = LEFT_BRACKET
            break

        if case('--'):
            addChar()
            nextToken = LEFT_BRACKET
            break

        if case('.'):
            addChar()
            nextToken = LEFT_BRACKET
            break

        if case('@int'):
            addChar()
            nextToken = LEFT_BRACKET
            break

        if case('@float'):
            addChar()
            nextToken = LEFT_BRACKET
            break

        if case('#if'):
            addChar()
            nextToken = LEFT_BRACKET
            break

        if case('#print'):
            addChar()
            nextToken = LEFT_BRACKET
            break

        if case('#read'):
            addChar()
            nextToken = LEFT_BRACKET
            break

        if case('#for'):
            addChar()
            nextToken = LEFT_BRACKET
            break

        if case('#end'):
            addChar()
            nextToken = LEFT_BRACKET
            break

        if case('!'):
            addChar()
            nextToken = LEFT_BRACKET
            break
            
        # end

        if case('\n'):
            addChar()
            nextToken = EOL
            lexeme = []
            lexeme.append("EOL")
            break
        else:
            addChar()
            nextToken = EOF
            break
        break
    return nextToken

def getNoneBlank():
    global charClass
    global nextChar
    global nextToken
    global lexLen
    global token
    global a
    global b
    global c
    while (nextChar==' ' or nextChar=='\v' or nextChar=='\t' or nextChar=='\f' or nextChar=='\r'):
        getChar()

def lex():
    global charClass
    global nextChar
    global nextToken
    global lexLen
    global token
    global a
    global b
    global c
    global lexeme
    #print "pasok lex"
    global nextToken
    lexLen = 0
    getNoneBlank()
    while switch(charClass):
        if case(LETTER):
            #print "letter"
            addChar()
            getChar()
            while (charClass == LETTER or charClass == DIGIT):
                addChar()
                getChar()
            nextToken = IDENT
            break
        if case(DIGIT):
            addChar()
            getChar()
            while (charClass == DIGIT):
                addChar()
                getChar()
            nextToken = INT_LIT
            break
        if case(UNKNOWN):
            lookup(nextChar)
            getChar()
            break
        if case(EOF):
            nextToken = EOF
            lexeme.append("EOL")
            break
        print nextToken
        break
    if (nextToken==EOL):
        a = -1
    else:
        a = nextToken
    if (c==0):
        print "Next token is: %(",a,"), Next lexeme is %(",lexeme,")\n"
    lexeme = []
    return nextToken

def A():
    global charClass
    global nextChar
    global nextToken
    global lexLen
    global token
    global a
    global b
    global c
    global lexeme
    print "A"
    while (nextToken==IDENT):
        lex()
    if (nextToken==ASSIGN_OP):
        while (nextToken!=COLON):
            print nextToken
            if (nextToken==EOL or nextToken==EOF):
                error()
                b=1
                break
            else:
                lex()
                expr()
        if (b==0):
            lex()
            if (nextToken!=EOL and nextToken!=EOF):
                error()
            else:
                print "exit A"
        b=0
    else:
        error()

def expr():
    global charClass
    global nextChar
    global nextToken
    global lexLen
    global token
    global a
    global b
    global c
    global lexeme
    print "expr"
    term()
    while (nextToken==ADD_OP or nextToken==SUB_OP):
        lex()
        term()
    print "exit expr"

def term():
    global charClass
    global nextChar
    global nextToken
    global lexLen
    global token
    global a
    global b
    global c
    global lexeme
    print "term"
    factor()
    while (nextToken==MULT_OP or nextToken==DIV_OP or nextToken==MOD):
        lex()
        factor()
    print "exit term"

def factor():
    global charClass
    global nextChar
    global nextToken
    global lexLen
    global token
    global a
    global b
    global c
    global lexeme
    print "factor"
    if (nextToken==IDENT or nextToken==INT_LIT):
        lex()
    else:
        if (nextToken==LEFT_PAREN):
            lex()
            expr()
            if (nextToken==RIGHT_PAREN):
                lex()
            else:
                error()
        else:
            error()
    print "exit factor"
    
def error():
    global charClass
    global nextChar
    global nextToken
    global lexLen
    global token
    global a
    global b
    global c
    global lexeme
    print "Syntax Error!"
    if (nextToken!=EOL and nextToken!=EOF):
        while (nextToken!=EOL and nextToken!=EOF):
            nextChar = f.read(1)
            if (nextChar == '\n'):
                nextToken = EOL
                c = 1
                lex()
                c = 0
                break
            elif (nextChar == EOF):
                nextToken = EOF
                break
            







        
    
f = open("a.txt", 'r')
getChar()
while(nextToken!=EOF):
    lex()
    A()
