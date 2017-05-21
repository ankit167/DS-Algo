import sys
import os
import re
import math


#
# Add two positive integers without using the '+' operator
#
def add_without_operator(x, y):
    while y != 0:
        carry = x & y
        x = x ^ y
        y = carry << 1
    print x


#
# Implementing strip() in python through regex,
# By default, white spaces are striped from left
# and right end of the string.
#
# Input: '  Hey there '
# Output: 'Hey there'
#
def strip(s, c=' '):
    regex = '^' + re.escape(c) + '+|' + re.escape(c) + '+$'
    s = re.sub(regex, '', s)
    return s


#
# Find the next greater number with the same set of digits of a given number.
#
def next_greater(n):
    l = map(int, str(n))
    i = len(l)-1
    while i >= 1 and l[i-1] >= l[i]:
        i -= 1
    if i <= 0:
        print 'Not possible'
        return
    p, index, m = i-1, i-1, sys.maxint
    # We can optimise this loop by doing a Binary Search
    # (since the sublist is sorted)
    for i in range(p+1, len(l)):
        if l[i] > l[p] and l[i] < m:
            m = l[i]
            index = i
    l[p], l[index] = l[index], l[p]
    l[p+1:] = sorted(l[p+1:])
    ng = int(''.join(str(x) for x in l))
    print ng


#
# Recursively print the contents of a directory.
# f.e.: s_path = '/etc/systemd'
#       output: All the files present in the directories and subdirectories
#               of s_path
#
def print_dir(s_path):
    for s_child in os.listdir(s_path):
        s_child_path = os.path.join(s_path, s_child)
        if os.path.isdir(s_child_path):
            print_dir(s_child_path)
        else:
            print s_child_path


#
# Print all prime numbers upto a given number using Sieve of Eratosthenes.
# Input: 5
# Output: 2,3,5
#
# T(n)- O(nlog(logn)) (Refer to O(n) soln from gfg)
#
def print_primes(n):
    p = [0 for i in range(n+1)]

    for i in range(2, int(math.sqrt(n))+1):
        if p[i] == 0:
            j = i+i
            while j < n+1:
                p[j] = 1
                j += i

    for i in range(2, n+1):
        if p[i] == 0:
            print i,


def main():
    n = int(raw_input())
    print_primes(n)

if __name__ == '__main__':
    main()
