import java.util.ArrayList;
import java.util.List;

public class MinSizeSubArraySum {

    public static void main(String[] args) {

        int[] arr = {2,3,1,2,4,3};
        int target = 7;

        List<List<Integer>> sumStore = new ArrayList<>();
        for (int i = 0; i < arr.length; i++)
        {
            List<Integer> row = new ArrayList<>();
            for(int j = 0; j < arr.length; j++){
                row.add(0);
            }
            sumStore.add(row);
        }

        for(int i = 0; i < arr.length; i++){
            sumStore.get(i).set(i, arr[i]);
        }
        int result = 0;
        for(int i = 0; i < arr.length; i++){
            for(int j = i; j < arr.length; j++){
                if (j != 0)
                {
                    sumStore.get(i).set(j, sumStore.get(i).get(j - 1) + arr[j]);
                }
                if(sumStore.get(i).get(j) >= target){
                    if(result == 0){
                        result = j - i + 1;
                    }
                    else {
                        result = Math.min(result, j - i + 1);
                    }
                }
            }
        }

        System.out.println(result);
        
    }
    
}
