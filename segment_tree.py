import math

#
# Given an array arr[0 . . . n-1]. We should be able to
# 1. Find the sum of elements from index l to r where 0 <= l <= r <= n-1
#
# 2. Change value of a specified element of the array to a new value x.
#    We need to do arr[i] = x where 0 <= i <= n-1.
#
# Approaches- (i) Run loop from l to r and find sum. Update using a[i] = x
#                 T(n)- O(n) (Sum), T(n)- O(1) (Update)
#            (ii) Use an auxilliary sum array 's', where s[i]=sum(a[0]..a[i])
#                 T(n)- O(1) (Sum), T(n)- O(n) (Update)
#           (iii) Segment Tree (Discussed below)
#
# T(n)- O(n) (Creation of segment tree)
# T(n)- O(logn) (Sum or Update query)
#


class SegmentTree:
    def __init__(self, a, n):
        height = int(math.ceil(math.log(n, 2)))
        max_size = 2*pow(2, height) - 1
        self.st = [-1]*max_size

        self.construct_tree(a, 0, n-1, 0)

    def construct_tree(self, a, ss, se, si):
        if ss == se:
            self.st[si] = a[ss]
            return a[ss]

        mid = ss + (se-ss)/2
        self.st[si] = self.construct_tree(a, ss, mid, 2*si+1) + \
                      self.construct_tree(a, mid+1, se, 2*si+2)
        return self.st[si]

    def get_sum_util(self, ss, se, qs, qe, si):
        if qs <= ss and qe >= se:
            return self.st[si]

        if qe < ss or qs > se:
            return 0

        mid = ss + (se-ss)/2
        return (self.get_sum_util(ss, mid, qs, qe, 2*si+1) +
                self.get_sum_util(mid+1, se, qs, qe, 2*si+2))

    def get_sum(self, n, qs, qe):
        if qs < 0 or qe > n-1 or qs > qe:
            print 'Invalid Input'
            return -1

        return self.get_sum_util(0, n-1, qs, qe, 0)

    def update_value_util(self, ss, se, i, diff, si):
        if i < ss or i > se:
            return

        self.st[si] += diff
        if ss != se:
            mid = ss + (se-ss)/2
            self.update_value_util(ss, mid, i, diff, 2*si+1)
            self.update_value_util(mid+1, se, i, diff, 2*si+2)

    def update_value(self, a, n, i, value):
        if i < 0 or i > n-1:
            return

        diff = value - a[i]
        a[i] = value

        self.update_value_util(0, n-1, i, diff, 0)


def main():
    a = list(map(int, raw_input().split()))
    n = len(a)
    s = SegmentTree(a, n)

    print s.get_sum(n, 1, 3)
    s.update_value(a, n, 1, 10)
    print s.get_sum(n, 1, 3)

if __name__ == '__main__':
    main()
