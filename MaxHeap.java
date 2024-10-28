import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;

public class MaxHeap {

    public static void main(String[] args)
    {
        char[] chars = {'A', 'A', 'B', 'B', 'B'};
        Map<Character, Integer> map1 = new HashMap<>();


        for(char character : chars){
            if(map1.containsKey(character)){
                map1.put(character, map1.get(character) + 1);
            } else{
                map1.put(character, 1);
            }
        }

        PriorityQueue<CustomEntry> heap = new PriorityQueue<>((item1, item2) -> {
            if(item1.repeat > item2.repeat){
                return -1;
            } else {
                return 1;
            }
        });
        for(Map.Entry<Character, Integer> entry : map1.entrySet()){
            heap.add(new CustomEntry(entry.getKey(), entry.getValue()));
        }
        System.out.println(heap.peek().character);
    }
}

class CustomEntry{
    Character character;
    Integer repeat;
    CustomEntry(Character ch, Integer in){
        this.character = ch;
        this.repeat = in;
    }
}
