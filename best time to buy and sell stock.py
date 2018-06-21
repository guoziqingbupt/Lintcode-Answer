class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        dp = [0]
        index, n = 1, len(prices)
        while index < n:
            gap = prices[index] - prices[index - 1]
            if dp[-1] < 0:
                dp.append(gap)
            else:
                dp.append(dp[-1] + gap)
            index += 1
        return max(dp)
        # write your code here
