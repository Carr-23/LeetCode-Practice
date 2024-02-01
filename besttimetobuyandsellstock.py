class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minIndex = 0
        for p in range(1, len(prices)):
            if prices[p] - prices[minIndex] > maxProfit:
                maxProfit = prices[p] - prices[minIndex]

            if prices[p] < prices[minIndex]:
                minIndex = p

        return maxProfit
