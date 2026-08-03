class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        minimum = prices[0]
        maxprofit = -1

        if len(prices) == 1:
            return 0

        for price in prices[1:]:
            maxprofit = price - minimum if maxprofit < price - minimum else maxprofit
            minimum = price if minimum > price else minimum

        return maxprofit if maxprofit >= 0 else 0

        