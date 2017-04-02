def addWithoutOperator(x, y):
	while y != 0:
		carry = x & y
		x = x ^ y
		y = carry << 1
	print x

'''
Implementing strip() in python through regex,
By default, white spaces are striped from left
and right end of the string.

Input: '  Hey there '
Output: 'Hey there'
'''
def strip(s,c=' '):
	regex = '^' + re.escape(c) + '+|' + re.escape(c) + '+$'
	s = re.sub(regex, '', s)
	return s

def main():
    s = '   hey there  '
    s = strip(s)
    print s

if __name__=='__main__':
    main()
