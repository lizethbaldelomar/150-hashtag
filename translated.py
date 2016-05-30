def main():
	print "Enter n "
	n = input()
	fib(n)

def fib(n):
	a=0
	b=1
	for i in range (0, n):
		temp = a
		a = b
		b = temp+b
	print a

main()