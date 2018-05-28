class Solution:
    """
    @param ops: the list of operations
    @return:  the sum of the points you could get in all the rounds
    """
    def calPoints(self, ops):
        temp = []
        for i in ops:
            if i == "C":
                temp.pop()
            elif i == "+":
                temp.append(temp[-1] + temp[-2])
            elif i == "D":
                temp.append(2 * temp[-1])
            else:
                temp.append(int(i))
        return sum(temp)
        # Write your code here