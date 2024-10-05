class Solution:
    def maximumProfit(self, prices):
        sell = 0
        profit = 0
        temp = 0
        for i in range(len(prices)-1,-1,-1):
            if prices[i]>sell:
                sell = prices[i]
            elif prices [i] < sell:
                temp = sell - prices[i]
                profit = max(profit, temp)
        return profit    
        # code here


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())  # Read number of test cases
    for _ in range(t):
        # Read input and split it into a list of integers
        prices = list(map(int, input().split()))
        # Create a Solution object and calculate the result
        obj = Solution()
        result = obj.maximumProfit(prices)
        # Print the result
        print(result)

# } Driver Code Ends