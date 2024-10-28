import java.util.ArrayList;
import java.util.List;

public class MinSizeSubArraySumSlidingWindow
{
    /**
     * @param args
     *
     * {2,3,1,2,4,3};
     *        l
     *          r
     */

    public static void main(String[] args) {

        int[] arr = {2,3,1,2,4,3};
        int target = 7;

        int left = 0, right = 0, sum = 0, minSize = Integer.MAX_VALUE;
        while(right < arr.length){
            sum += arr[right];
            while(sum >= target){
                // condition to shrink
                minSize = Math.min(minSize, right - left + 1);
                sum -= arr[left];
                left++;
            }
            right++;
        }
        System.out.println(minSize);
        
    }
    
}
