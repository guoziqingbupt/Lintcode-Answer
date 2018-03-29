class Solution:
    """
    @param inputA: Input stream A
    @param inputB: Input stream B
    @return: The answer
    """
    def inputStream(self, inputA, inputB):

        r1, r2 = [], []

        for i in inputA:
            if i == "<" and len(r1) != 0:
                r1.pop()
            elif i != "<":
                r1.append(i)

        for i in inputB:
            if i == "<" and len(r2) != 0:
                r2.remove(r2[-1])
            elif i != "<":
                r2.append(i)

        n1, n2 = len(r1), len(r2)

        if n1 != n2:
            return "NO"

        for index in range(n1):
            if r1[index] != r2[index]:
                return "NO"
        return "YES"
        # Write your code here

obj = Solution()
inputA = "<<<<<<<"
inputB = "<<<<"
print(obj.inputStream(inputA, inputB))
