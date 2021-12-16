import java.util.Scanner;

public class loopLab3
{
   public static void main(String [] args)
   {
   
      Scanner scan = new Scanner(System.in);
      
      //int original = 0;
      int reverse = 0;
      int x = 0;;
      int z = 0;
      
      System.out.println("Enter one positive integer");
      x = scan.nextInt();
      
      while (x > 0)
      {
      
      z = x % 10;
      
      
      System.out.print(z);
      x = x / 10;
      
      }
      
      
   }
   
}