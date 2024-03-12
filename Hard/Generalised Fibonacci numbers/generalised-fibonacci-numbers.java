//{ Driver Code Starts
//Initial Template for Java

import java.io.*;
import java.util.*;

class GFG {
    public static void main(String args[]) throws IOException {
        BufferedReader read =
            new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(read.readLine());
        while (t-- > 0) {
            String S[] = read.readLine().split(" ");
            
            long a = Long.parseLong(S[0]);
            long b = Long.parseLong(S[1]);
            long c = Long.parseLong(S[2]);
            long n = Long.parseLong(S[3]);
            long m = Long.parseLong(S[4]);

            Solution ob = new Solution();
            System.out.println(ob.genFibNum(a,b,c,n,m));
        }
    }
}
// } Driver Code Ends


//User function Template for Java

class Solution {
    static long genFibNum(Long a,Long b, Long c, long n, long m){
        if(n<=2)
        return 1L % m;
        List <List<Long>> mat = new ArrayList<>();
        mat.add(Arrays.asList(a,b,1L));
        mat.add(Arrays.asList(1L,0L,0L));
        mat.add(Arrays.asList(0L,0L,1L));
        List<List<Long>> res = new ArrayList<>();
        res.add(Arrays.asList(1L,0L,0L));
        res.add(Arrays.asList(0L,1L,0L));
        res.add(Arrays.asList(0L,0L,1L));
        n-=2;
        while(n > 0){
            if((n & 1)==1)
            res=multiply(res,mat,m);
            mat=multiply(mat,mat,m);
            n>>=1;
        }
        return (res.get(0).get(0) + res.get(0).get(1) + c * res.get(0).get(2)) %m;
        
    }
    
    static List<List<Long>> multiply(List<List<Long>> A, List<List<Long>> B,long m){
        int size = A.size();
        List<List<Long>> result = new ArrayList<>();
        for (int i =0; i<size; ++i){
            List<Long> row = new ArrayList<>();
            for(int j = 0;j<size;++j){
                long sum = 0;
                for (int k = 0; k< size; ++k){
                    sum+= A.get(i).get(k) * B.get(k).get(j);
                    sum%=m;
                }
                row.add(sum);
            }
            result.add(row);
        }
        return result;
    }
};