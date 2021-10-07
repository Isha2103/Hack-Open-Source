import java.util.*;

public class Program
{
    public static void main(String[] args) {
        int arr[] = {4,3,4,7,2,7,8,2,3,1};
        dupli(arr);
    }
    public static void dupli(int arr[]){
        Arrays.sort(arr);
        int n = arr.length;
       /* for(int j=0;j<n;j++){
            System.out.println(arr[j]);
        }*/
        ArrayList list = new ArrayList(); 
        for(int i=0;i<n-1;i++){
            if(arr[i]==arr[i+1])
            list.add(arr[i+1]);
        }
        System.out.print(list);
    }
}
