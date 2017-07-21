import sys
import os
import re
import math
from random import randint


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
# Check if a number is power of two using bitwise operator
#
def check_power_of_two(n):
    if n > 0 and n & (n-1) == 0:
        return True
    return False


#
# Count the number of 1's in the bit representation of an unsigned integer
# T(n)- O(log n)
#
def count_ones(n):
    if n < 0:
        return  # Avoid negative integers
    c = 0
    while n:
        # Check the right most bit and right shift
        # the number by 1 bit
        c += n & 1
        n >>= 1
    print c


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
# Print all prime factors of a given number.
# Input: 12
# Output: 2 2 3
#
# T(n)- O(sqrt(n))
#
def prime_factors(n):
    while n % 2 == 0:  # Print this number of 2's that divide n
        print 2,
        n = n/2

    # n is odd at this point of time. Only odd factors left to consider.
    for i in range(3, int(math.sqrt(n))+1, 2):
        while n % i == 0:
            print i,
            n = n/i

    if n > 2:  # Handles the case where n is a prime number greater than 2.
        print n


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


#
# Given a music player with 'n' songs. Play a song randomly, making
# sure that each song gets played exactly once. The program should
# terminate once all songs have been played.
#
# Approach: Find a random song in the list. Play the song. Swap the
#           song with the last song in the list. Reduce length of the list
#           by 1. Iterate with this logic until the length of the list gets
#           reduced to 0.
#
# T(n)- O(n)
#
# Note: The hashmap approach (to check whether a song has been played before,
#       if not, hash it) might not work, since the random function might
#       might return an already played song again and again, leading to
#       infinite loop.
#
def music_player(a):
    n = len(a)
    while n > 0:
        num = randint(0, n-1)
        print "Playing song %s" % a[num]
        a[num], a[n-1] = a[n-1], a[num]
        n -= 1


#
# Given the top left and bottom right coordinates of two rectangles, check if
# the rectangles overlap.
#
def rectangle_intersect(l1, r1, l2, r2):
    '''
    l1 = {'x':0, 'y':10}, r1 = {'x':10, 'y':0}
    l2 = {'x':5, 'y':5}, r2 = {'x':15, 'y':0}
    '''

    # if one rectangle is on the left side of the other
    if l1['x'] > r2['x'] or l2['x'] > r1['x']:
        return False

    # if one rectangle is above the other
    if l1['y'] < r2['y'] or l2['y'] < r1['y']:
        return False
    return True


#
# Check if a given number is a palindrome (without using extra space)
#
def is_palindrome(x):
    d = len(str(x))  # Number of digits in the number

    while d > 0:
        right_digit = x % 10
        left_digit = x/int(pow(10, d-1))

        if left_digit != right_digit:
            break

        x = x % int(pow(10, d-1))  # Trim one digit from left
        x = x/10  # Trim one digit from right
        d -= 2

    if d > 0:
        return False
    return True


#
# Given an infinite number line. We can start from '0', and can go either left
# or right in each step. In the ith step, we can move +i steps or -i steps.
# Find out the most optimal number of steps to reach a destination.
#
# The 'source' and 'step' variables are '0' by default.
#
def min_steps_to_a_destination(source, step, dest):
    if abs(source) > dest:
        return sys.maxint

    if source == dest:
        return step

    # if we go on the positive side
    pos = min_steps_to_a_destination(source+step+1, step+1, dest)
    # if we go on the negative side
    neg = min_steps_to_a_destination(source-step-1, step+1, dest)

    return min(pos, neg)  # return minimum of both cases


def main():
    n = int(raw_input())
    print min_steps_to_a_destination(0, 0, n)

if __name__ == '__main__':
    main()
