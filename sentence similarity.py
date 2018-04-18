class Solution:
    """
    @param words1: a list of string
    @param words2: a list of string
    @param pairs: a list of string pairs
    @return: return a boolean, denote whether two sentences are similar or not
    """
    def isSentenceSimilarity(self, words1, words2, pairs):
        n1, n2 = len(words1), len(words2)
        if n1 != n2:
            return False

        index = 0
        if len(pairs) == 0:
            while index < n1:
                if words1[index] != words2[index]:
                    return False
                index += 1
            return True

        index = 0
        while index < n1:
            if not self.wordsAreSimilar(words1[index], words2[index], pairs):
                return False
            index += 1
        return True

    def wordsAreSimilar(self, w1, w2, pairs):

        for i in pairs:
            if w1 in i and w2 in i:
                return True
        return False
        # write your code here

