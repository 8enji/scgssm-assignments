import java.util.Scanner;

public class loopLab4
{
   public static void main(String [] args)
   {
   
      Scanner scan = new Scanner(System.in);
      
      int x = 0;
      int y = 0;
      int r = 1;
      
      System.out.println("Enter two values to find the gcd between them.");
      x = scan.nextInt();
      y = scan.nextInt();
      
      while (r > 0)
      {
      if(y == 0) {
      System.out.println("The gcd is " + x);
      System.exit(0);
      }
      r = x % y;
      if (r == 0)
      {
      System.out.println("The gcd is " + y);
      //System.exit(0);
      }
      else
      {
      x = y;
      y = r;
      }
      }
      
  }
}