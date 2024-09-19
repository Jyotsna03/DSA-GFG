# User function Template for python3

class Solution:
    
    # Function to reverse words in a given string.
    def reverseWords(self, str):
        # Split the string into words based on '.'
        words = str.split('.')
        # Reverse the list of words
        reversed_words = words[::-1]
        # Join the reversed list into a string with '.' as a separator
        return '.'.join(reversed_words)

        
        # code here 


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = str(input())
        obj = Solution()
        print(obj.reverseWords(s))

# } Driver Code Ends