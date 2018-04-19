class Solution:
    """
    @param s: The data stream
    @return: Return the judgement stream
    """
    def getStream(self, s):
        record = {}
        result = []
        for char in s:
            if char not in record:
                record[char] = 1
            else:
                record[char] += 1

            oddNum = 0
            for item in record:
                if record[item] % 2 == 1:
                    oddNum += 1
            if oddNum > 1:
                result.append(0)
            else:
                result.append(1)
        return result
        # Write your code here
