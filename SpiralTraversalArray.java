import java.util.*;;

class SpiralTraversalArray{
    public static void main(String[] args) {
        int[][] arr = {
            {1,2,3,4,5},
            {3,4,5,7,4},
            {6,1,4,9,0},
            {6,1,4,9,0},
        };
        int rows = 3;
        int cols = 5;
        List<Integer> res = new ArrayList<>();

        int noOfSprials = (rows % 2 == 0) ? (rows/2) : (rows/2) + 1;
        for(int spiralNo = 0; spiralNo < noOfSprials; spiralNo++){
            //right 
            for(int i = spiralNo, j = spiralNo; j < cols - spiralNo; j++){
                res.add(arr[i][j]);
            }
            //bottom 
            for(int i = spiralNo, j = cols - 1 - spiralNo; i < rows - spiralNo; i++){
                res.add(arr[i][j]);
            }
            //left 
            for(int i = rows - 1 - spiralNo, j = cols - 1 - spiralNo; j >= spiralNo; j--){
                res.add(arr[i][j]);
            }
            //top 
            for(int i = rows - 1 - spiralNo, j = spiralNo; i >= spiralNo; i--){
                res.add(arr[i][j]);
            }
        }
        System.out.println(res);
    }
}