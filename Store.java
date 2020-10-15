package JC.Day65;

import java.util.Scanner;
import java.util.stream.IntStream;

public class Store {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        
        int N = sc.nextInt();
        int [] arr = new int [N];
        for (int i = 0; i < arr.length; i++) {
            arr[i] = sc.nextInt();
        }

        int M = sc.nextInt();
        int [] brr = new int [M];
        for (int i = 0; i < brr.length; i++) {
            brr[i] = sc.nextInt();
        }

        for (int i = 0; i < M; i++) {
           int c = brr[i];
           if(IntStream.of(arr).anyMatch(x->x==c)){
                System.out.print("yes"+" ");
           }
           else{
               System.out.print("No"+" ");
           }
        }
    }
}
