#User function Template for python3

#User function Template for python3

class Solution:
    def computeLPSArray(self, pattern):
        lps = [0] * len(pattern)
        length = 0
        i = 1

        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1

        return lps

    def KMPSearch(self, text, pattern, lps):
        i, j = 0, 0
        while i < len(text):
            if pattern[j] == text[i]:
                i += 1
                j += 1
            if j == len(pattern):
                return True
            elif i < len(text) and pattern[j] != text[i]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        return False

    def minRepeats(self, A, B):
        lenA, lenB = len(A), len(B)
        lps = self.computeLPSArray(B)
        
        # Minimum number of repeats to cover the length of B
        X = (lenB + lenA - 1) // lenA
        repeatedA = A * X
        
        # Check if B is a substring in repeatedA
        if self.KMPSearch(repeatedA, B, lps):
            return X
        
        # Check with one more repetition of A
        repeatedA += A
        if self.KMPSearch(repeatedA, B, lps):
            return X + 1
        
        return -1



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        A = input()
        B = input()

        ob = Solution()
        print(ob.minRepeats(A, B))

# } Driver Code Ends