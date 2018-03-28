class Solution:
    """
    @param Matrix: the input
    @return: the element which appears every row
    """
    def FindElements(self, Matrix):
        record = {}
        for i in Matrix[0]:
            if i not in record:
                record[i] = 1

        for i in record:
            for row in Matrix[1:]:
                if i not in row:
                    record[i] = 0

        for i in record:
            if record[i] == 1:
                return i
        # write your code here
