import java.util.Scanner;

public class LoopLab1
{
   public static void main(String [] args)
   {
      Scanner scan = new Scanner(System.in);
      
      System.out.println("Enter values to calculate sum and average \n"
      + " Enter negative to stop. ");
      
      int count = 0;
      int sum = 0;
      int value = scan.nextInt();
      double avg = 0;
    
      
      while(value >= 0)
      {
         sum += value;
         count++;
         System.out.println("Enter another non-negative value to continue ");
         value = scan.nextInt();
      }
   
      System.out.println("Sum is " + sum + " and count is " + count);
      if(count > 0)
      {
         avg = (double)sum / count;
         System.out.println("Average is " + avg);
      }
      else
      {
      System.out.println("Average is not applicable");
      }
   }
}