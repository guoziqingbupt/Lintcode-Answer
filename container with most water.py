class Solution:
    """
    @param heights: a vector of integers
    @return: an integer
    """
    def maxArea(self, heights):
        left, right = 0, len(heights) - 1
        result = 0
        while left < right:
            temp = (right - left) * min(heights[right], heights[left])
            if temp > result:
                result = temp

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return result
        # write your code here
