class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max,profit = 0, 0
        buy ,sell = 0,1
        # sell < length of prices -> still loop
        while sell < len(prices) :
            # value in day buy > day sell --> day buy = day sell, otherwise no profit
            if prices[buy] > prices[sell]:
                buy = sell
            #update profit, and move sell to new day
            else:
                profit = prices[sell] - prices[buy]
                sell+=1
                # compare maxProfit to the newProfit--> if it greater than, update maxProfit
                if(max < profit):
                    max = profit
        return max
