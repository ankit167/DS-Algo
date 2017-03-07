
#
# Returns the longest palindromic substring
# T(n)- O(n^2), S(n)- O(n^2)
#
def longestPalindromicSubstring(s):
	n = len(s)
	table = [[False for j in range(n)] for i in range(n)]
	for i in range(n):
		table[i][i] = True
	maxlen, start, end = 1, 0, 0
	for i in range(n-1):
		if s[i] == s[i+1]:
			table[i][i+1] = True
			start = i
			end = i+1
			maxlen = 2
	for k in range(3,n+1):
		for i in range(0,n-k+1):
			j = i+k-1
			if s[i] == s[j] and table[i+1][j-1]:
				table[i][j] = True
				if k > maxlen:
					maxlen = k
					start = i
					end = j
	return s[start:end+1]

#
# Computes prefix array for KMP
#
def prefixCompute(f, patt, m):
	i,j = 1,0
	f[0] = 0
	while i < m:
		if patt[i] == patt[j]:
			f[i] = j+1
			i += 1
			j += 1
		elif j > 0:
			j = f[j-1]
		else:
			f[i] = 0
			i += 1
#
# Searches a pattern in a string using KMP algorithm.
# Compute prefix array -> Compare string and pattern
# T(n)- O(m+n), S(n)- O(m)
# n- length of string, m- length of pattern
#
def KMP(string, patt):
	m, n = len(patt), len(string)
	f = [0 for i in range(m)]
	prefixCompute(f, patt, m)
	i,j = 0,0
	while i < n:
		if string[i] == patt[j]:
			if j == m-1:
				return i-j
			i += 1
			j += 1
		elif j > 0:
			j = f[j-1]
		else:
			i += 1
	return -1

def main():
	s = raw_input()
	p = raw_input()
	print KMP(s,p)

if __name__ == "__main__":
	main()
