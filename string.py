
#
# Returns the longest palindromic substring
# T(n)- O(n), S(n)- O(n)
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

def main():
	s = raw_input()
	print longestPalindromicSubstring(s);

if __name__ == "__main__":
	main()
