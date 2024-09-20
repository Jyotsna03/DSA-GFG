#User function Template for python3

class Solution:
    # Returns count of buildings that can see sunlight
    def countBuildings(self, height):
        # Initializing the left pointer and max height
        l = 0
        count = 1  # The first building always sees the sunrise
        max_height = height[0]
        
        # Start iterating from the second building
        for r in range(1, len(height)):
            # If the current building is taller than max_height
            if height[r] > max_height:
                count += 1  # Increment the count
                max_height = height[r]  # Update the max_height to the current building's height
        
        return count
                
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        height = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.countBuildings(height)
        print(ans)

# } Driver Code Ends