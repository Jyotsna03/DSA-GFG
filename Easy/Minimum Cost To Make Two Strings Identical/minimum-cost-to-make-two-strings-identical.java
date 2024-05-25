//{ Driver Code Starts
// Initial Template for Java

import java.io.*;
import java.util.*;

class GfG {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while (t-- > 0) {
            String X = sc.next();
            String Y = sc.next();
            int costX = sc.nextInt();
            int costY = sc.nextInt();

            Solution ob = new Solution();
            System.out.println(ob.findMinCost(X, Y, costX, costY));
        }
    }
}
// } Driver Code Ends


class Solution {
    public int findMinCost(String x, String y, int costX, int costY) {
        int n1=x.length();
        int n2=y.length();
        int[][] dp=new int[n1+1][n2+1];
        for(int i=1;i<=n1;i++){
            for(int j=1;j<=n2;j++){
                if(x.charAt(i-1)==y.charAt(j-1)){
                    dp[i][j]=costX+costY+dp[i-1][j-1];
                }
                else{
                    dp[i][j]=Math.max(dp[i-1][j],dp[i][j-1]);
                }
            }
        }
        return (n1*costX+n2*costY)-dp[n1][n2];
    }
}