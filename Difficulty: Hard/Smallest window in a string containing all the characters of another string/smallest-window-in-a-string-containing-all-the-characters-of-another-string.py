#User function Template for python3



from collections import Counter

class Solution:
    
    #Function to find the smallest window in the string s consisting
    #of all the characters of string p.
    def smallestWindow(self, s, p):
        #code here
        
        p_count = Counter(p)
        required = len(p_count)  # Number of unique characters in p
        
        # Dictionary to store the frequency of characters in the current window
        window_count = {}
        
        # Two pointers for sliding window
        start = 0
        min_len = float('inf')
        min_start = 0
        formed = 0  # To keep track of how many unique characters in the window match p
        
        left = 0
        for right in range(len(s)):
            # Add the current character to the window
            char = s[right]
            window_count[char] = window_count.get(char, 0) + 1
            
            # If the frequency of the current character in the window matches its frequency in p
            if char in p_count and window_count[char] == p_count[char]:
                formed += 1
            
            # Try to shrink the window from the left
            while left <= right and formed == required:
                char = s[left]
                
                # Update the minimum length and starting index
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_start = left
                
                # Remove the leftmost character from the window
                window_count[char] -= 1
                if char in p_count and window_count[char] < p_count[char]:
                    formed -= 1
                
                # Move the left pointer ahead
                left += 1
        
        # If no valid window was found
        if min_len == float('inf'):
            return "-1"
        
        # Return the smallest window substring
        return s[min_start:min_start + min_len]

        #code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s=str(input())
        p=str(input())
        ob = Solution()
        print(ob.smallestWindow(s,p))
# } Driver Code Ends