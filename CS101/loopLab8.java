import java.util.ArrayList;
import java.util.Scanner;

public class loopLab8
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
     
      
   
      
      System.out.println(tests.toString());
      
      for(int l = 0; l < tests.size(); l++){
            for(int j = l + 1; j<tests.size(); j++){
                if(tests.get(l).equals(tests.get(j))){
                    tests.remove(j);
                    j--;
                }
            }
        }
     System.out.println(tests.toString());

  }
  
}