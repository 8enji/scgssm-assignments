import java.util.ArrayList;
import java.util.Scanner;

public class loopLab6
{
   public static void main(String [] args)
   {
      ArrayList<Integer> tests = new ArrayList<Integer>();
      Scanner scan = new Scanner(System.in);
      
      int answer = 0;
      int test = 0;
      int sum = 0;
      int i = 0;
      double avg = 0;
      
      System.out.println("How many tests would you like to input for the average?");
      answer = scan.nextInt();
      
      while(i<answer)
      {
      
      System.out.println("Enter your test grade");
      test = scan.nextInt();
      tests.add(test);
      i ++;
    
      }
     
      
      for(int n = 0; n < tests.size(); n++)
      sum += tests.get(n);
      
      avg = (double)sum/tests.size();
      System.out.println("The test average is " + avg);
      System.out.println("Tests above average:");
      
      int y = 0;
      for(int z = 0; z < tests.size(); z++)
      {
      y = tests.get(z);
      if( y > avg)
      System.out.println(y);
      }
  }
  
}