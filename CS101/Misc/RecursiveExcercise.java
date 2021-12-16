import java.util.*;

public class RecursiveExcercise {

   public static void main(String [] args) {

          Scanner scan = new Scanner(System.in);

          System.out.println("Enter a positive integer: ");

          int n = scan.nextInt();

         System.out.println( factorial(n));

 }

// Examine the factorial method:

   public static int factorial(int n) {

          if (n == 1)                         // base case is when n is equal to 1

                 return n;

          else

                 n = n * factorial(n - 1);       // general case calls factorial again but passes a smaller value

          return n;

   }  

 }