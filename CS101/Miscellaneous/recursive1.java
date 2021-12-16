import java.util.*;

public class recursive1 {

   public static void main(String [] args) {
   
   Scanner scan = new Scanner(System.in);

   System.out.println("Enter a positive integer: ");

   int n = scan.nextInt();
   
   reverse(n);
   
}

 public static void reverse(int num){
        System.out.print(num %10);
        if(num / 10 == 0){
           return;
        }
        reverse(num /10);
           return;
    }
}