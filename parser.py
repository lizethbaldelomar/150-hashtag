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
				str3 = "#if"
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
				elif(lexeme == str3):
					nextToken = IF_COND
				elif(lexeme == str4):
					nextToken = ELIF_COND
				elif(lexeme == str5):
					nextToken = ELSE_COND
				elif(lexeme == str6):
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

		#print nextToken
		break
	#if (nextToken==EOL):
	#    a = -1
	#else:
	#    a = nextToken
	if (c==0):
		print "Next token is: %(",nextToken,"), Next lexeme is %(",lexeme,")\n"
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
	while (nextToken==VAR):
		lex()
	if (nextToken==ASSIGN_OP):
		while (nextToken!=EOL and nextToken!=EOF):
			#print nextToken
			#if (nextToken==EOL or nextToken==EOF):
			#    error()
			#    b=1
			#    break
			#else:
			lex()
			expr()
		if (b==0):
			print nextToken
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
	if (nextToken==VAR or nextToken==INT_LIT):
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
	print nextToken
	print "exit factor"
			
def program():
	global charClass
	global nextChar
	global nextToken
	global lexLen
	global token
	global a
	global b
	global c
	global lexeme
	print "start program\n"
	while (nextToken==START_PROG):
		lex()
	if (nextToken==EOL):
		while (nextToken!=END_PROG):
			#print nextToken
			if (nextToken==EOF):
				error()
				b=1
				break
			lex() # \n
			block1()
		if (b==0):
			lex() # endprog
			if (nextToken!=EOF):
				# error()
				outsideprog()
			else:
				print "end of code\n"
		b=0
	else:
		error()
	print "end program"

def outsideprog():
	global charClass
	global nextChar
	global nextToken
	global lexLen
	global token
	global a
	global b
	global c
	global lexeme
	print "outside program\n"
	while (nextToken==SEP_FUNC):
		lex()
		func()
	if (nextToken==EOL or nextToken==EOF): #edit
		while (nextToken!=EOF):
			#print nextToken
			# if (nextToken==EOF):
			#   error()
			#   b=1
			#   break
			lex() # \n
			outsideprog()
			print "exit outside prog\n"
		print "end of code1\n"
	else:
		error()

def func():
	global charClass
	global nextChar
	global nextToken
	global lexLen
	global token
	global a
	global b
	global c
	global lexeme
	print "separate function\n"
	while (nextToken==SEP_FUNC):
		lex() # VAR
	if (nextToken==VAR):
		lex() # (
		if (nextToken==LEFT_PAREN):
			lex() # var or )
			param()
			if (nextToken==RIGHT_PAREN):
				lex() # EOL
				while (nextToken!=END_DELIM):
					lex()
					block1()
				print "end of separate function"
				lex()
			else: error()
		else: error()
	else: error()

def block1():
	global charClass
	global nextChar
	global nextToken
	global lexLen
	global token
	print "block w/ declaration\n"
	while (nextToken==DEC_INT or nextToken==DEC_FLOAT):
		declare()
		print nextToken
	#if (nextToken==EOL):
	#	lex()
	#	print nextToken	
	block()
	# else: error()

def declare():
	global charClass
	global nextChar
	global nextToken
	global lexLen
	global token
	global a
	global b
	global c
	global lexeme
	print "declaration\n"
	if (nextToken==DEC_INT):
		lex()
		if (nextToken==VAR):
			lex()
			if (nextToken==ASSIGN_OP):
				lex()
				if (nextToken==ADD_OP or nextToken==SUB_OP or nextToken==INT_LIT):
					constant()
				else: error()
			elif (nextToken==EOL):
				lex()
			else: error()
		else: error()
	elif (nextToken==DEC_FLOAT):
		lex()
		if (nextToken==VAR):
			lex()
			if (nextToken==ASSIGN_OP):
				lex()
				if (nextToken==ADD_OP or nextToken==SUB_OP or nextToken==INT_LIT):
					constant()
					if (nextToken==FLOAT_PT):
						lex()
						if (nextToken==INT_LIT):
							lex()
							if (nextToken==EOL): lex()
							else: error()
						else: error()
					else: error()
				else: error()
			elif (nextToken==EOL):
				lex()
			else: error()
		else: error()
	else: error()


def constant():
	global charClass
	global nextChar
	global nextToken
	global lexLen
	global token
	global a
	global b
	global c
	global lexeme
	print "constant\n"
	if (nextToken==ADD_OP or nextToken==SUB_OP):
		lex()
	if (nextToken==INT_LIT):
		lex()
		if (nextToken==EOL):
			lex()

def param():
	global charClass
	global nextChar
	global nextToken
	global lexLen
	global token
	global a
	global b
	global c
	global lexeme
	print "parameter\n"
	if (nextToken==VAR or nextToken==INT_LIT):
		lex() # COMMA OR )
		param1()

def param1():
	global charClass
	global nextChar
	global nextToken
	global lexLen
	global token
	global a
	global b
	global c
	global lexeme
	print "parameter 1\n"
	if (nextToken==COMMA):
		lex() # VAR/INT
		param()

def block():
	global charClass
	global nextChar
	global nextToken
	global lexLen
	global token
	global a
	global b
	global c
	global lexeme
	print "block\n"
	print nextToken
	
	while(nextToken==EOL):
		lex()
	if (nextToken==VAR or nextToken==PRINT_OUTPUT or nextToken==READ_INPUT or nextToken==FOR_COND or nextToken==IF_COND or nextToken==CALL_FUNC or nextToken==COMMENT):
		#lex()
		function()
		#if (nextToken==EOL):
		#	lex()
		block()

def function():
	global charClass
	global nextChar
	global nextToken
	global lexLen
	global token
	global a
	global b
	global c
	global lexeme
	print "function\n"
	print nextToken
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
		comment_out()
	else: error()

def print_out():
	global charClass
	global nextChar
	global nextToken
	global lexLen
	global token
	global a
	global b
	global c
	global lexeme
	print "print function\n"
	lex()
	print nextToken	
	if (nextToken==QUOTE):
		#lex()
		print nextToken
		strexpr()
		#while(nextToken!=QUOTE):
		#	print nextToken
		#	lex()
		lex() # end
		if (nextToken==END_DELIM):
			lex()
			if (nextToken==EOL):
				lex()
			else: error()
		else: error()
	else: error()
	print "end of print"

def read_in():
	global charClass
	global nextChar
	global nextToken
	global lexLen
	global token
	global a
	global b
	global c
	global lexeme
	print "read function\n"
	lex()
	if (nextToken==VAR):
		lex()
		if(nextToken==END_DELIM):
			lex()
			if (nextToken==EOL):
				lex()
			else: error()
		else: error()
	else: error()

def strexpr():
	global charClass
	global nextChar
	global nextToken
	global lexLen
	global token
	global a
	global b
	global c
	global lexeme
	print "strexpr\n"
	print nextToken

	lex()
	#if (nextToken==LEFT_BRACKET):
	#	#lex()
	#	comment_out()
	if (nextToken==LEFT_BRACKET):
		lex()
		if (nextToken==VAR):
			lex()
			if (nextToken==RIGHT_BRACKET):
				lex()
			else: error()
		else: error()
	else:
		comment_out()
	# else: error()
	print "end of strexpr"


def comment_out():
	global charClass
	global nextChar
	global nextToken
	global lexLen
	global token
	global a
	global b
	global c
	global lexeme
	print "comment\n"

	while (nextToken==VAR or nextToken==INT_LIT):
		lex()
		if (nextToken==QUOTE):
			break
		elif (nextToken==COMMENT):
			lex()
			if(nextToken==EOL):
				lex()
				break
			else: error()
	print "end of comment"
def call_function():
	global charClass
	global nextChar
	global nextToken
	global lexLen
	global token
	global a
	global b
	global c
	global lexeme
	print "call function\n"

	lex()
	if (nextToken==VAR):
		lex()
		if (nextToken==LEFT_PAREN):
			lex()
			param()
			if (nextToken==RIGHT_PAREN):
				lex()
				if (nextToken==END_DELIM):
					lex()
					if (nextToken==EOL):
						lex()
					else: error()
				else: error()
			else: error()
		else: error()
	else: error()

def if_cont():
	global charClass
	global nextChar
	global nextToken
	global lexLen
	global token
	global a
	global b
	global c
	global lexeme
	print "if control struct\n"

	lex()
	if (nextToken==LEFT_PAREN):
		lex()
		cond()
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
					lex()
					if (nextToken==EOL):
						lex()
					else: error()
				# else: error()
			else: error()
		else: error()
	else: error()

def elif_cont():
	global charClass
	global nextChar
	global nextToken
	global lexLen
	global token
	global a
	global b
	global c
	global lexeme
	print "elif control struct\n"

	lex()
	if (nextToken==LEFT_PAREN):
		lex()
		cond()
		if (nextToken==RIGHT_PAREN):
			lex()
			if (nextToken==EOL):
				lex()
				block()
				if (nextToken==ELIF_COND):
					elif_cont()
			else: error()
		else: error()
	else: error()

def else_cont():
	global charClass
	global nextChar
	global nextToken
	global lexLen
	global token
	global a
	global b
	global c
	global lexeme
	print "else control struct\n"

	lex()
	if (nextToken==EOL):
		lex()
		block()
	else: error()

def for_cont():
	global charClass
	global nextChar
	global nextToken
	global lexLen
	global token
	global a
	global b
	global c
	global lexeme
	print "for control struct\n"

	lex()
	if (nextToken==LEFT_PAREN):
		lex()
		if (nextToken==VAR):
			lex()
			if (nextToken==ASSIGN_OP):
				lex()
				if (nextToken==VAR or nextToken==INT_LIT):
					lex()
					if (nextToken==COLON):
						lex()
						cond()
						if (nextToken==COLON):
							lex()
							if (nextToken==VAR):
								lex()
								if (nextToken==ITER_PLUS or nextToken==ITER_MINUS):
									lex()
                                                                        if (nextToken==RIGHT_PAREN):
                                                                            lex()
									    if (nextToken==EOL):
									    	lex()
									    	block()
									    	if (nextToken==END_DELIM):
									    		lex()
									    		if (nextToken==EOL):
									    			lex()
									    		else: error()
									    	else: error()
									    else: error()
                                                                        else: error()
								else: error()
							else: error()
						else: error()
					else: error()
				else: error()
			else: error()
		else: error()
	else: error()

def cond():
	global charClass
	global nextChar
	global nextToken
	global lexLen
	global token
	global a
	global b
	global c
	global lexeme
	print "condition\n"

	if (nextToken==VAR):
		expr()
		print nextToken
		if (nextToken==EQUAL or nextToken==NOT_EQ or nextToken==GREATER_THAN or nextToken==LESS_THAN or nextToken==GT_EQ or nextToken==LT_EQ):
			lex()
			if (nextToken==VAR or nextToken==INT_LIT):
				expr()
			else: error()
		else: error()
	else: error()

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
	
f = open("hashrdtest.txt", 'r')
getChar()
while(nextToken!=EOF):
	lex()
	program()
