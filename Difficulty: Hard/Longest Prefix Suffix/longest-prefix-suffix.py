#User function Template for python3

class Solution:
    def lps(self, str):
        # code here
        n = len(str)
        lps1 = [0]*n
        lps1[0] = 0
        i = 1
        length = 0
        while i < n:
            if str[i] == str[length]:
                length += 1
                lps1[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps1[length-1]
                else:
                    lps1[i] = 0
                    i += 1
        return lps1[n-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()

        ob = Solution()
        answer = ob.lps(s)
        print(answer)

# } Driver Code Ends