//{ Driver Code Starts
import java.io.*;
import java.util.*;

class IntMatrix {
    public static int[][] input(BufferedReader br, int n, int m) throws IOException {
        int[][] mat = new int[n][];

        for (int i = 0; i < n; i++) {
            String[] s = br.readLine().trim().split(" ");
            mat[i] = new int[s.length];
            for (int j = 0; j < s.length; j++) mat[i][j] = Integer.parseInt(s[j]);
        }

        return mat;
    }

    public static void print(int[][] m) {
        for (var a : m) {
            for (int e : a) System.out.print(e + " ");
            System.out.println();
        }
    }

    public static void print(ArrayList<ArrayList<Integer>> m) {
        for (var a : m) {
            for (int e : a) System.out.print(e + " ");
            System.out.println();
        }
    }
}

class GFG {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t;
        t = Integer.parseInt(br.readLine());
        while (t-- > 0) {

            int n;
            n = Integer.parseInt(br.readLine());

            int[][] edges = IntMatrix.input(br, n - 1, 2);

            Solution obj = new Solution();
            int res = obj.minimumEdgeRemove(n, edges);

            System.out.println(res);
        }
    }
}

// } Driver Code Ends



class Solution {
    int ans=0;
    int dfs(ArrayList<ArrayList<Integer>>adj,boolean[] vis,int item){
        vis[item]=true;
        int size=1;
        for(int node:adj.get(item))
           {
               if(!vis[node]){
                   int temp=dfs(adj,vis,node);
                   size+=temp;
                   if(temp%2==0)
                     ans++;
               }
           }
           return size;
    }
    public int minimumEdgeRemove(int n, int[][] edges) {
        // code here
        boolean[] vis=new boolean[n+1];
        ArrayList<ArrayList<Integer>>adj=new ArrayList<>();
        for(int i=0;i<=n;i++)
         adj.add(new ArrayList<>());
        for(int i=0;i<edges.length;i++){
          adj.get(edges[i][0]).add(edges[i][1]);
          adj.get(edges[i][1]).add(edges[i][0]);
         }
        for(int i=1;i<=n;i++){
            if(!vis[i]){
                dfs(adj,vis,i);
            }
        }
        return ans;
    }
}
