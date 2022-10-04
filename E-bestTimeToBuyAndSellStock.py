def maxProfit(prices):
    l = 0   # buy
    r = 1   # sell
    maxP = 0

    while r < len(prices):

        # if statement to find right day to buy. continue moving l by one if value next to it is less
        if prices[l] < prices[r]:
            # also find day to sell
            profit = prices[r] - prices[l]
            maxP = max(maxP, profit)
        else:
            l = r
        r += 1

    return maxP


prices = [7,5,1,3,6,4]
result = maxProfit(prices)
print(prices)
print("\nMaximum Profit: ", result)
print("--------------------")

prices = [7,6,4,1,3]
result = maxProfit(prices)
print(prices)
print("\nMaximum Profit: ", result)
print("--------------------")