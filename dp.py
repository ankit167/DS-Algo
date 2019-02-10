# This file contains list of problems, that can be solved through Dynamic Programming

#
# Given a number, find the minimum number of squares
# whose sum is equal to n.
#
# Input: 6
# Output: 3 (1*1 + 1*1 + 2*2)
#
# Input: 27
# Output: 3 (3*3 + 3*3 + 3*3)
#
# T(n)- O(n*n)
#
def min_square_sum(n):
    # dp[i] stores the minimum number of squares that add to i
    dp = [0, 1, 2, 3]

    for i in range(4, n + 1):
        # Setting max value of dp[i] = i
        # dp[4] = 4 (1*1 + 1*1 + 1*1 + 1*1)
        dp.append(i)

        for x in range(1, i + 1):
            temp = x * x
            if temp > i:
                break
            dp[i] = min(dp[i], 1 + dp[i - temp])  # Recursive formula to compute min squares

    return dp[n]


def main():
    n = int(raw_input())
    print min_square_sum(n)


if __name__ == '__main__':
    main()
