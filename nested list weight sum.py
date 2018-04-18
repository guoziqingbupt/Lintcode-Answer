"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation

class NestedInteger(object):
    def isInteger(self):
        # @return {boolean} True if this NestedInteger holds a single integer,
        # rather than a nested list.

    def getInteger(self):
        # @return {int} the single integer that this NestedInteger holds,
        # if it holds a single integer
        # Return None if this NestedInteger holds a nested list

    def getList(self):
        # @return {NestedInteger[]} the nested list that this NestedInteger holds,
        # if it holds a nested list
        # Return None if this NestedInteger holds a single integer
"""


class Solution(object):
    # @param {NestedInteger[]} nestedList a list of NestedInteger Object
    # @return {int} an integer
    def depthSum(self, nestedList):

        result = 0
        times = 1
        for ele in nestedList:
            result += self.helper(ele, times)
        return result

    def helper(self, ele, times):

        result = 0

        if ele.isInteger():
            result += ele.getInteger() * times
        else:
            times += 1
            for i in ele.getList():
                result += self.helper(i, times)
        return result
        # Write your code here
