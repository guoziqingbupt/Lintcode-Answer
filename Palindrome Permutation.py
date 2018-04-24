class Solution:
    """
    @param s: the given string
    @return: if a permutation of the string could form a palindrome
    """
    def canPermutePalindrome(self, s):
        record = {}
        for char in s:
            if char not in record:
                record[char] = 1
            else:
                record[char] += 1
        count = 0
        for ele in record:
            if record[ele] % 2 != 0:
                count += 1
            if count > 1:
                return False
        return True
        # write your code here