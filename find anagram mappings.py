class Solution:
    """
    @param A: lists A
    @param B: lists B
    @return: the index mapping
    """
    def anagramMappings(self, A, B):
        result = []
        dic = {}

        for index, item in enumerate(B):
            dic[item] = index

        for i in A:
            result.append(dic[i])

        return result
        # Write your code here
