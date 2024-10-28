public class PalindromeDp {

    /**
     * 
     * t f f f 
     *   t f f 
     *     t f 
     *       t
     */

    public static void main(String[] args) {
        String str = "bbababbabababbaaba";
        int strLen = str.length();
        boolean[][] dp = new boolean[strLen][strLen];
        for(int i = 0, j = 0; i < strLen; i++,j++){
            dp[i][j] = true;
        }
        for(int i = 0, j = 1; i < strLen - 1; i++,j++){
            if(str.charAt(i) == str.charAt(j)) dp[i][j] = true;
            else dp[i][j] = false;
        }
        //printdp(dp, strLen);
        int res = 1;
        for(int len = 3; len < strLen + 1; len++){
            for(int i = 0; i < strLen; i++){
                int j = i + len - 1;
                if(j < strLen){
                    if(dp[i+1][j-1] == true && str.charAt(i) ==  str.charAt(j)){
                        dp[i][j] = true;
                        res = Math.max(res, j - i + 1);
                        System.out.println(str.substring(i, j+1));
                    }
                    else{
                        dp[i][j] = false;
                    }
                }
            }
        }
        System.out.println(res);
    }

    public static void printdp(boolean[][] dp, int n){
        for(int i = 0; i < n; i++){
            for(int j = i; j < n; j++){
                System.out.print(dp[i][j] + " ");
            }
            System.out.println();
        }
    }
}

/**
 * 
 * bbababbabababbaaba
 * 
 * brute force - i , j
 * time - O(n ^ 3)
 * 
 * dp 
 * abba
 * 
 * 2d - n x n 
 * 
 * i - 1 & j + 1 is palin & a[i] = a[j]
 * 
 * 
 * tff
 *  t
 *   t 
 *    t
 * 
 * time - O(n ^ 2)
 * space - O(n ^ 2)
 */
