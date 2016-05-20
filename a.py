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
RIGHT_PAREN =26
COLON =200
MOD =27


#global
charClass = "UNKNOWN"



def getChar():
        c = f.read(1)
        print c
        if not c:
          charClass = EOF

        if (c.isalpha()):
            charClass = LETTER
        elif (c.isdigit()):
            charClass = DIGIT
        else:
            charClass = UNKNOWN

def addChar():
    if (lexLen <= 98):
        lexLen+=1
        lexeme[lexLen] = nextChar
        lexeme[lexLen] = 0
    else:
        print "Error - lexeme is too long!"

def lookup(ch):
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
            nextToken = DIV_OP
            break
        if case(';'):
            addChar()
            nextToken = COLON
            break
        if case('='):
            addChar()
            nextToken = ASSIGN_OP
            break
        if case('\n'):
            addChar()
            nextToken = EOL
            lexeme[0] = 'E'
            lexeme[1] = 'O'
            lexeme[2] = 'L'
            lexeme[3] = 0
            break
        else:
            addChar()
            nextToken = EOF
            break
        break
    return nextToken

def getNoneBlank():
    while (nextChar==' ' or nextChar=='\v' or nextChar=='\t' or nextChar=='\f' or nextChar=='\r'):
        getChar()

def lex():
    lexLen = 0
    getNoneBlank()
    while switch(charClass):
        if case(LETTER):
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
            lexeme[0] = 'E'
            lexeme[1] = 'O'
            lexeme[2] = 'L'
            lexeme[3] = 0
            break
        print nextToken
        break
    if (nextToken==EOL):
        a = -1
    else:
        a = nextToken
    if (c==0):
        print "Next token is: %(a), Next lexeme is %(lexeme)\n"
    return nextToken

    
f = open("a.txt", 'r')
getChar()
while (nextToken!=EOF):
    lex()




        

