class Solution:
    """
    @param A: a string
    @param B: a string
    @return: a boolean
    """
    def Permutation(self, A, B):

        if len(A) != len(B):
            return False

        list_B = [char for char in B]
        for char in A:
            if char in list_B:
                list_B.remove(char)
            else:
                return False
        return len(list_B) == 0
        # write your code here