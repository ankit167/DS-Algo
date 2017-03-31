def addWithoutOperator(x, y):
	while y != 0:
		carry = x & y
		x = x ^ y
		y = carry << 1
	print x

def main():
    x,y = map(int, raw_input().split())
    addWithoutOperator(x,y)

if __name__=='__main__':
    main()
