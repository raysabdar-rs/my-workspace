# Given the prices of a stock over time find the maximum profit you can gain
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_ = prices[0]
        max_ = 0
        profit = 0
        for n in prices:
            if n <= min_:
                min_ = n
                max_ = 0
            else:
                max_ = max(max_, n)
            if max_ > min_:
                profit = max(profit, max_ - min_)

        return profit
