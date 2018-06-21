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
            if gap > 0:
                dp.append(dp[-1] + gap)
            else:
                dp.append(dp[-1])
            index += 1
        return dp[-1]
        # write your code here
