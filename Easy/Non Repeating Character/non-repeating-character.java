//{ Driver Code Starts
//Initial Template for Java

import java.io.*;
import java.lang.*;
import java.util.*;

class Driverclass
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        
        while(t-- > 0)
        {
            String st = sc.next();
            
            char ans=new Solution().nonrepeatingCharacter(st);
            
            if(ans!='$')
            System.out.println(ans);
            else
            System.out.println(-1);
        }
    }
}

// } Driver Code Ends


//User function Template for Java

class Solution
{
    //Function to find the first non-repeating character in a string.
    static char nonrepeatingCharacter(String S)
    {
        //Your code here
        int CHAR=256;
        int [] count = new int[CHAR];
        for(int i=0; i<S.length(); i++) {
            count[S.charAt(i)]++;
        }
        for(int i=0; i<S.length(); i++) {
            if(count[S.charAt(i)]==1)
            return S.charAt(i);
        }
        return '$';
    }
}

