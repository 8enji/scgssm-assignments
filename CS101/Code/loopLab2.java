import java.util.Scanner;

public class loopLab2
{
   public static void main(String [] args)
   {
   
      Scanner scan = new Scanner(System.in);
      
      int count = 0;
      int min = 0;
      int max = 0;
      int value = 0;
      
      System.out.println("How many values do you want to input (input an integer larger than zero)?");
      count = scan.nextInt();
      
      if(count == 0)
      System.exit(0);
      
      
      System.out.println("What is your first value?");
      value = scan.nextInt();
      
      min = value;
      max = value;
      
      while(count>1)
      {
      System.out.println("What is your next value?");
      value = scan.nextInt();
      if(value > max)
      max = value;
      
      if(value < min)
      min = value;
      
      count--;
      }
      
      System.out.println("Max: " + max + " Min: " + min);
      
   }
}
      