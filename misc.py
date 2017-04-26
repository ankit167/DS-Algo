import sys

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

#
# Find the next greater number with the same set of digits of a given number.
#
def nextGreater(n):
    l = map(int, str(n))
    i = len(l)-1
    while i >= 1 and l[i-1] >= l[i]:
        i -= 1
    if i <= 0:
        print 'Not possible'
        return
    p,index,m = i-1,i-1,sys.maxint
    # We can optimise this loop by doing a Binary Search
    # (since the sublist is sorted)
    for i in range(p+1,len(l)):
        if l[i] > l[p] and l[i] < m:
            m = l[i]
            index = i
    l[p],l[index] = l[index],l[p]
    l[p+1:] = sorted(l[p+1:])
    ng = int(''.join(str(x) for x in l))
    print ng

def main():
    n = int(raw_input())
    nextGreater(n)

if __name__=='__main__':
    main()
