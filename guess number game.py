"""
The guess API is already defined for you.
@param num, your guess
@return -1 if my number is lower, 1 if my number is higher, otherwise return 0
you can call Guess.guess(num)
"""


class Solution:
    # @param {int} n an integer
    # @return {int} the number you guess
    def guessNumber(self, n):

        left, right = 1, n
        cur = (left + right) // 2
        while left <= right:
            if Guess.guess(cur) == 0:
                return cur
            elif Guess.guess(cur) == -1:
                right = cur - 1
            else:
                left = cur + 1
            cur = (left + right) // 2
        # Write your code here