#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
def maxProfit(prices):
   max_profit = 0  # Initialize the maximum profit to 0
   for i in range(1, len(prices)):  # Iterate through the list of prices
       if prices[i] > prices[i - 1]:  # If the current price is greater than the previous price
           max_profit += prices[i] - prices[i - 1]  # Add the difference between the two prices to the total profit
   return max_profit  # Return the total profit