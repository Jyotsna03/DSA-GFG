#User function Template for python3
class Solution:
    def isValid(self, ip_str):
        a = ip_str.split('.') 
        if len(a) != 4:
            return 0
        for i in a:
            # Check if i is a digit, within the range 0-255, and does not have leading zeroes
            if i.isdigit() and 0 <= int(i) <= 255 and str(int(i)) == i:
                continue
            else:
                return 0
        return 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        s = input()
        ob = Solution()
        if (ob.isValid(s)):
            print("true")
        else:
            print("false")

# } Driver Code Ends