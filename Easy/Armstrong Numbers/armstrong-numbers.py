#User function Template for python3


class Solution:
    def armstrongNumber (self, n):
         s=0
         temp=n
         while n>0:
            l=n%10
            n=n//10
            s=s+(l**3)
         if s==temp:
            return "true"
         else:
            return "false"


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = input()
        n = int(n)
        ob = Solution()
        print(ob.armstrongNumber(n))

# } Driver Code Ends