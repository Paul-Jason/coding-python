import java.util.ArrayList;
import java.util.List;

public class KBeautyNum {

    /*
    num = 430043, k = 2
     */
    public static void main(String[] args)
    {
        int num = 430043, k = 2;
        int l = 0, r = k - 1;
        String str = String.valueOf(num);
        int result = 0;
        List<String> subStrings = new ArrayList<>();
        subStrings.add(String.valueOf(str.charAt(0)));
        for (int i = 1; i < str.length(); i++)
        {
            subStrings.add(subStrings.get(i-1) + str.charAt(i));
        }
        while(r < str.length()){
            int divisor = Integer.parseInt(subStrings.get(r));
            if(divisor != 0 && num % divisor == 0){
                result++;
            }
            l++; r++;
        }
        System.out.println(result);
    }
}
