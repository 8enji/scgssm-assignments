import java.util.*;

public class RecursiveGCD {
   public static void main(String[] args) {
   
   Scanner scan = new Scanner(System.in);
   
   System.out.println("ENeter a poitive integer for x: ");
   int x = scan.nextInt();
   
   System.out.println("Enter a positive integer for y: ");
   int y = scan.nextInt();
   
   int answer = gcd(x, y);
   System.out.println("answer is " + answer);
   
   }
   
   public static int gcd(int x, int y){
   
      if (y == 0)
         return x;
         
      else
         return gcd(y,x%y);
         
     }
     
 }