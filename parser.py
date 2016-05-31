import sys

#switch
class switch(object):
	value = None
	def __new__(class_, value):
		class_.value = value
		return True

def case(*args):
	return any((arg == switch.value for arg in args))

fprint= 0
LETTER = 0
DIGIT = 1
UNKNOWN = 99
EOL = -2
EOF = -1
INT_LIT = 10
VAR = 11
ASSIGN_OP = 20
ADD_OP = 21
SUB_OP = 22
MULT_OP = 23
DIV_OP = 24
MOD = 25
LEFT_PAREN = 26
RIGHT_PAREN = 27
LEFT_BRACKET = 28
RIGHT_BRACKET = 29
NOT_EQ = 30
GREATER_THAN = 31
LESS_THAN = 32
GT_EQ = 33
LT_EQ = 34
EQUAL = 35
ITER_PLUS = 36
ITER_MINUS = 37
FLOAT_PT = 38
DEC_INT = 39
DEC_FLOAT = 40
IF_COND = 41
ELIF_COND = 42
ELSE_COND = 43
PRINT_OUTPUT = 44
READ_INPUT = 45
FOR_COND = 46
CALL_FUNC = 47
END_DELIM = 48
COMMENT = 49
START_PROG = 50
END_PROG = 51
SEP_FUNC = 52
COMMA = 53
QUOTE = 54
COLON = 55
HASH = 56
DEC = 57
BRACKET = 58
SPECIAL = 59
ADD = 60
GREAT = 61
EQ = 62
MINUS = 63
EX = 64
LESS = 65
#global

def getChar():
		global charClass
		global g
		global f
		global line
		global tabs
		global nextChar
		global nextToken
		global lexLen
		global token
		global a
		global b
		global c
		global fprint
		nextChar = f.read(1)
		if not nextChar:
			charClass = EOF
			lexeme = []
			lexeme.append("EOF")
		if (nextChar.isalpha()):
			charClass = LETTER
		elif (nextChar.isdigit()):
			charClass = DIGIT
		elif (nextChar == "#"):
			charClass = HASH
		elif (nextChar == "@"):

			charClass = DEC
		elif (nextChar == "{"):
			charClass = BRACKET
		elif (nextChar == ">"):
			charClass = GREAT
		elif (nextChar == "<"):
			charClass = LESS
		elif (nextChar == "="):
			charClass = EQ
		elif (nextChar == "+"):
			charClass = ADD
		elif (nextChar == "-"):
			charClass = MINUS
		elif (nextChar == "!"):
			charClass = EX
		else:
			charClass = UNKNOWN

def addChar():
	global charClass
	global g
	global f
	global line
	global tabs
	global nextChar
	global nextToken
	global lexLen
	global token
	global a
	global b
	global c
	global lexeme
	global str3
	global fprint
	lexeme.append(nextChar)

def lookup(ch):
	global charClass
	global g
	global f
	global line
	global tabs
	global nextChar
	global nextToken
	global lexLen
	global token
	global a
	global b
	global c
	global fprint
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

		if case('}'):
			addChar()
			nextToken = RIGHT_BRACKET
			break    

		if case('.'):
			addChar()
			nextToken = FLOAT_PT
			break

		if case('?'):
			addChar()
			nextToken = COMMENT
			break

		if case(','):
			addChar()
			nextToken = COMMA
			break

		if case('"'):
			addChar()
			nextToken = QUOTE
			break

		if case(';'):
			addChar()
			nextToken = COLON
			break

		if case('\n'):
			addChar()
			line = line+1
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
	global g
	global f
	global line
	global tabs
	global nextChar
	global nextToken
	global lexLen
	global token
	global a
	global b
	global c
	global fprint
	while (nextChar==' ' or nextChar=='\v' or nextChar=='\t' or nextChar=='\f' or nextChar=='\r'):
		getChar()

def lex():
	global charClass
	global g
	global f
	global line
	global tabs
	global nextChar
	global nextToken
	global lexLen
	global token
	global a
	global b
	global c
	global lexeme
	global str3
	global fprint
	lexeme = []
	global nextToken
	lexLen = 0
	getNoneBlank()
	while switch(charClass):

		if case(LETTER):
			addChar()
			getChar()
			while (charClass == LETTER or charClass == DIGIT):
				addChar()
				getChar()
			nextToken = VAR
			break

		if case(DIGIT):
			addChar()
			getChar()
			while (charClass == DIGIT):
				addChar()
				getChar()
			nextToken = INT_LIT
			break

		if case(HASH):
			addChar()
			getChar()

			if (charClass == BRACKET):
				addChar()
				getChar()
				lexeme = ''.join(lexeme)
				nextToken = LEFT_BRACKET
			else:
				while (charClass == LETTER):
					addChar()
					getChar()

				str1 = "#startprogram"
				str2 = "#endprogram"
				str12 = "#if"
				str4 = "#elif"
				str5 = "#else"
				str6 = "#print"
				str7 = "#read"
				str8 = "#for"
				str9 = "#call"
				str10 = "#end"
				str11 = "#function"

				lexeme = ''.join(lexeme)
				if (lexeme == str1):
					nextToken = START_PROG
				elif(lexeme == str2):
					nextToken = END_PROG
				elif(lexeme == str12):
					nextToken = IF_COND
				elif(lexeme == str4):
					nextToken = ELIF_COND
				elif(lexeme == str5):
					nextToken = ELSE_COND
				elif(lexeme == str6):
					for num in range(0,tabs):
						g.write("\t")
					g.write("print ")
					nextToken = PRINT_OUTPUT
				elif(lexeme == str7):
					nextToken = READ_INPUT
				elif(lexeme == str8):
					nextToken = FOR_COND
				elif(lexeme == str9):
					nextToken = CALL_FUNC
				elif(lexeme == str10):
					nextToken = END_DELIM
				elif(lexeme == str11):
					nextToken = SEP_FUNC
				else:
					nextToken = UNKNOWN
				break

		if case(DEC):
			addChar()
			getChar()
			while (charClass == LETTER):
				addChar()
				getChar()

			str1 = "@int"
			str2 = "@float"
			lexeme = ''.join(lexeme)
			if (lexeme == str1):
				nextToken = DEC_INT
			elif(lexeme == str2):
				nextToken = DEC_FLOAT
			else:
				nextToken = UNKNOWN
			break

		if case(GREAT):
			addChar()
			getChar()
			if (charClass == EQ):
				addChar()
				getChar()
				lexeme = ''.join(lexeme)
				nextToken = GT_EQ
			else:
				nextToken = GREATER_THAN
			break

		if case(LESS):
			addChar()
			getChar()
			if (charClass == EQ):
				addChar()
				getChar()
				lexeme = ''.join(lexeme)
				nextToken = LT_EQ
			else:
				nextToken = LESS_THAN
			break

		if case(EQ):
			addChar()
			getChar()
			if (charClass == EQ):
				addChar()
				getChar()
				lexeme = ''.join(lexeme)
				nextToken = EQUAL
			else:
				nextToken = ASSIGN_OP
			break

		if case(EX):
			addChar()
			getChar()
			if (charClass == EQ):
				addChar()
				getChar()
				lexeme = ''.join(lexeme)
				nextToken = NOT_EQ
			else:
				nextToken = UNKNOWN
			break

		if case(ADD):
			addChar()
			getChar()
			if (charClass == ADD):
				addChar()
				getChar()
				lexeme = ''.join(lexeme)
				nextToken = ITER_PLUS
			else:
				nextToken = ADD_OP
			break

		if case(MINUS):
			addChar()
			getChar()
			if (charClass == MINUS):
				addChar()
				getChar()
				lexeme = ''.join(lexeme)
				nextToken = ITER_MINUS
			else:
				nextToken = SUB_OP
			break

		if case(UNKNOWN):
			lookup(nextChar)
			getChar()
			break

		if case(EOF):
			nextToken = EOF
			lexeme.append("EOL")
			break

		break
	return nextToken

def A():
	global charClass
	global g
	global f
	global line
	global tabs
	global nextChar
	global nextToken
	global lexLen
	global token
	global a
	global b
	global c
	global lexeme
	global str3
	global fprint
	for num in range(0,tabs):
		g.write("\t")
	while (nextToken==VAR):
		g.write(' '.join(map(str, lexeme)).replace(" ", ""))
		lex()
	if (nextToken==ASSIGN_OP):
		g.write(" = ")
		while (nextToken!=EOL and nextToken!=EOF):
			lex()
			expr2()
	else:
		deletecontent(g)
		g.write("print 'Syntax error. Expected ='")
		error()
	g.write("\n")

def expr():
	global charClass
	global g
	global f
	global tabs
	global nextChar
	global nextToken
	global lexLen
	global token
	global a
	global b
	global line
	global c
	global lexeme
	global str3
	global fprint
	str3 = []
	term()
	while (nextToken==ADD_OP or nextToken==SUB_OP):
		lexeme = ''.join(lexeme)
		str3.append(lexeme)
		lex()
		term()

def term():
	global charClass
	global g
	global f
	global tabs
	global nextChar
	global nextToken
	global lexLen
	global token
	global a
	global b
	global c
	global line
	global lexeme
	global str3
	global fprint
	factor()
	while (nextToken==MULT_OP or nextToken==DIV_OP or nextToken==MOD):
		lexeme = ''.join(lexeme)
		str3.append(lexeme)
		lex()
		factor()

def factor():
	global charClass
	global g
	global f
	global tabs
	global nextChar
	global nextToken
	global lexLen
	global token
	global a
	global b
	global c
	global line
	global lexeme
	global str3
	global fprint
	if (nextToken==VAR or nextToken==INT_LIT):
		lexeme = ''.join(lexeme)
		str3.append(lexeme)
		lex()
	else:
		if (nextToken==LEFT_PAREN):
			lexeme = ''.join(lexeme)
			str3.append(lexeme)
			lex()
			expr()
			if (nextToken==RIGHT_PAREN):
				lexeme = ''.join(lexeme)
				str3.append(lexeme)
				lex()
			else:
				deletecontent(g)
				g.write("print 'Syntax error. Expected )'")
				error()
		else:
			deletecontent(g)
			g.write("print 'Syntax error. Expected VAR, INT, or ('")
			error()

def expr2():
	global charClass
	global g
	global f
	global tabs
	global nextChar
	global nextToken
	global lexLen
	global token
	global a
	global b
	global c
	global line
	global lexeme
	global str3
	global fprint
	term2()
	while (nextToken==ADD_OP or nextToken==SUB_OP):
		g.write(' '.join(map(str, lexeme)).replace(" ", ""))
		lex()
		term2()

def term2():
	global charClass
	global g
	global f
	global tabs
	global nextChar
	global nextToken
	global lexLen
	global token
	global a
	global b
	global c
	global line
	global lexeme
	global str3
	global fprint
	factor2()
	while (nextToken==MULT_OP or nextToken==DIV_OP or nextToken==MOD):
		g.write(' '.join(map(str, lexeme)).replace(" ", ""))
		lex()
		factor2()

def factor2():
	global charClass
	global g
	global f
	global tabs
	global nextChar
	global nextToken
	global lexLen
	global token
	global a
	global b
	global c
	global line
	global lexeme
	global str3
	global fprint
	if (nextToken==VAR or nextToken==INT_LIT):
		g.write(' '.join(map(str, lexeme)).replace(" ", ""))
		lex()
	else:
		if (nextToken==LEFT_PAREN):
			lex()
			expr2()
			if (nextToken==RIGHT_PAREN):
				lex()
			else:
				deletecontent(g)
				g.write("print 'Syntax error. Expected )'")
				error()
		else:
			deletecontent(g)
			g.write("print 'Syntax error. Expected VAR, INT, or ('")
			error()
			
def program():
	global charClass
	global g
	global f
	global tabs
	global nextChar
	global nextToken
	global lexLen
	global token
	global a
	global b
	global c
	global line
	global lexeme
	global str3
	global fprint
	g.write("def main():\n")
	while (nextToken==START_PROG):
		lex()
	tabs = tabs + 1
	if (nextToken==EOL):
		while (nextToken!=END_PROG):
			if (nextToken==EOF):
				deletecontent(g)
				g.write("print 'Syntax error. Expected #endprogram'")
				error()
				b=1
				break
			lex() # \n
			block1()
		tabs = tabs-1
		if (b==0):
			lex() # endprog
			if (nextToken!=EOF):
				outsideprog()
		b=0
	else:
		deletecontent(g)
		g.write("print 'Syntax error. Expected EOL'")
		error()
	for num in range(0,tabs):
		g.write("\t")
	if (fprint !=1):
		g.write("\nmain()")

def outsideprog():
	global charClass
	global g
	global f
	global tabs
	global nextChar
	global nextToken
	global lexLen
	global token
	global a
	global b
	global c
	global line
	global lexeme
	global str3
	global fprint
	while (nextToken==SEP_FUNC):
		lex()
		func()
	if (nextToken==EOL or nextToken==EOF): #edit
		while (nextToken!=EOF):
			lex() # \n
			outsideprog()
	else:
		deletecontent(g)
		g.write("print 'Syntax error. Expected EOL or EOF'")
		error()

def func():
	global charClass
	global g
	global f
	global tabs
	global nextChar
	global nextToken
	global lexLen
	global token
	global a
	global b
	global c
	global line
	global lexeme
	global str3
	global fprint
	g.write("\ndef ")
	while (nextToken==SEP_FUNC):
		lex() # VAR
	if (nextToken==VAR):
		g.write(' '.join(map(str, lexeme)).replace(" ", ""))
		lex() # (
		if (nextToken==LEFT_PAREN):
			g.write("(")
			lex() # var or )
			param()
			if (nextToken==RIGHT_PAREN):
				g.write("):\n")
				tabs = tabs + 1
				lex() # EOL
				while (nextToken!=END_DELIM):
					lex()
					block1()
				tabs = tabs - 1
				lex()
			else: 
				deletecontent(g)
				g.write("print 'Syntax error. Expected )'")
				error()
		else:
			deletecontent(g) 
			g.write("print 'Syntax error. Expected ('")
			error()
	else: 
		deletecontent(g)
		g.write("print 'Syntax error. Expected VAR'")
		error()

def block1():
	global charClass
	global g
	global f
	global tabs
	global nextChar
	global nextToken
	global lexLen
	global token
	global line
	global fprint
	while (nextToken==DEC_INT or nextToken==DEC_FLOAT):
		declare()
	block()

def declare():
	global charClass
	global g
	global f
	global line
	global tabs
	global nextChar
	global nextToken
	global lexLen
	global token
	global a
	global b
	global c
	global lexeme
	global str3
	global fprint
	if (nextToken==DEC_INT):
		lex()
		if (nextToken==VAR):
			str0 = ''.join(lexeme)
			lex()
			if (nextToken==ASSIGN_OP):
				for num in range(0,tabs):
					g.write("\t")
				g.write(' '.join(map(str, str0)).replace(" ", ""))
				g.write("=")
				lex()
				if (nextToken==ADD_OP or nextToken==SUB_OP or nextToken==INT_LIT):
					constant()
					g.write("\n")
				else: 
					deletecontent(g)
					g.write("print 'Syntax error. Expected INT'")
					error()
			elif (nextToken==EOL):
				lex()
			else: 
				deletecontent(g)
				g.write("print 'Syntax error. Expected = or EOL'")
				error()
		else: 
			deletecontent(g)
			g.write("print 'Syntax error. Expected VAR'")
			error()
	elif (nextToken==DEC_FLOAT):
		lex()
		if (nextToken==VAR):
			str0 = ''.join(lexeme)
			lex()
			if (nextToken==ASSIGN_OP):
				for num in range(0,tabs):
					g.write("\t")
				g.write(' '.join(map(str, str0)).replace(" ", ""))
				g.write("=")
				lex()
				if (nextToken==ADD_OP or nextToken==SUB_OP or nextToken==INT_LIT):
					constant()
					if (nextToken==FLOAT_PT):
						g.write(".")
						lex()
						if (nextToken==INT_LIT):
							g.write(' '.join(map(str, lexeme)).replace(" ", ""))
							g.write("\n")
							lex()
							if (nextToken==EOL): lex()
							else:
								deletecontent(g) 
								g.write("print 'Syntax error. Expected EOL'")
								error()
						else: 
							deletecontent(g)
							g.write("print 'Syntax error. Expected FLOAT'")
							error()
					else: 
						deletecontent(g)
						g.write("print 'Syntax error. Expected .'")
						error()
				else: 
					deletecontent(g)
					g.write("print 'Syntax error. Expected FLOAT'")
					error()
			elif (nextToken==EOL):
				lex()
			else: 
				deletecontent(g)
				g.write("print 'Syntax error. Expected = or EOL'")
				error()
		else: 
			deletecontent(g)
			g.write("print 'Syntax error. Expected VAR'")
			error()
	else: 
		deletecontent(g)
		g.write("print 'Syntax error. Expected @int or @float'")
		error()

def constant():
	global charClass
	global g
	global f
	global tabs
	global nextChar
	global nextToken
	global lexLen
	global token
	global a
	global b
	global c
	global line
	global lexeme
	global str3
	global fprint
	if (nextToken==ADD_OP or nextToken==SUB_OP):
		g.write(' '.join(map(str, lexeme)).replace(" ", ""))
		lex()
	if (nextToken==INT_LIT):
		g.write(' '.join(map(str, lexeme)).replace(" ", ""))
		lex()
		if (nextToken==EOL):
			lex()

def param():
	global charClass
	global g
	global f
	global tabs
	global nextChar
	global nextToken
	global lexLen
	global token
	global a
	global b
	global c
	global line
	global lexeme
	global str3
	global fprint
	if (nextToken==VAR or nextToken==INT_LIT):
		g.write(' '.join(map(str, lexeme)).replace(" ", ""))
		lex() # COMMA OR )
		param1()

def param1():
	global charClass
	global g
	global f
	global tabs
	global nextChar
	global nextToken
	global lexLen
	global token
	global a
	global b
	global c
	global line
	global lexeme
	global str3
	global fprint
	if (nextToken==COMMA):
		g.write(", ")
		lex() # VAR/INT
		param()

def block():
	global charClass
	global g
	global f
	global tabs
	global nextChar
	global nextToken
	global lexLen
	global token
	global a
	global b
	global c
	global line
	global lexeme
	global str3
	global fprint
	while(nextToken==EOL):
		lex()
	if (nextToken==VAR or nextToken==PRINT_OUTPUT or nextToken==READ_INPUT or nextToken==FOR_COND or nextToken==IF_COND or nextToken==CALL_FUNC or nextToken==COMMENT):
		function()
		block()

def function():
	global charClass
	global g
	global f
	global tabs
	global nextChar
	global nextToken
	global lexLen
	global token
	global a
	global b
	global c
	global line
	global lexeme
	global str3
	global fprint
	if (nextToken==VAR):
		A()
	elif (nextToken==PRINT_OUTPUT):
		print_out()
	elif (nextToken==READ_INPUT):
		read_in()
	elif (nextToken==FOR_COND):
		for_cont()
	elif (nextToken==IF_COND):
		if_cont()
	elif (nextToken==CALL_FUNC):
		call_function()
	elif (nextToken==COMMENT):
		lex()
		comment_out()
	else: 
		deletecontent(g)
		g.write("print 'Syntax error. Expected VAR or FUNCTION'")
		error()

def print_out():
	global charClass
	global g
	global f
	global line
	global tabs
	global nextChar
	global nextToken
	global lexLen
	global token
	global a
	global b
	global c
	global lexeme
	global str3
	global fprint
	lex()	
	if (nextToken==QUOTE):
		strexpr()
		lex() # end
		if (nextToken==END_DELIM):
			lex()
			if (nextToken==EOL):
				lex()
			else:
				deletecontent(g) 
				g.write("print 'Syntax error. Expected EOL'")
				error()
		else: 
			deletecontent(g)
			g.write("print 'Syntax error. Expected #end'")
			error()
	else: 
		deletecontent(g)
		g.write("print 'Syntax error. Expected Quote'")
		error()

def read_in():
	global charClass
	global g
	global f
	global line
	global tabs
	global nextChar
	global nextToken
	global lexLen
	global token
	global a
	global b
	global c
	global lexeme
	global str3
	global fprint
	lex()
	if (nextToken==VAR):
		for num in range(0,tabs):
			g.write("\t")
		g.write(' '.join(map(str, lexeme)).replace(" ", ""))
		g.write(' = tkSimpleDialog.askinteger("Integer input", "Input an integer")')
		g.write('\n')
		for num in range(0,tabs):
			g.write("\t")
		g.write("sys.stdout.flush()\n")
		lex()
		if(nextToken==END_DELIM):
			lex()
			if (nextToken==EOL):
				lex()
			else: 
				deletecontent(g)
				g.write("print 'Syntax error. Expected EOL'")
				error()
		else: 
			deletecontent(g)
			g.write("print 'Syntax error. Expected #end'")
			error()
	else: 
		deletecontent(g)
		g.write("print 'Syntax error. Expected VAR'")
		error()

def strexpr():
	global charClass
	global g
	global f
	global line
	global tabs
	global nextChar
	global nextToken
	global lexLen
	global token
	global a
	global b
	global c
	global lexeme
	global str3
	global fprint
	
	lex()
	if (nextToken==LEFT_BRACKET):
		lex()
		if (nextToken==VAR):
			g.write(' '.join(map(str, lexeme)).replace(" ", ""))
			g.write('\n')	
			lex()
			if (nextToken==RIGHT_BRACKET):
				lex()
			else:
				deletecontent(g) 
				g.write("print 'Syntax error. Expected }'")
				error()
		else: 
			deletecontent(g)
			g.write("print 'Syntax error. Expected VAR'")
			error()
	else:
		if (nextToken!=COMMENT): g.write('"') 
		comment_out()

def comment_out():
	global charClass
	global g
	global f
	global line
	global tabs
	global nextChar
	global nextToken
	global lexLen
	global token
	global a
	global b
	global c
	global lexeme
	global str3
	global fprint
	while (nextToken==VAR or nextToken==INT_LIT):
		g.write(' '.join(map(str, lexeme)).replace(" ", ""))
		g.write(" ")
		lex()
		if (nextToken==QUOTE):
			break
		elif (nextToken==COMMENT):
			lex()
			if(nextToken==EOL):
				lex()
			else: 
				deletecontent(g)
				g.write("print 'Syntax error. Expected EOL'")
				error()
			break
	g.write('"')
	g.write("\n")

def call_function():
	global charClass
	global g
	global f
	global line
	global tabs
	global nextChar
	global nextToken
	global lexLen
	global token
	global a
	global b
	global c
	global lexeme
	global str3
	global fprint
	for num in range(0,tabs):
		g.write("\t")

	lex()
	if (nextToken==VAR):
		g.write(' '.join(map(str, lexeme)).replace(" ", ""))
		g.write("(")
		lex()
		if (nextToken==LEFT_PAREN):
			lex()
			param()
			if (nextToken==RIGHT_PAREN):
				g.write(")\n")
				lex()
				if (nextToken==END_DELIM):
					lex()
					if (nextToken==EOL):
						lex()
					else:
						deletecontent(g) 
						g.write("print 'Syntax error. Expected EOL'")
						error()
				else: 
					deletecontent(g)
					g.write("print 'Syntax error. Expected #end'")
					error()
			else:
				deletecontent(g) 
				g.write("print 'Syntax error. Expected )'")
				error()
		else: 
			deletecontent(g)
			g.write("print 'Syntax error. Expected ('")
			error()
	else: 
		deletecontent(g)
		g.write("print 'Syntax error. Expected VAR'")
		error()

def if_cont():
	global charClass
	global g
	global f
	global tabs
	global nextChar
	global nextToken
	global lexLen
	global token
	global a
	global b
	global c
	global line
	global lexeme
	global str3
	global fprint
	for num in range(0,tabs):
		g.write("\t")
	tabs = tabs + 1
	g.write("if (")

	lex()
	if (nextToken==LEFT_PAREN):
		lex()
		if (nextToken==VAR):
			expr2()
			if (nextToken==EQUAL or nextToken==NOT_EQ or nextToken==GREATER_THAN or nextToken==LESS_THAN or nextToken==GT_EQ or nextToken==LT_EQ):
				g.write(' '.join(map(str, lexeme)).replace(" ", ""))
				lex()
				if (nextToken==VAR or nextToken==INT_LIT):
					expr2()
					g.write("):\n")
				else:
					deletecontent(g) 
					g.write("print 'Syntax error. Expected VAR or INT'")
					error()
			else: 
				deletecontent(g)
				g.write("print 'Syntax error. Expected == , != , > , < , >= or <= '")
				error()
		else: 
			deletecontent(g)
			g.write("print 'Syntax error. Expected VAR'")
			error()
		if (nextToken==RIGHT_PAREN):
			lex()
			if (nextToken==EOL):
				lex()
				block()
				if (nextToken==ELIF_COND):
					elif_cont()
				if (nextToken==ELSE_COND):
					else_cont()
				if (nextToken==END_DELIM):
					tabs = tabs - 1
					lex()
					if (nextToken==EOL):
						lex()
					else:
						deletecontent(g) 
						g.write("print 'Syntax error. Expected EOL'")
						error()
			else: 
				deletecontent(g)
				g.write("print 'Syntax error. Expected EOL'")
				error()
		else: 
			deletecontent(g)
			g.write("print 'Syntax error. Expected )'")
			error()
	else: 
		deletecontent(g)
		g.write("print 'Syntax error. Expected ('")
		error()

def elif_cont():
	global charClass
	global g
	global f
	global tabs
	global nextChar
	global nextToken
	global lexLen
	global token
	global a
	global b
	global c
	global lexeme
	global str3
	global line
	global fprint
	tabs = tabs - 1
	for num in range(0,tabs):
		g.write("\t")
	tabs = tabs + 1
	g.write("elif (")

	lex()
	if (nextToken==LEFT_PAREN):
		lex()
		if (nextToken==VAR):
			expr2()
			print nextToken
			if (nextToken==EQUAL or nextToken==NOT_EQ or nextToken==GREATER_THAN or nextToken==LESS_THAN or nextToken==GT_EQ or nextToken==LT_EQ):
				g.write(' '.join(map(str, lexeme)).replace(" ", ""))
				lex()
				if (nextToken==VAR or nextToken==INT_LIT):
					expr2()
					g.write("):\n")
				else:
					deletecontent(g) 
					g.write("print 'Syntax error. Expected VAR or INT'")
					error()
			else: 
				deletecontent(g)
				g.write("print 'Syntax error. Expected == , != , > , < , >= , or <='")
				error()
		else: 
			deletecontent(g)
			g.write("print 'Syntax error. Expected VAR'")
			error()
		if (nextToken==RIGHT_PAREN):
			lex()
			if (nextToken==EOL):
				lex()
				block()
				if (nextToken==ELIF_COND):
					elif_cont()
			else: 
				deletecontent(g)
				g.write("print 'Syntax error. Expected EOL'")
				error()
		else: 
			deletecontent(g)
			g.write("print 'Syntax error. Expected )'")
			error()
	else: 
		deletecontent(g)
		g.write("print 'Syntax error. Expected ('")
		error()

def else_cont():
	global charClass
	global g
	global f
	global tabs
	global nextChar
	global nextToken
	global lexLen
	global token
	global a
	global b
	global c
	global lexeme
	global str3
	global line
	global fprint
	tabs = tabs - 1
	for num in range(0,tabs):
		g.write("\t")
	g.write("else:\n")
	tabs = tabs + 1

	lex()
	if (nextToken==EOL):
		lex()
		block()
	else: 
		deletecontent(g)
		g.write("print 'Syntax error. Expected EOL'")
		error()

def for_cont():
	global charClass
	global g
	global f
	global tabs
	global nextChar
	global nextToken
	global lexLen
	global token
	global a
	global b
	global c
	global lexeme
	global str3
	global fprint
	global line
	for num in range(0,tabs):
		g.write("\t")
	tabs = tabs + 1
	check = 0
	lex()
	if (nextToken==LEFT_PAREN):
		lex()
		if (nextToken==VAR):
			str1 = lexeme
			
			lex()
			if (nextToken==ASSIGN_OP):
				lex()
				if (nextToken==VAR or nextToken==INT_LIT):
					str2 = lexeme
					lex()
					if (nextToken==COLON):
						lex()
						if (nextToken==VAR):
							expr()
							if (nextToken==EQUAL or nextToken==NOT_EQ or nextToken==GREATER_THAN or nextToken==LESS_THAN or nextToken==GT_EQ or nextToken==LT_EQ):
								if (nextToken==GT_EQ or nextToken==LT_EQ):
									check = 1
								lex()
								if (nextToken==VAR or nextToken==INT_LIT):
									str3 = lexeme
									expr()
								else: 
									deletecontent(g)
									g.write("print 'Syntax error. Expected VAR or INT'")
									error()
							else: 
								deletecontent(g)
								g.write("print 'Syntax error. Expected == , != , > , < , >= or <='")
								error()
						else: 
							deletecontent(g)
							g.write("print 'Syntax error. Expected VAR'")
							error()
						if (nextToken==COLON):
							lex()
							if (nextToken==VAR):
								lex()
								if (nextToken==ITER_PLUS or nextToken==ITER_MINUS):
									g.write("for ")
									g.write(' '.join(map(str, str1)).replace(" ", ""))
									g.write(" in range (")
									if (nextToken==ITER_PLUS):
										g.write(' '.join(map(str, str2)).replace(" ", ""))
										g.write(", ")
										g.write(' '.join(map(str, str3)).replace(" ", ""))
									else:
										g.write(' '.join(map(str, str3)).replace(" ", ""))
										g.write(", ")
										g.write(' '.join(map(str, str2)).replace(" ", ""))
									if (check == 1):
										g.write("+1):\n")
									else:
										g.write("):\n")
									check = 0
									
										
									lex()
                                                                        if (nextToken==RIGHT_PAREN):
                                                                            lex()
									    if (nextToken==EOL):
									    	lex()
									    	block()
									    	if (nextToken==END_DELIM):
											tabs = tabs - 1
								
									    		lex()
									    		if (nextToken==EOL):
									    			lex()
									    		else: 
									    			deletecontent(g)
								    				g.write("print 'Syntax error. Expected EOL'")
									    			error()
									    	else: 
									    		deletecontent(g)
									    		g.write("print 'Syntax error. Expected #end'")
									    		error()
									    else: 
									    	deletecontent(g)
									    	g.write("print 'Syntax error. Expected EOL'")
									    	error()
                                                                        else: 
                                                                        	deletecontent(g)
                             	                                          	g.write("print 'Syntax error. Expected )'")
                                                                        	error()
								else: 
									deletecontent(g)
									g.write("print 'Syntax error. Expected ++ or --'")
									error()
							else: 
								deletecontent(g)
								g.write("print 'Syntax error. Expected VAR'")
								error()
						else: 
							deletecontent(g)
							g.write("print 'Syntax error. Expected ;'")
							error()
					else: 
						deletecontent(g)
						g.write("print 'Syntax error. Expected ;'")
						error()
				else: 
					deletecontent(g)
					g.write("print 'Syntax error. Expected VAR or INT'")
					error()
			else: 
				deletecontent(g)
				g.write("print 'Syntax error. Expected ='")
				error()
		else: 
			deletecontent(g)
			g.write("print 'Syntax error. Expected VAR'")
			error()
	else: 
		deletecontent(g)
		g.write("print 'Syntax error. Expected ('")
		error()

def cond():
	global charClass
	global g
	global f
	global tabs
	global nextChar
	global nextToken
	global lexLen
	global token
	global a
	global b
	global c
	global lexeme
	global str3
	global fprint
	global line

	if (nextToken==VAR):
		g.write(' '.join(map(str, lexeme)).replace(" ", ""))
		expr()
		if (nextToken==EQUAL or nextToken==NOT_EQ or nextToken==GREATER_THAN or nextToken==LESS_THAN or nextToken==GT_EQ or nextToken==LT_EQ):
			g.write(' '.join(map(str, lexeme)).replace(" ", ""))
			lex()
			if (nextToken==VAR or nextToken==INT_LIT):
				g.write(' '.join(map(str, lexeme)).replace(" ", ""))
				expr()
			else:
				deletecontent(g)
				g.write("print 'Syntax error. Expected VAR or INT'")
				error()
		else: 
			deletecontent(g)
			g.write("print 'Syntax error. Expected == , != , > , < , >= or <='")
			error()
	else: 
		deletecontent(g)
		g.write("print 'Syntax error. Expected VAR'")
		error()

def deletecontent(pfile):
	global line
	global nextToken
	pfile.seek(0)
	pfile.truncate()
	if (nextToken != EOL):
		line = line+1
	pfile.write("import sys\nimport time\nimport tkSimpleDialog\nsys.stdout=open('output.txt', 'w')\n\n")
	pfile.write("line = %i" % line)
	pfile.write("\n\n")
	pfile.write("print 'line '+str(line)")
	pfile.write("\n\n")

def error():
	global charClass
	global g
	global f
	global tabs
	global nextChar
	global nextToken
	global lexLen
	global token
	global a
	global b
	global c
	global lexeme
	global str3
	global fprint
	global line
	fprint = 1
	if (nextToken!=EOL and nextToken!=EOF):
		while (nextToken!=EOF):
			nextChar = f.read(1)
			if (nextChar == EOF):
				nextToken = EOF
				break

def start(filename):
	global line
	global f
	global g
	global nextChar
	global nextToken
	global lexLen
	global token
	global a
	global b
	global c
	global lexeme
	global str3
	global charClass
	global tabs
	global fprint
	nextChar = 'a'
	nextToken = 0
	lexLen = 0
	token = 0
	a = 0
	b = 0
	c = 0
	line = 0 
	lexeme = []
	str3 = []
	charClass = "UNKNOWN"
	tabs = 0
	f = open("hash.txt",'r')
	g = open("translated.py",'w')
	print f
	g = open("translated.py", 'w')	
	f = open(filename, 'r')
	print f	
	g.write("import sys\nimport time\nimport tkSimpleDialog\nsys.stdout=open('output.txt', 'w')\n\n")
	getChar()
	while(nextToken!=EOF):
		lex()
		program()
	g.write("\nsys.stdin=sys.__stdin__\nsys.stdout=sys.__stdout__")
	f.close()
	g.close()
	return 1