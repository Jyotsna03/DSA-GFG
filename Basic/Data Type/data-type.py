#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def dataTypeSize(self, str):
        type_sizes = {
            "Character":1,
            "Integer":4,
            "Long":8,
            "Float":4,
            "Double":8
        }
        
        if str in type_sizes:
            return type_sizes[str]
        else:
            return -1
solution = Solution()
        # Code here

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        str = input()
        ob = Solution()
        res = ob.dataTypeSize(str)
        print(res)
# } Driver Code Ends