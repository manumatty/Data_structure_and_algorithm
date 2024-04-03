#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
def maxProfit(self, prices):   # Defines a function named maxProfit that takes a list of prices as an argument
       max_profit=0           # Initializes a variable named max_profit to store the maximum profit found
       min_price=prices[0]    # Initializes a variable named min_price to the first price in the list

       for i in prices:        # Iterates through each price in the list
           if min_price > i:  # If the current price is less than the current min_price
               min_price=i    # Update min_price to the current price
           else:              # If the current price is greater than or equal to the current min_price
               if i-min_price>max_profit: # If the difference between the current price and min_price is greater than max_profit
                   max_profit=i-min_price # Update max_profit to the difference between the current price and min_price
       return max_profit       # Returns the maximum profit found