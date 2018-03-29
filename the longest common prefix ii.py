class Solution:
    """
    @param dic: the n strings
    @param target: the target string
    @return: The ans
    """
    def the_longest_common_prefix(self, dic, target):
        result = 0
        for string in dic:
            index = 0
            while index < len(string) and index < len(target):
                if string[index] == target[index]:
                    index += 1
                    result = max(result, index)
                else:
                    break
        return result
        # write your code here
